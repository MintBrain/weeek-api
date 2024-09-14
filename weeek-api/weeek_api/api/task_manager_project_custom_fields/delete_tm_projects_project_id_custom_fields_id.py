from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_tm_projects_project_id_custom_fields_id_response_200 import (
    DeleteTmProjectsProjectIdCustomFieldsIdResponse200,
)
from ...types import Response


def _get_kwargs(
    project_id: str,
    id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/tm/projects/{project_id}/custom-fields/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DeleteTmProjectsProjectIdCustomFieldsIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeleteTmProjectsProjectIdCustomFieldsIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DeleteTmProjectsProjectIdCustomFieldsIdResponse200]:
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
) -> Response[DeleteTmProjectsProjectIdCustomFieldsIdResponse200]:
    """Delete a custom field

    Args:
        project_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteTmProjectsProjectIdCustomFieldsIdResponse200]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        id=id,
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
) -> Optional[DeleteTmProjectsProjectIdCustomFieldsIdResponse200]:
    """Delete a custom field

    Args:
        project_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteTmProjectsProjectIdCustomFieldsIdResponse200
    """

    return sync_detailed(
        project_id=project_id,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteTmProjectsProjectIdCustomFieldsIdResponse200]:
    """Delete a custom field

    Args:
        project_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteTmProjectsProjectIdCustomFieldsIdResponse200]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[DeleteTmProjectsProjectIdCustomFieldsIdResponse200]:
    """Delete a custom field

    Args:
        project_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteTmProjectsProjectIdCustomFieldsIdResponse200
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            id=id,
            client=client,
        )
    ).parsed
