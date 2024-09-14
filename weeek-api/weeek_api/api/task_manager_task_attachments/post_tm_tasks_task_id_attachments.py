from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_tm_tasks_task_id_attachments_body import PostTmTasksTaskIdAttachmentsBody
from ...models.post_tm_tasks_task_id_attachments_response_200 import PostTmTasksTaskIdAttachmentsResponse200
from ...types import Response


def _get_kwargs(
    task_id: str,
    *,
    body: PostTmTasksTaskIdAttachmentsBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/tm/tasks/{task_id}/attachments",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostTmTasksTaskIdAttachmentsResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostTmTasksTaskIdAttachmentsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostTmTasksTaskIdAttachmentsResponse200]:
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
    body: PostTmTasksTaskIdAttachmentsBody,
) -> Response[PostTmTasksTaskIdAttachmentsResponse200]:
    """Upload attachments

    Args:
        task_id (str):
        body (PostTmTasksTaskIdAttachmentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTmTasksTaskIdAttachmentsResponse200]
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
    body: PostTmTasksTaskIdAttachmentsBody,
) -> Optional[PostTmTasksTaskIdAttachmentsResponse200]:
    """Upload attachments

    Args:
        task_id (str):
        body (PostTmTasksTaskIdAttachmentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTmTasksTaskIdAttachmentsResponse200
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
    body: PostTmTasksTaskIdAttachmentsBody,
) -> Response[PostTmTasksTaskIdAttachmentsResponse200]:
    """Upload attachments

    Args:
        task_id (str):
        body (PostTmTasksTaskIdAttachmentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTmTasksTaskIdAttachmentsResponse200]
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
    body: PostTmTasksTaskIdAttachmentsBody,
) -> Optional[PostTmTasksTaskIdAttachmentsResponse200]:
    """Upload attachments

    Args:
        task_id (str):
        body (PostTmTasksTaskIdAttachmentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTmTasksTaskIdAttachmentsResponse200
    """

    return (
        await asyncio_detailed(
            task_id=task_id,
            client=client,
            body=body,
        )
    ).parsed
