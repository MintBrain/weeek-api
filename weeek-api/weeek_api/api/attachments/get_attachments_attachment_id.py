from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_attachments_attachment_id_response_200 import GetAttachmentsAttachmentIdResponse200
from ...types import Response


def _get_kwargs(
    attachment_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/attachments/{attachment_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetAttachmentsAttachmentIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetAttachmentsAttachmentIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetAttachmentsAttachmentIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    attachment_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[GetAttachmentsAttachmentIdResponse200]:
    """Get an attachment

    Args:
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAttachmentsAttachmentIdResponse200]
    """

    kwargs = _get_kwargs(
        attachment_id=attachment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    attachment_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[GetAttachmentsAttachmentIdResponse200]:
    """Get an attachment

    Args:
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAttachmentsAttachmentIdResponse200
    """

    return sync_detailed(
        attachment_id=attachment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    attachment_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[GetAttachmentsAttachmentIdResponse200]:
    """Get an attachment

    Args:
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAttachmentsAttachmentIdResponse200]
    """

    kwargs = _get_kwargs(
        attachment_id=attachment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    attachment_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[GetAttachmentsAttachmentIdResponse200]:
    """Get an attachment

    Args:
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAttachmentsAttachmentIdResponse200
    """

    return (
        await asyncio_detailed(
            attachment_id=attachment_id,
            client=client,
        )
    ).parsed
