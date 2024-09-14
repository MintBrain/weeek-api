from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.phone_response import PhoneResponse
from ...models.put_crm_organizations_organization_id_phones_phone_id_body import (
    PutCrmOrganizationsOrganizationIdPhonesPhoneIdBody,
)
from ...types import Response


def _get_kwargs(
    organization_id: str,
    phone_id: str,
    *,
    body: PutCrmOrganizationsOrganizationIdPhonesPhoneIdBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/crm/organizations/{organization_id}/phones/{phone_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[PhoneResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PhoneResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[PhoneResponse]:
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
    body: PutCrmOrganizationsOrganizationIdPhonesPhoneIdBody,
) -> Response[PhoneResponse]:
    """Update the phone

    Args:
        organization_id (str):
        phone_id (str):
        body (PutCrmOrganizationsOrganizationIdPhonesPhoneIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PhoneResponse]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        phone_id=phone_id,
        body=body,
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
    body: PutCrmOrganizationsOrganizationIdPhonesPhoneIdBody,
) -> Optional[PhoneResponse]:
    """Update the phone

    Args:
        organization_id (str):
        phone_id (str):
        body (PutCrmOrganizationsOrganizationIdPhonesPhoneIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PhoneResponse
    """

    return sync_detailed(
        organization_id=organization_id,
        phone_id=phone_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    phone_id: str,
    *,
    client: AuthenticatedClient,
    body: PutCrmOrganizationsOrganizationIdPhonesPhoneIdBody,
) -> Response[PhoneResponse]:
    """Update the phone

    Args:
        organization_id (str):
        phone_id (str):
        body (PutCrmOrganizationsOrganizationIdPhonesPhoneIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PhoneResponse]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        phone_id=phone_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    phone_id: str,
    *,
    client: AuthenticatedClient,
    body: PutCrmOrganizationsOrganizationIdPhonesPhoneIdBody,
) -> Optional[PhoneResponse]:
    """Update the phone

    Args:
        organization_id (str):
        phone_id (str):
        body (PutCrmOrganizationsOrganizationIdPhonesPhoneIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PhoneResponse
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            phone_id=phone_id,
            client=client,
            body=body,
        )
    ).parsed
