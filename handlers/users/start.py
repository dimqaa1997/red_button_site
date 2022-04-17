from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
import requests

from keyboards.inline.callback_datas import update_callback
from keyboards.inline.inline_buttons_update import update_button
from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=update_button)


@dp.callback_query_handler(update_callback.filter(item_name="site"))
async def run_update_site(call: CallbackQuery):
    # await call.answer(text="попали в хендлер")
    await bot.answer_callback_query(callback_query_id=call.id)
    # pprint(call.from_user)
    await bot.send_message(call.from_user.id, text="Запускаю обновление")
    response = requests.get("http://pablicfund.pythonanywhere.com/response_ok")
    if response.ok:
        await bot.send_message(call.from_user.id, text="Обновление завершено")
    else:
        await bot.send_message(call.from_user.id, text="Возникла ошибка!\n\n"
                                                       "Попробуйте еще раз")
