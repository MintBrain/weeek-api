from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_tm_board_columns_response_200 import GetTmBoardColumnsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    board_id: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["boardId"] = board_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/tm/board-columns",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetTmBoardColumnsResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetTmBoardColumnsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetTmBoardColumnsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    board_id: Union[Unset, int] = UNSET,
) -> Response[GetTmBoardColumnsResponse200]:
    """Get board column list

    Args:
        board_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTmBoardColumnsResponse200]
    """

    kwargs = _get_kwargs(
        board_id=board_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    board_id: Union[Unset, int] = UNSET,
) -> Optional[GetTmBoardColumnsResponse200]:
    """Get board column list

    Args:
        board_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTmBoardColumnsResponse200
    """

    return sync_detailed(
        client=client,
        board_id=board_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    board_id: Union[Unset, int] = UNSET,
) -> Response[GetTmBoardColumnsResponse200]:
    """Get board column list

    Args:
        board_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTmBoardColumnsResponse200]
    """

    kwargs = _get_kwargs(
        board_id=board_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    board_id: Union[Unset, int] = UNSET,
) -> Optional[GetTmBoardColumnsResponse200]:
    """Get board column list

    Args:
        board_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTmBoardColumnsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            board_id=board_id,
        )
    ).parsed
