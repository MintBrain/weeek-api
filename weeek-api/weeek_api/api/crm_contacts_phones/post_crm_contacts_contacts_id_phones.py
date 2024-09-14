from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.phone_response_1 import PhoneResponse1
from ...models.post_crm_contacts_contacts_id_phones_body import PostCrmContactsContactsIdPhonesBody
from ...types import Response


def _get_kwargs(
    contacts_id: str,
    *,
    body: PostCrmContactsContactsIdPhonesBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/crm/contacts/{contacts_id}/phones",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PhoneResponse1]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PhoneResponse1.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PhoneResponse1]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    contacts_id: str,
    *,
    client: AuthenticatedClient,
    body: PostCrmContactsContactsIdPhonesBody,
) -> Response[PhoneResponse1]:
    """Create a phone

    Args:
        contacts_id (str):
        body (PostCrmContactsContactsIdPhonesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PhoneResponse1]
    """

    kwargs = _get_kwargs(
        contacts_id=contacts_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    contacts_id: str,
    *,
    client: AuthenticatedClient,
    body: PostCrmContactsContactsIdPhonesBody,
) -> Optional[PhoneResponse1]:
    """Create a phone

    Args:
        contacts_id (str):
        body (PostCrmContactsContactsIdPhonesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PhoneResponse1
    """

    return sync_detailed(
        contacts_id=contacts_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    contacts_id: str,
    *,
    client: AuthenticatedClient,
    body: PostCrmContactsContactsIdPhonesBody,
) -> Response[PhoneResponse1]:
    """Create a phone

    Args:
        contacts_id (str):
        body (PostCrmContactsContactsIdPhonesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PhoneResponse1]
    """

    kwargs = _get_kwargs(
        contacts_id=contacts_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    contacts_id: str,
    *,
    client: AuthenticatedClient,
    body: PostCrmContactsContactsIdPhonesBody,
) -> Optional[PhoneResponse1]:
    """Create a phone

    Args:
        contacts_id (str):
        body (PostCrmContactsContactsIdPhonesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PhoneResponse1
    """

    return (
        await asyncio_detailed(
            contacts_id=contacts_id,
            client=client,
            body=body,
        )
    ).parsed
