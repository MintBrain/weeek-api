from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.crm_deals import CrmDeals
from ...types import UNSET, Response, Unset


def _get_kwargs(
    status_id: str,
    *,
    search: Union[Unset, str] = UNSET,
    executor_ids: Union[Unset, List[str]] = UNSET,
    win_statuses: Union[Unset, List[str]] = UNSET,
    last_updated: Union[Unset, List[str]] = UNSET,
    tags: Union[Unset, List[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["search"] = search

    json_executor_ids: Union[Unset, List[str]] = UNSET
    if not isinstance(executor_ids, Unset):
        json_executor_ids = executor_ids

    params["executorIds"] = json_executor_ids

    json_win_statuses: Union[Unset, List[str]] = UNSET
    if not isinstance(win_statuses, Unset):
        json_win_statuses = win_statuses

    params["winStatuses"] = json_win_statuses

    json_last_updated: Union[Unset, List[str]] = UNSET
    if not isinstance(last_updated, Unset):
        json_last_updated = last_updated

    params["lastUpdated"] = json_last_updated

    json_tags: Union[Unset, List[str]] = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags"] = json_tags

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/crm/statuses/{status_id}/deals",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[CrmDeals]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CrmDeals.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[CrmDeals]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    status_id: str,
    *,
    client: AuthenticatedClient,
    search: Union[Unset, str] = UNSET,
    executor_ids: Union[Unset, List[str]] = UNSET,
    win_statuses: Union[Unset, List[str]] = UNSET,
    last_updated: Union[Unset, List[str]] = UNSET,
    tags: Union[Unset, List[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[CrmDeals]:
    """Get all deals

    Args:
        status_id (str):
        search (Union[Unset, str]):
        executor_ids (Union[Unset, List[str]]):
        win_statuses (Union[Unset, List[str]]):
        last_updated (Union[Unset, List[str]]):
        tags (Union[Unset, List[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CrmDeals]
    """

    kwargs = _get_kwargs(
        status_id=status_id,
        search=search,
        executor_ids=executor_ids,
        win_statuses=win_statuses,
        last_updated=last_updated,
        tags=tags,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    status_id: str,
    *,
    client: AuthenticatedClient,
    search: Union[Unset, str] = UNSET,
    executor_ids: Union[Unset, List[str]] = UNSET,
    win_statuses: Union[Unset, List[str]] = UNSET,
    last_updated: Union[Unset, List[str]] = UNSET,
    tags: Union[Unset, List[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[CrmDeals]:
    """Get all deals

    Args:
        status_id (str):
        search (Union[Unset, str]):
        executor_ids (Union[Unset, List[str]]):
        win_statuses (Union[Unset, List[str]]):
        last_updated (Union[Unset, List[str]]):
        tags (Union[Unset, List[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CrmDeals
    """

    return sync_detailed(
        status_id=status_id,
        client=client,
        search=search,
        executor_ids=executor_ids,
        win_statuses=win_statuses,
        last_updated=last_updated,
        tags=tags,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    status_id: str,
    *,
    client: AuthenticatedClient,
    search: Union[Unset, str] = UNSET,
    executor_ids: Union[Unset, List[str]] = UNSET,
    win_statuses: Union[Unset, List[str]] = UNSET,
    last_updated: Union[Unset, List[str]] = UNSET,
    tags: Union[Unset, List[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[CrmDeals]:
    """Get all deals

    Args:
        status_id (str):
        search (Union[Unset, str]):
        executor_ids (Union[Unset, List[str]]):
        win_statuses (Union[Unset, List[str]]):
        last_updated (Union[Unset, List[str]]):
        tags (Union[Unset, List[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CrmDeals]
    """

    kwargs = _get_kwargs(
        status_id=status_id,
        search=search,
        executor_ids=executor_ids,
        win_statuses=win_statuses,
        last_updated=last_updated,
        tags=tags,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    status_id: str,
    *,
    client: AuthenticatedClient,
    search: Union[Unset, str] = UNSET,
    executor_ids: Union[Unset, List[str]] = UNSET,
    win_statuses: Union[Unset, List[str]] = UNSET,
    last_updated: Union[Unset, List[str]] = UNSET,
    tags: Union[Unset, List[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[CrmDeals]:
    """Get all deals

    Args:
        status_id (str):
        search (Union[Unset, str]):
        executor_ids (Union[Unset, List[str]]):
        win_statuses (Union[Unset, List[str]]):
        last_updated (Union[Unset, List[str]]):
        tags (Union[Unset, List[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CrmDeals
    """

    return (
        await asyncio_detailed(
            status_id=status_id,
            client=client,
            search=search,
            executor_ids=executor_ids,
            win_statuses=win_statuses,
            last_updated=last_updated,
            tags=tags,
            limit=limit,
            offset=offset,
        )
    ).parsed
