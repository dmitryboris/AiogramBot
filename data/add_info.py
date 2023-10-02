import aiosqlite

subscriptions = {
    "Essential": 100,
    "Extra": 200,
    "Deluxe": 300,
    "EA Play Plus": 100,
    "EA Play Pro": 400,
    "PC": 100,
    "Console": 200,
    "Ultimate": 400
}


async def add_user(id: int, name: str):
    async with aiosqlite.connect('db/bot.sqlite') as db:
        await db.execute(
            f'INSERT INTO users(id, name, count_of_orders) VALUES (?, ?, ?)',
            (id, name, 0)
        )
        await db.commit()


async def add_subscriptions():
    parameters = ((key, items[0], items[1]) for key, items in enumerate(subscriptions.items()))
    async with aiosqlite.connect('db/bot.sqlite') as db:
        for key, items in enumerate(subscriptions.items()):
            name, cost = items
            await db.execute(
                'INSERT INTO subscriptions(id, name, cost) VALUES (?, ?, ?)',
                (key, name, cost)
            )
        await db.commit()
