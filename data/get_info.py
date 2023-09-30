import aiosqlite


async def get_user(id: int):
    async with aiosqlite.connect('db/bot.sqlite') as db:
        """user = await db.execute(
            f'SELECT * FROM users WHERE id = ?',
            (id, )
        )"""
        async with db.execute(f'SELECT * FROM users WHERE id = ?', (id,)) as cursor:
            async for user in cursor:
                return user
