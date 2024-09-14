from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.crm_funnel_status import CrmFunnelStatus
from ...models.funnel_status_manage_request import FunnelStatusManageRequest
from ...types import Response


def _get_kwargs(
    funnel_id: str,
    *,
    body: FunnelStatusManageRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/crm/funnels/{funnel_id}/statuses",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CrmFunnelStatus]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CrmFunnelStatus.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CrmFunnelStatus]:
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
    body: FunnelStatusManageRequest,
) -> Response[CrmFunnelStatus]:
    """Create a funnel status

    Args:
        funnel_id (str):
        body (FunnelStatusManageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CrmFunnelStatus]
    """

    kwargs = _get_kwargs(
        funnel_id=funnel_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    funnel_id: str,
    *,
    client: AuthenticatedClient,
    body: FunnelStatusManageRequest,
) -> Optional[CrmFunnelStatus]:
    """Create a funnel status

    Args:
        funnel_id (str):
        body (FunnelStatusManageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CrmFunnelStatus
    """

    return sync_detailed(
        funnel_id=funnel_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    funnel_id: str,
    *,
    client: AuthenticatedClient,
    body: FunnelStatusManageRequest,
) -> Response[CrmFunnelStatus]:
    """Create a funnel status

    Args:
        funnel_id (str):
        body (FunnelStatusManageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CrmFunnelStatus]
    """

    kwargs = _get_kwargs(
        funnel_id=funnel_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    funnel_id: str,
    *,
    client: AuthenticatedClient,
    body: FunnelStatusManageRequest,
) -> Optional[CrmFunnelStatus]:
    """Create a funnel status

    Args:
        funnel_id (str):
        body (FunnelStatusManageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CrmFunnelStatus
    """

    return (
        await asyncio_detailed(
            funnel_id=funnel_id,
            client=client,
            body=body,
        )
    ).parsed
