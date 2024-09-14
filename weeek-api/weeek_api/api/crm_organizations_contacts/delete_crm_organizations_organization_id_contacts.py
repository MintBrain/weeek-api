from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_crm_organizations_organization_id_contacts_body import (
    DeleteCrmOrganizationsOrganizationIdContactsBody,
)
from ...models.successful_response import SuccessfulResponse
from ...types import Response


def _get_kwargs(
    organization_id: str,
    *,
    body: DeleteCrmOrganizationsOrganizationIdContactsBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/crm/organizations/{organization_id}/contacts",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    *,
    client: AuthenticatedClient,
    body: DeleteCrmOrganizationsOrganizationIdContactsBody,
) -> Response[SuccessfulResponse]:
    """Detach the contact

    Args:
        organization_id (str):
        body (DeleteCrmOrganizationsOrganizationIdContactsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuccessfulResponse]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    body: DeleteCrmOrganizationsOrganizationIdContactsBody,
) -> Optional[SuccessfulResponse]:
    """Detach the contact

    Args:
        organization_id (str):
        body (DeleteCrmOrganizationsOrganizationIdContactsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuccessfulResponse
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    body: DeleteCrmOrganizationsOrganizationIdContactsBody,
) -> Response[SuccessfulResponse]:
    """Detach the contact

    Args:
        organization_id (str):
        body (DeleteCrmOrganizationsOrganizationIdContactsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuccessfulResponse]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    body: DeleteCrmOrganizationsOrganizationIdContactsBody,
) -> Optional[SuccessfulResponse]:
    """Detach the contact

    Args:
        organization_id (str):
        body (DeleteCrmOrganizationsOrganizationIdContactsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuccessfulResponse
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            body=body,
        )
    ).parsed
