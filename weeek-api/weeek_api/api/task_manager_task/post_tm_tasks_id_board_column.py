from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_tm_tasks_id_board_column_body import PostTmTasksIdBoardColumnBody
from ...models.post_tm_tasks_id_board_column_response_200 import PostTmTasksIdBoardColumnResponse200
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: PostTmTasksIdBoardColumnBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/tm/tasks/{id}/board-column",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostTmTasksIdBoardColumnResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostTmTasksIdBoardColumnResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostTmTasksIdBoardColumnResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostTmTasksIdBoardColumnBody,
) -> Response[PostTmTasksIdBoardColumnResponse200]:
    """Change board column

    Args:
        id (str):
        body (PostTmTasksIdBoardColumnBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTmTasksIdBoardColumnResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostTmTasksIdBoardColumnBody,
) -> Optional[PostTmTasksIdBoardColumnResponse200]:
    """Change board column

    Args:
        id (str):
        body (PostTmTasksIdBoardColumnBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTmTasksIdBoardColumnResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostTmTasksIdBoardColumnBody,
) -> Response[PostTmTasksIdBoardColumnResponse200]:
    """Change board column

    Args:
        id (str):
        body (PostTmTasksIdBoardColumnBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTmTasksIdBoardColumnResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostTmTasksIdBoardColumnBody,
) -> Optional[PostTmTasksIdBoardColumnResponse200]:
    """Change board column

    Args:
        id (str):
        body (PostTmTasksIdBoardColumnBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTmTasksIdBoardColumnResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
