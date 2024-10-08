from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.email_response_1 import EmailResponse1
from ...models.put_crm_contacts_contact_id_emails_email_id_body import PutCrmContactsContactIdEmailsEmailIdBody
from ...types import Response


def _get_kwargs(
    contact_id: str,
    email_id: str,
    *,
    body: PutCrmContactsContactIdEmailsEmailIdBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/crm/contacts/{contact_id}/emails/{email_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[EmailResponse1]:
    if response.status_code == HTTPStatus.OK:
        response_200 = EmailResponse1.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[EmailResponse1]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    contact_id: str,
    email_id: str,
    *,
    client: AuthenticatedClient,
    body: PutCrmContactsContactIdEmailsEmailIdBody,
) -> Response[EmailResponse1]:
    """Update the email

    Args:
        contact_id (str):
        email_id (str):
        body (PutCrmContactsContactIdEmailsEmailIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailResponse1]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        email_id=email_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    contact_id: str,
    email_id: str,
    *,
    client: AuthenticatedClient,
    body: PutCrmContactsContactIdEmailsEmailIdBody,
) -> Optional[EmailResponse1]:
    """Update the email

    Args:
        contact_id (str):
        email_id (str):
        body (PutCrmContactsContactIdEmailsEmailIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailResponse1
    """

    return sync_detailed(
        contact_id=contact_id,
        email_id=email_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    contact_id: str,
    email_id: str,
    *,
    client: AuthenticatedClient,
    body: PutCrmContactsContactIdEmailsEmailIdBody,
) -> Response[EmailResponse1]:
    """Update the email

    Args:
        contact_id (str):
        email_id (str):
        body (PutCrmContactsContactIdEmailsEmailIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailResponse1]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        email_id=email_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    contact_id: str,
    email_id: str,
    *,
    client: AuthenticatedClient,
    body: PutCrmContactsContactIdEmailsEmailIdBody,
) -> Optional[EmailResponse1]:
    """Update the email

    Args:
        contact_id (str):
        email_id (str):
        body (PutCrmContactsContactIdEmailsEmailIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailResponse1
    """

    return (
        await asyncio_detailed(
            contact_id=contact_id,
            email_id=email_id,
            client=client,
            body=body,
        )
    ).parsed
