from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_ws_tags_id_response_200 import GetWsTagsIdResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    content_type: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(content_type, Unset):
        headers["Content-Type"] = content_type

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/ws/tags/{id}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetWsTagsIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetWsTagsIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetWsTagsIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    content_type: Union[Unset, str] = UNSET,
) -> Response[GetWsTagsIdResponse200]:
    """Tag

    Args:
        id (int):
        content_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWsTagsIdResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        content_type=content_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    content_type: Union[Unset, str] = UNSET,
) -> Optional[GetWsTagsIdResponse200]:
    """Tag

    Args:
        id (int):
        content_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWsTagsIdResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        content_type=content_type,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    content_type: Union[Unset, str] = UNSET,
) -> Response[GetWsTagsIdResponse200]:
    """Tag

    Args:
        id (int):
        content_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWsTagsIdResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        content_type=content_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    content_type: Union[Unset, str] = UNSET,
) -> Optional[GetWsTagsIdResponse200]:
    """Tag

    Args:
        id (int):
        content_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWsTagsIdResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            content_type=content_type,
        )
    ).parsed
