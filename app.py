async def on_startup(dp):

    import filters
    filters.setup(dp)
    import middlewares
    middlewares.setup(dp)


    from loader import db
    from utils.db_api.db_gino import on_startup
    print('connection to PostgreSQL')
    await on_startup(dp)


    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    print("delete db")
    await db.gino.drop_all()

    print('creating db')
    await db.gino.create_all()
    print('ready')

    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)

    print('bot initiated')

if __name__== '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)