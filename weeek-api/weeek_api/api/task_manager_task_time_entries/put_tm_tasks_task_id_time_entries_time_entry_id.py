from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_tm_tasks_task_id_time_entries_time_entry_id_response_200 import (
    PutTmTasksTaskIdTimeEntriesTimeEntryIdResponse200,
)
from ...models.time_entry_request import TimeEntryRequest
from ...types import Response


def _get_kwargs(
    task_id: str,
    time_entry_id: str,
    *,
    body: TimeEntryRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/tm/tasks/{task_id}/time-entries/{time_entry_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PutTmTasksTaskIdTimeEntriesTimeEntryIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PutTmTasksTaskIdTimeEntriesTimeEntryIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PutTmTasksTaskIdTimeEntriesTimeEntryIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    task_id: str,
    time_entry_id: str,
    *,
    client: AuthenticatedClient,
    body: TimeEntryRequest,
) -> Response[PutTmTasksTaskIdTimeEntriesTimeEntryIdResponse200]:
    """Update a time entry

    Args:
        task_id (str):
        time_entry_id (str):
        body (TimeEntryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutTmTasksTaskIdTimeEntriesTimeEntryIdResponse200]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        time_entry_id=time_entry_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    task_id: str,
    time_entry_id: str,
    *,
    client: AuthenticatedClient,
    body: TimeEntryRequest,
) -> Optional[PutTmTasksTaskIdTimeEntriesTimeEntryIdResponse200]:
    """Update a time entry

    Args:
        task_id (str):
        time_entry_id (str):
        body (TimeEntryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutTmTasksTaskIdTimeEntriesTimeEntryIdResponse200
    """

    return sync_detailed(
        task_id=task_id,
        time_entry_id=time_entry_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    task_id: str,
    time_entry_id: str,
    *,
    client: AuthenticatedClient,
    body: TimeEntryRequest,
) -> Response[PutTmTasksTaskIdTimeEntriesTimeEntryIdResponse200]:
    """Update a time entry

    Args:
        task_id (str):
        time_entry_id (str):
        body (TimeEntryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutTmTasksTaskIdTimeEntriesTimeEntryIdResponse200]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        time_entry_id=time_entry_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    task_id: str,
    time_entry_id: str,
    *,
    client: AuthenticatedClient,
    body: TimeEntryRequest,
) -> Optional[PutTmTasksTaskIdTimeEntriesTimeEntryIdResponse200]:
    """Update a time entry

    Args:
        task_id (str):
        time_entry_id (str):
        body (TimeEntryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutTmTasksTaskIdTimeEntriesTimeEntryIdResponse200
    """

    return (
        await asyncio_detailed(
            task_id=task_id,
            time_entry_id=time_entry_id,
            client=client,
            body=body,
        )
    ).parsed
