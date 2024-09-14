from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_crm_deals_deal_id_attachments_body import PostCrmDealsDealIdAttachmentsBody
from ...models.post_crm_deals_deal_id_attachments_response_200 import PostCrmDealsDealIdAttachmentsResponse200
from ...types import Response


def _get_kwargs(
    deal_id: str,
    *,
    body: PostCrmDealsDealIdAttachmentsBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/crm/deals/{deal_id}/attachments",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostCrmDealsDealIdAttachmentsResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostCrmDealsDealIdAttachmentsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostCrmDealsDealIdAttachmentsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    deal_id: str,
    *,
    client: AuthenticatedClient,
    body: PostCrmDealsDealIdAttachmentsBody,
) -> Response[PostCrmDealsDealIdAttachmentsResponse200]:
    """Upload attachments

    Args:
        deal_id (str):
        body (PostCrmDealsDealIdAttachmentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostCrmDealsDealIdAttachmentsResponse200]
    """

    kwargs = _get_kwargs(
        deal_id=deal_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    deal_id: str,
    *,
    client: AuthenticatedClient,
    body: PostCrmDealsDealIdAttachmentsBody,
) -> Optional[PostCrmDealsDealIdAttachmentsResponse200]:
    """Upload attachments

    Args:
        deal_id (str):
        body (PostCrmDealsDealIdAttachmentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostCrmDealsDealIdAttachmentsResponse200
    """

    return sync_detailed(
        deal_id=deal_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    deal_id: str,
    *,
    client: AuthenticatedClient,
    body: PostCrmDealsDealIdAttachmentsBody,
) -> Response[PostCrmDealsDealIdAttachmentsResponse200]:
    """Upload attachments

    Args:
        deal_id (str):
        body (PostCrmDealsDealIdAttachmentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostCrmDealsDealIdAttachmentsResponse200]
    """

    kwargs = _get_kwargs(
        deal_id=deal_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    deal_id: str,
    *,
    client: AuthenticatedClient,
    body: PostCrmDealsDealIdAttachmentsBody,
) -> Optional[PostCrmDealsDealIdAttachmentsResponse200]:
    """Upload attachments

    Args:
        deal_id (str):
        body (PostCrmDealsDealIdAttachmentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostCrmDealsDealIdAttachmentsResponse200
    """

    return (
        await asyncio_detailed(
            deal_id=deal_id,
            client=client,
            body=body,
        )
    ).parsed
