import aiosqlite
from data.get_info import get_subscriptions
from data.add_info import add_subscriptions


async def create_user_table(db_file: str):
    conn_str = f'sqlite:///{db_file}'
    async with aiosqlite.connect(db_file) as db:
        await db.execute('CREATE TABLE IF NOT EXISTS users'
                         '(id INTEGER PRIMARY KEY,'
                         ' name TEXT NOT NULL,'
                         ' count_of_orders INTEGER)')
        await db.commit()


async def create_order_table(db_file: str):
    async with aiosqlite.connect(db_file) as db:
        await db.execute('CREATE TABLE IF NOT EXISTS orders'
                         '(id INTEGER PRIMARY KEY AUTOINCREMENT,'
                         'user_id INTEGER,'
                         'sub_id INTEGER,'
                         'FOREIGN KEY (user_id) REFERENCES users (id),'
                         'FOREIGN KEY (sub_id) REFERENCES subscriptions (id))')
        await db.commit()


async def create_subscription_table(db_file: str):
    async with aiosqlite.connect(db_file) as db:
        await db.execute('CREATE TABLE IF NOT EXISTS subscriptions'
                         '(id INTEGER PRIMARY KEY AUTOINCREMENT,'
                         'name TEXT NOT NULL,'
                         'cost INTEGER,'
                         'own TEXT NOT NULL)')
        await db.commit()
    subs = await get_subscriptions()
    if len(subs.keys()) == 0:
        await add_subscriptions()

