from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_crm_funnels_funnel_id_custom_fields_id_move_body import PostCrmFunnelsFunnelIdCustomFieldsIdMoveBody
from ...models.post_crm_funnels_funnel_id_custom_fields_id_move_response_200 import (
    PostCrmFunnelsFunnelIdCustomFieldsIdMoveResponse200,
)
from ...types import Response


def _get_kwargs(
    funnel_id: str,
    id: str,
    *,
    body: PostCrmFunnelsFunnelIdCustomFieldsIdMoveBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/crm/funnels/{funnel_id}/custom-fields/{id}/move",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostCrmFunnelsFunnelIdCustomFieldsIdMoveResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostCrmFunnelsFunnelIdCustomFieldsIdMoveResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostCrmFunnelsFunnelIdCustomFieldsIdMoveResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    funnel_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostCrmFunnelsFunnelIdCustomFieldsIdMoveBody,
) -> Response[PostCrmFunnelsFunnelIdCustomFieldsIdMoveResponse200]:
    """Move a custom field

    Args:
        funnel_id (str):
        id (str):
        body (PostCrmFunnelsFunnelIdCustomFieldsIdMoveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostCrmFunnelsFunnelIdCustomFieldsIdMoveResponse200]
    """

    kwargs = _get_kwargs(
        funnel_id=funnel_id,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    funnel_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostCrmFunnelsFunnelIdCustomFieldsIdMoveBody,
) -> Optional[PostCrmFunnelsFunnelIdCustomFieldsIdMoveResponse200]:
    """Move a custom field

    Args:
        funnel_id (str):
        id (str):
        body (PostCrmFunnelsFunnelIdCustomFieldsIdMoveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostCrmFunnelsFunnelIdCustomFieldsIdMoveResponse200
    """

    return sync_detailed(
        funnel_id=funnel_id,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    funnel_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostCrmFunnelsFunnelIdCustomFieldsIdMoveBody,
) -> Response[PostCrmFunnelsFunnelIdCustomFieldsIdMoveResponse200]:
    """Move a custom field

    Args:
        funnel_id (str):
        id (str):
        body (PostCrmFunnelsFunnelIdCustomFieldsIdMoveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostCrmFunnelsFunnelIdCustomFieldsIdMoveResponse200]
    """

    kwargs = _get_kwargs(
        funnel_id=funnel_id,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    funnel_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostCrmFunnelsFunnelIdCustomFieldsIdMoveBody,
) -> Optional[PostCrmFunnelsFunnelIdCustomFieldsIdMoveResponse200]:
    """Move a custom field

    Args:
        funnel_id (str):
        id (str):
        body (PostCrmFunnelsFunnelIdCustomFieldsIdMoveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostCrmFunnelsFunnelIdCustomFieldsIdMoveResponse200
    """

    return (
        await asyncio_detailed(
            funnel_id=funnel_id,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
