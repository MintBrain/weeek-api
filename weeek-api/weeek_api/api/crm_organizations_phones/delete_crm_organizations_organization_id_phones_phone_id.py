from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.successful_response import SuccessfulResponse
from ...types import Response


def _get_kwargs(
    organization_id: str,
    phone_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/crm/organizations/{organization_id}/phones/{phone_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SuccessfulResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SuccessfulResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SuccessfulResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    phone_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[SuccessfulResponse]:
    """Delete the phone

    Args:
        organization_id (str):
        phone_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuccessfulResponse]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        phone_id=phone_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    phone_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[SuccessfulResponse]:
    """Delete the phone

    Args:
        organization_id (str):
        phone_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuccessfulResponse
    """

    return sync_detailed(
        organization_id=organization_id,
        phone_id=phone_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    phone_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[SuccessfulResponse]:
    """Delete the phone

    Args:
        organization_id (str):
        phone_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuccessfulResponse]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        phone_id=phone_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    phone_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[SuccessfulResponse]:
    """Delete the phone

    Args:
        organization_id (str):
        phone_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuccessfulResponse
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            phone_id=phone_id,
            client=client,
        )
    ).parsed
