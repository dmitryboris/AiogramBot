import aiosqlite
import asyncio


async def create(db_file):
    conn_str = f'sqlite:///{db_file}'
    conn = await aiosqlite.connect(conn_str)
    await conn.execute(
        """CREATE TABLE users (
        id int PRIMARY KEY  
        """
    )


async def main():
    await create(1)


asyncio.get_event_loop().run_until_complete(create('./db/test.sqlite'))