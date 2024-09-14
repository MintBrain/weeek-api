from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_tm_tasks_response_200 import GetTmTasksResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    day: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    project_id: Union[Unset, int] = UNSET,
    completed: Union[Unset, bool] = UNSET,
    board_id: Union[Unset, int] = UNSET,
    board_column_id: Union[Unset, int] = UNSET,
    type: Union[Unset, str] = UNSET,
    priority: Union[Unset, int] = UNSET,
    search: Union[Unset, str] = UNSET,
    per_page: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    all_: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["day"] = day

    params["userId"] = user_id

    params["projectId"] = project_id

    params["completed"] = completed

    params["boardId"] = board_id

    params["boardColumnId"] = board_column_id

    params["type"] = type

    params["priority"] = priority

    params["search"] = search

    params["perPage"] = per_page

    params["offset"] = offset

    params["sortBy"] = sort_by

    params["startDate"] = start_date

    params["endDate"] = end_date

    params["all"] = all_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/tm/tasks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetTmTasksResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetTmTasksResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetTmTasksResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    day: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    project_id: Union[Unset, int] = UNSET,
    completed: Union[Unset, bool] = UNSET,
    board_id: Union[Unset, int] = UNSET,
    board_column_id: Union[Unset, int] = UNSET,
    type: Union[Unset, str] = UNSET,
    priority: Union[Unset, int] = UNSET,
    search: Union[Unset, str] = UNSET,
    per_page: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    all_: Union[Unset, bool] = UNSET,
) -> Response[GetTmTasksResponse200]:
    """Get tasks

     Get tasks

    Args:
        day (Union[Unset, str]):
        user_id (Union[Unset, str]):
        project_id (Union[Unset, int]):
        completed (Union[Unset, bool]):
        board_id (Union[Unset, int]):
        board_column_id (Union[Unset, int]):
        type (Union[Unset, str]):
        priority (Union[Unset, int]):
        search (Union[Unset, str]):
        per_page (Union[Unset, int]):
        offset (Union[Unset, int]):
        sort_by (Union[Unset, str]):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        all_ (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTmTasksResponse200]
    """

    kwargs = _get_kwargs(
        day=day,
        user_id=user_id,
        project_id=project_id,
        completed=completed,
        board_id=board_id,
        board_column_id=board_column_id,
        type=type,
        priority=priority,
        search=search,
        per_page=per_page,
        offset=offset,
        sort_by=sort_by,
        start_date=start_date,
        end_date=end_date,
        all_=all_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    day: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    project_id: Union[Unset, int] = UNSET,
    completed: Union[Unset, bool] = UNSET,
    board_id: Union[Unset, int] = UNSET,
    board_column_id: Union[Unset, int] = UNSET,
    type: Union[Unset, str] = UNSET,
    priority: Union[Unset, int] = UNSET,
    search: Union[Unset, str] = UNSET,
    per_page: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    all_: Union[Unset, bool] = UNSET,
) -> Optional[GetTmTasksResponse200]:
    """Get tasks

     Get tasks

    Args:
        day (Union[Unset, str]):
        user_id (Union[Unset, str]):
        project_id (Union[Unset, int]):
        completed (Union[Unset, bool]):
        board_id (Union[Unset, int]):
        board_column_id (Union[Unset, int]):
        type (Union[Unset, str]):
        priority (Union[Unset, int]):
        search (Union[Unset, str]):
        per_page (Union[Unset, int]):
        offset (Union[Unset, int]):
        sort_by (Union[Unset, str]):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        all_ (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTmTasksResponse200
    """

    return sync_detailed(
        client=client,
        day=day,
        user_id=user_id,
        project_id=project_id,
        completed=completed,
        board_id=board_id,
        board_column_id=board_column_id,
        type=type,
        priority=priority,
        search=search,
        per_page=per_page,
        offset=offset,
        sort_by=sort_by,
        start_date=start_date,
        end_date=end_date,
        all_=all_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    day: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    project_id: Union[Unset, int] = UNSET,
    completed: Union[Unset, bool] = UNSET,
    board_id: Union[Unset, int] = UNSET,
    board_column_id: Union[Unset, int] = UNSET,
    type: Union[Unset, str] = UNSET,
    priority: Union[Unset, int] = UNSET,
    search: Union[Unset, str] = UNSET,
    per_page: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    all_: Union[Unset, bool] = UNSET,
) -> Response[GetTmTasksResponse200]:
    """Get tasks

     Get tasks

    Args:
        day (Union[Unset, str]):
        user_id (Union[Unset, str]):
        project_id (Union[Unset, int]):
        completed (Union[Unset, bool]):
        board_id (Union[Unset, int]):
        board_column_id (Union[Unset, int]):
        type (Union[Unset, str]):
        priority (Union[Unset, int]):
        search (Union[Unset, str]):
        per_page (Union[Unset, int]):
        offset (Union[Unset, int]):
        sort_by (Union[Unset, str]):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        all_ (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTmTasksResponse200]
    """

    kwargs = _get_kwargs(
        day=day,
        user_id=user_id,
        project_id=project_id,
        completed=completed,
        board_id=board_id,
        board_column_id=board_column_id,
        type=type,
        priority=priority,
        search=search,
        per_page=per_page,
        offset=offset,
        sort_by=sort_by,
        start_date=start_date,
        end_date=end_date,
        all_=all_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    day: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    project_id: Union[Unset, int] = UNSET,
    completed: Union[Unset, bool] = UNSET,
    board_id: Union[Unset, int] = UNSET,
    board_column_id: Union[Unset, int] = UNSET,
    type: Union[Unset, str] = UNSET,
    priority: Union[Unset, int] = UNSET,
    search: Union[Unset, str] = UNSET,
    per_page: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    all_: Union[Unset, bool] = UNSET,
) -> Optional[GetTmTasksResponse200]:
    """Get tasks

     Get tasks

    Args:
        day (Union[Unset, str]):
        user_id (Union[Unset, str]):
        project_id (Union[Unset, int]):
        completed (Union[Unset, bool]):
        board_id (Union[Unset, int]):
        board_column_id (Union[Unset, int]):
        type (Union[Unset, str]):
        priority (Union[Unset, int]):
        search (Union[Unset, str]):
        per_page (Union[Unset, int]):
        offset (Union[Unset, int]):
        sort_by (Union[Unset, str]):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        all_ (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTmTasksResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            day=day,
            user_id=user_id,
            project_id=project_id,
            completed=completed,
            board_id=board_id,
            board_column_id=board_column_id,
            type=type,
            priority=priority,
            search=search,
            per_page=per_page,
            offset=offset,
            sort_by=sort_by,
            start_date=start_date,
            end_date=end_date,
            all_=all_,
        )
    ).parsed
