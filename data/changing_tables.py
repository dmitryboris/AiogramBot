import aiosqlite


async def add_user(id: int, name: str):
    async with aiosqlite.connect('db/bot.sqlite') as db:
        await db.execute(
            f'INSERT INTO users(id, name, count_of_orders) VALUES (?, ?, ?)',
            (id, name, 0)
        )
        await db.commit()
