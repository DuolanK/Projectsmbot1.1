import asyncio
from data import config
from utils.db_api import quick_commands
from utils.db_api.db_gino import db


#async def db_test():
    #await db.set_bind(config.POSTGRES_URI)
    #await db.gino.drop_all()
    #await db.gino.create_all()

    #await quick_commands.add_user(1, 'Duo', 'Duo5')
    #await quick_commands.add_user(123, 'Dddd', 'Duo4')
   # await quick_commands.add_user(1321, 'bot', 'Duo3')
    #await quick_commands.add_user(9, 'telegram', 'Duo2')
    #await quick_commands.add_user(3, 'Duo', 'Duo1')


    #users = await quick_commands.select_all_users()
    #print(users)

    #count = await quick_commands.count_users()
    #print(count)

    #user = await quick_commands.select_user()
    #print(user)

    #await quick_commands.update_user_name(1, 'DuoDuo')
    #print(user)

#loop = asyncio.get_event_loop()
#loop.run_until_complete(db_test())