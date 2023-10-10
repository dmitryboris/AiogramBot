from data.creating_tables import create_subscription_table, create_order_table, create_user_table


async def global_init(db_file):
    await create_user_table(db_file)
    await create_order_table(db_file)
    await create_subscription_table(db_file)


"""async def main():
    await global_init('../db/bot.sqlite')
asyncio.run(main())"""
