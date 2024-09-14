from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_field_update_body import CustomFieldUpdateBody
from ...models.put_tm_projects_project_id_custom_fields_id_response_200 import (
    PutTmProjectsProjectIdCustomFieldsIdResponse200,
)
from ...types import Response


def _get_kwargs(
    project_id: str,
    id: str,
    *,
    body: CustomFieldUpdateBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/tm/projects/{project_id}/custom-fields/{id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PutTmProjectsProjectIdCustomFieldsIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PutTmProjectsProjectIdCustomFieldsIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PutTmProjectsProjectIdCustomFieldsIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: CustomFieldUpdateBody,
) -> Response[PutTmProjectsProjectIdCustomFieldsIdResponse200]:
    """Update a custom field

    Args:
        project_id (str):
        id (str):
        body (CustomFieldUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutTmProjectsProjectIdCustomFieldsIdResponse200]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: CustomFieldUpdateBody,
) -> Optional[PutTmProjectsProjectIdCustomFieldsIdResponse200]:
    """Update a custom field

    Args:
        project_id (str):
        id (str):
        body (CustomFieldUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutTmProjectsProjectIdCustomFieldsIdResponse200
    """

    return sync_detailed(
        project_id=project_id,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: CustomFieldUpdateBody,
) -> Response[PutTmProjectsProjectIdCustomFieldsIdResponse200]:
    """Update a custom field

    Args:
        project_id (str):
        id (str):
        body (CustomFieldUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutTmProjectsProjectIdCustomFieldsIdResponse200]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: CustomFieldUpdateBody,
) -> Optional[PutTmProjectsProjectIdCustomFieldsIdResponse200]:
    """Update a custom field

    Args:
        project_id (str):
        id (str):
        body (CustomFieldUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutTmProjectsProjectIdCustomFieldsIdResponse200
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
