import aiosqlite

subscriptions = {
    "Essential": [100, "PS"],
    "Extra": [200, "PS"],
    "Deluxe": [300, "PS"],
    "EA Play Plus": [100, "EA"],
    "EA Play Pro": [400, "EA"],
    "PC": [100, "XBOX"],
    "Console": [200, "XBOX"],
    "Ultimate": [400, "XBOX"]
}


async def add_user(id: int, name: str):
    async with aiosqlite.connect('db/bot.sqlite') as db:
        await db.execute(
            'INSERT INTO users(id, name, count_of_orders) VALUES (?, ?, ?)',
            (id, name, 0)
        )
        await db.commit()


async def add_subscriptions():
    async with aiosqlite.connect('db/bot.sqlite') as db:
        for key, items in enumerate(subscriptions.items()):
            name, values = items
            cost, own = values
            await db.execute(
                'INSERT INTO subscriptions(id, name, cost, own) VALUES (?, ?, ?, ?)',
                (key, name, cost, own)
            )
        await db.commit()
