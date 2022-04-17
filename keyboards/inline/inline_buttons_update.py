from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback_datas import update_callback

update_button = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardButton(
                                                 text="Обновить данные на сайте",
                                                 callback_data=update_callback.new(item_name="site")
                                             )
                                         ]
                                     ])
