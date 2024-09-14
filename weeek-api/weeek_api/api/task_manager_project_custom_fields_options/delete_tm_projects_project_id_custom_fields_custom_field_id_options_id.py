from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_tm_projects_project_id_custom_fields_custom_field_id_options_id_response_200 import (
    DeleteTmProjectsProjectIdCustomFieldsCustomFieldIdOptionsIdResponse200,
)
from ...types import Response


def _get_kwargs(
    project_id: str,
    custom_field_id: str,
    id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/tm/projects/{project_id}/custom-fields/{custom_field_id}/options/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DeleteTmProjectsProjectIdCustomFieldsCustomFieldIdOptionsIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeleteTmProjectsProjectIdCustomFieldsCustomFieldIdOptionsIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DeleteTmProjectsProjectIdCustomFieldsCustomFieldIdOptionsIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    custom_field_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteTmProjectsProjectIdCustomFieldsCustomFieldIdOptionsIdResponse200]:
    """Delete a custom field option

    Args:
        project_id (str):
        custom_field_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteTmProjectsProjectIdCustomFieldsCustomFieldIdOptionsIdResponse200]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        custom_field_id=custom_field_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    custom_field_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[DeleteTmProjectsProjectIdCustomFieldsCustomFieldIdOptionsIdResponse200]:
    """Delete a custom field option

    Args:
        project_id (str):
        custom_field_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteTmProjectsProjectIdCustomFieldsCustomFieldIdOptionsIdResponse200
    """

    return sync_detailed(
        project_id=project_id,
        custom_field_id=custom_field_id,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    custom_field_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteTmProjectsProjectIdCustomFieldsCustomFieldIdOptionsIdResponse200]:
    """Delete a custom field option

    Args:
        project_id (str):
        custom_field_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteTmProjectsProjectIdCustomFieldsCustomFieldIdOptionsIdResponse200]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        custom_field_id=custom_field_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    custom_field_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[DeleteTmProjectsProjectIdCustomFieldsCustomFieldIdOptionsIdResponse200]:
    """Delete a custom field option

    Args:
        project_id (str):
        custom_field_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteTmProjectsProjectIdCustomFieldsCustomFieldIdOptionsIdResponse200
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            custom_field_id=custom_field_id,
            id=id,
            client=client,
        )
    ).parsed
