from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.crm_funnel_statuses import CrmFunnelStatuses
from ...types import Response


def _get_kwargs(
    funnel_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/crm/funnels/{funnel_id}/statuses",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CrmFunnelStatuses]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CrmFunnelStatuses.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CrmFunnelStatuses]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    funnel_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CrmFunnelStatuses]:
    """Get all funnel statuses

    Args:
        funnel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CrmFunnelStatuses]
    """

    kwargs = _get_kwargs(
        funnel_id=funnel_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    funnel_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CrmFunnelStatuses]:
    """Get all funnel statuses

    Args:
        funnel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CrmFunnelStatuses
    """

    return sync_detailed(
        funnel_id=funnel_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    funnel_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CrmFunnelStatuses]:
    """Get all funnel statuses

    Args:
        funnel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CrmFunnelStatuses]
    """

    kwargs = _get_kwargs(
        funnel_id=funnel_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    funnel_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CrmFunnelStatuses]:
    """Get all funnel statuses

    Args:
        funnel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CrmFunnelStatuses
    """

    return (
        await asyncio_detailed(
            funnel_id=funnel_id,
            client=client,
        )
    ).parsed
