from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Message', callback_data='Message'),
                                        InlineKeyboardButton(text='link', url='https://youtube.com')
                                    ]
                                ])