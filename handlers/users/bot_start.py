from aiogram import types
from loader import dp
from filters import  IsPrivate
from utils.misc import rate_limit
from utils.db_api import quick_commands
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from utils.db_api.schemas.menu import MenuItem
from utils.db_api.schemas.cart import CartItem

# Команда для старта
@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), commands=['start'])
async def command_start(message: types.Message):
    try:
        user = await quick_commands.select_user(message.from_user.id)
        if user.status == 'active':
            await message.answer(f'Hi {message.from_user.full_name}\n')
        elif user.status == 'banned':
            await message.answer('You are banned =D')
    except Exception:
        await quick_commands.add_user(user_id=message.from_user.id,
                                      username=message.from_user.username,
                                      status='active')
        await message.answer('Привет')

# Команда для бана
@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), commands=['ban'])
async def get_ban(message: types.Message):
    await quick_commands.update_status('ban')
    await message.answer('You are banned lol')

# Команда для разбанивания
@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), commands=['unban'])
async def get_unban(message: types.Message):
    await quick_commands.update_status('active')
    await message.answer('You are NOT banned')

# # Команда для отображения меню /startmenu
# @rate_limit(limit=3)
# @dp.message_handler(IsPrivate(), commands=['startmenu'])
# async def command_menu(message: types.Message):
#     try:
#         menu_items = await quick_commands.select_menu()
#         if menu_items:
#             menu_text = "Our Menu:\n"
#             buttons = []
#             for item in menu_items:
#                 menu_text += f"\n{item.name} - {item.price}\n{item.description}\n"
#                 buttons.append([InlineKeyboardButton(text=f"Add {item.name} to cart", callback_data=f"add_{item.id}")])
#
#             menu_markup = InlineKeyboardMarkup(inline_keyboard=buttons)
#             await message.answer(menu_text, reply_markup=menu_markup)
#         else:
#             await message.answer('Menu is currently empty.')
#     except Exception as e:
#         await message.answer('An error occurred while fetching the menu.')
#         print(e)
#
# # Обработчик для нажатий на кнопки меню
# @dp.callback_query_handler(lambda call: call.data.startswith('add_'))
# async def add_to_cart_handler(call: types.CallbackQuery):
#     item_id = int(call.data.split('_')[1])
#     menu_item = await quick_commands.select_menu_item(item_id)
#     if menu_item:
#         await quick_commands.add_to_cart(user_id=call.from_user.id, item_id=item_id)
#         await call.answer(f"{menu_item.name} added to cart")
#     else:
#         await call.answer('Item not found.')
#
# # Команда для добавления пункта меню /addmenu
# @rate_limit(limit=3)
# @dp.message_handler(IsPrivate(), commands=['addmenu'])
# async def command_addmenu(message: types.Message):
#     await message.answer("Please provide the menu details in the following format:\n\n"
#                          "Name\nDescription\nPrice\nImage URL\nStatus (true/false)")
#
# # Обработчик для текстовых сообщений, которые следуют за командой /addmenu
# @dp.message_handler(IsPrivate(), content_types=types.ContentTypes.TEXT)
# async def addmenu_handler(message: types.Message):
#     if message.text.startswith('/addmenu '):
#         try:
#             parts = message.text.split('|')
#             if len(parts) != 6:
#                 await message.answer('Usage: /addmenu <name>|<description>|<price>|<image_url>|<status>')
#                 return
#
#             name, description, price, image, status = parts[1].strip(), parts[2].strip(), parts[3].strip(), parts[4].strip(), parts[5].strip()
#             status = status.lower() == 'true'
#
#             await quick_commands.add_menu_item(name=name, description=description, price=price, image=image, status=status)
#             await message.answer('Menu item added successfully.')
#         except Exception as e:
#             await message.answer('An error occurred while adding the menu item.')
#             print(e)
#     else:
#         await message.answer('Invalid format. Please provide details in the following format:\n\n'
#                              'Name\nDescription\nPrice\nImage URL\nStatus (true/false)')
#
# # Команда для удаления пункта меню /deletemenu
# @rate_limit(limit=3)
# @dp.message_handler(IsPrivate(), commands=['deletemenu'])
# async def command_deletemenu(message: types.Message):
#     try:
#         parts = message.text.split()
#         if len(parts) != 2:
#             await message.answer('Usage: /deletemenu <item_id>')
#             return
#
#         item_id = int(parts[1])
#         await quick_commands.delete_menu_item(item_id)
#         await message.answer('Menu item deleted successfully.')
#     except Exception as e:
#         await message.answer('An error occurred while deleting the menu item.')
#         print(e)