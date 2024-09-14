from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.crm_deal import CrmDeal
from ...models.deal_create_request import DealCreateRequest
from ...types import Response


def _get_kwargs(
    status_id: str,
    *,
    body: DealCreateRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/crm/statuses/{status_id}/deals",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[CrmDeal]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CrmDeal.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[CrmDeal]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    status_id: str,
    *,
    client: AuthenticatedClient,
    body: DealCreateRequest,
) -> Response[CrmDeal]:
    """Create a deal

    Args:
        status_id (str):
        body (DealCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CrmDeal]
    """

    kwargs = _get_kwargs(
        status_id=status_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    status_id: str,
    *,
    client: AuthenticatedClient,
    body: DealCreateRequest,
) -> Optional[CrmDeal]:
    """Create a deal

    Args:
        status_id (str):
        body (DealCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CrmDeal
    """

    return sync_detailed(
        status_id=status_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    status_id: str,
    *,
    client: AuthenticatedClient,
    body: DealCreateRequest,
) -> Response[CrmDeal]:
    """Create a deal

    Args:
        status_id (str):
        body (DealCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CrmDeal]
    """

    kwargs = _get_kwargs(
        status_id=status_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    status_id: str,
    *,
    client: AuthenticatedClient,
    body: DealCreateRequest,
) -> Optional[CrmDeal]:
    """Create a deal

    Args:
        status_id (str):
        body (DealCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CrmDeal
    """

    return (
        await asyncio_detailed(
            status_id=status_id,
            client=client,
            body=body,
        )
    ).parsed
