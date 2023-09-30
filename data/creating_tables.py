import aiosqlite


async def create_user_table(db_file: str):
    conn_str = f'sqlite:///{db_file}'
    async with aiosqlite.connect(db_file) as db:
        await db.execute('CREATE TABLE IF NOT EXISTS users'
                         '(id INTEGER PRIMARY KEY,'
                         ' name TEXT,'
                         ' count_of_orders INTEGER)')
        await db.commit()


async def create_order_table(db_file: str):
    async with aiosqlite.connect(db_file) as db:
        await db.execute('CREATE TABLE IF NOT EXISTS orders'
                         '(id INTEGER PRIMARY KEY)')
        await db.commit()


async def create_subscription_table(db_file: str):
    async with aiosqlite.connect(db_file) as db:
        await db.execute('CREATE TABLE IF NOT EXISTS subscriptions'
                         '(id INTEGER PRIMARY KEY,'
                         ' name TEXT)')
        await db.commit()
