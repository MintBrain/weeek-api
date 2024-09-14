from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_tm_tasks_task_id_watchers_response_200 import DeleteTmTasksTaskIdWatchersResponse200
from ...models.watchers import Watchers
from ...types import Response


def _get_kwargs(
    task_id: str,
    *,
    body: Watchers,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/tm/tasks/{task_id}/watchers",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DeleteTmTasksTaskIdWatchersResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeleteTmTasksTaskIdWatchersResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DeleteTmTasksTaskIdWatchersResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    task_id: str,
    *,
    client: AuthenticatedClient,
    body: Watchers,
) -> Response[DeleteTmTasksTaskIdWatchersResponse200]:
    """Remove watchers from a task

    Args:
        task_id (str):
        body (Watchers):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteTmTasksTaskIdWatchersResponse200]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    task_id: str,
    *,
    client: AuthenticatedClient,
    body: Watchers,
) -> Optional[DeleteTmTasksTaskIdWatchersResponse200]:
    """Remove watchers from a task

    Args:
        task_id (str):
        body (Watchers):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteTmTasksTaskIdWatchersResponse200
    """

    return sync_detailed(
        task_id=task_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    task_id: str,
    *,
    client: AuthenticatedClient,
    body: Watchers,
) -> Response[DeleteTmTasksTaskIdWatchersResponse200]:
    """Remove watchers from a task

    Args:
        task_id (str):
        body (Watchers):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteTmTasksTaskIdWatchersResponse200]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    task_id: str,
    *,
    client: AuthenticatedClient,
    body: Watchers,
) -> Optional[DeleteTmTasksTaskIdWatchersResponse200]:
    """Remove watchers from a task

    Args:
        task_id (str):
        body (Watchers):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteTmTasksTaskIdWatchersResponse200
    """

    return (
        await asyncio_detailed(
            task_id=task_id,
            client=client,
            body=body,
        )
    ).parsed
