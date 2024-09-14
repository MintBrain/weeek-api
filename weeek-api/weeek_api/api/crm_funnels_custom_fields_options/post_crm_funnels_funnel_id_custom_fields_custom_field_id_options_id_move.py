from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_crm_funnels_funnel_id_custom_fields_custom_field_id_options_id_move_body import (
    PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveBody,
)
from ...models.post_crm_funnels_funnel_id_custom_fields_custom_field_id_options_id_move_response_200 import (
    PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveResponse200,
)
from ...types import Response


def _get_kwargs(
    funnel_id: str,
    custom_field_id: str,
    id: str,
    *,
    body: PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/crm/funnels/{funnel_id}/custom-fields/{custom_field_id}/options/{id}/move",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveResponse200.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    funnel_id: str,
    custom_field_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveBody,
) -> Response[PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveResponse200]:
    """Move a custom field option

    Args:
        funnel_id (str):
        custom_field_id (str):
        id (str):
        body (PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveResponse200]
    """

    kwargs = _get_kwargs(
        funnel_id=funnel_id,
        custom_field_id=custom_field_id,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    funnel_id: str,
    custom_field_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveBody,
) -> Optional[PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveResponse200]:
    """Move a custom field option

    Args:
        funnel_id (str):
        custom_field_id (str):
        id (str):
        body (PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveResponse200
    """

    return sync_detailed(
        funnel_id=funnel_id,
        custom_field_id=custom_field_id,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    funnel_id: str,
    custom_field_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveBody,
) -> Response[PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveResponse200]:
    """Move a custom field option

    Args:
        funnel_id (str):
        custom_field_id (str):
        id (str):
        body (PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveResponse200]
    """

    kwargs = _get_kwargs(
        funnel_id=funnel_id,
        custom_field_id=custom_field_id,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    funnel_id: str,
    custom_field_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveBody,
) -> Optional[PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveResponse200]:
    """Move a custom field option

    Args:
        funnel_id (str):
        custom_field_id (str):
        id (str):
        body (PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveResponse200
    """

    return (
        await asyncio_detailed(
            funnel_id=funnel_id,
            custom_field_id=custom_field_id,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
