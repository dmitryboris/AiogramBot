import aiosqlite


async def get_user(id: int):
    async with aiosqlite.connect('db/bot.sqlite') as db:
        async with db.execute('SELECT * FROM users WHERE id = ?', (id,)) as cursor:
            async for user in cursor:
                return user


async def get_subscriptions():
    subs = {}
    async with aiosqlite.connect('db/bot.sqlite') as db:
        async with db.execute('SELECT name, cost FROM subscriptions') as cursor:
            async for name, cost in cursor:
                subs[name] = cost
    return subs


async def get_subscriptions_by_own(own: str):
    subs = {}
    async with aiosqlite.connect('db/bot.sqlite') as db:
        async with db.execute('SELECT name, cost FROM subscriptions WHERE own = ?', (own, )) as cursor:
            async for name, cost in cursor:
                subs[name] = cost
    return subs
