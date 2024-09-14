import logs
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "weeek-api"))

import asyncio
from weeek_api import AuthenticatedClient
from weeek_api.models import *
from weeek_api.api.workspace import get_ws
from weeek_api.api.task_manager_project import get_tm_projects
from weeek_api.api.task_manager_task import post_tm_tasks, delete_tm_tasks_id

from config_reader import config

client: AuthenticatedClient
project_id = 2

async def create_task():
    res = await post_tm_tasks.asyncio(client=client, body=PostTmTasksBody(type=TaskType.ACTION))
    res2 = await delete_tm_tasks_id.asyncio(str(res.task.id), client=client)
    pass

async def program():
    if (res := await get_tm_projects.asyncio(client=client)) is not None:
        pass
    proj = res.projects
    res2: GetWsResponse200 = await get_ws.asyncio(client=client)
    await create_task()
    pass

async def main():
    global client
    client = AuthenticatedClient(base_url=config.api_url.get_secret_value(), token=config.api_token.get_secret_value())
    await program()

if __name__ == '__main__':
    asyncio.run(main())
