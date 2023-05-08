from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import text
from keyboards import client_kd

from create_bot import dp, bot, Dispatcher


# @dp.message_handler(commands=['start'])
async def info(message: types.Message):
    await message.answer_photo(photo=open('img/dom.jpg', 'rb'), caption=f'Hello, {message.from_user.first_name}!', reply_markup=client_kd.start_menu)


# @dp.callback_query_handler(text='create_account')
async def registration(call: types.CallbackQuery) -> None:
    await call.message.answer_photo(photo=open('img/dom.jpg', 'rb'), caption='<b>ЗАРЕЄСТРУВАТИСЯ</b> ↘️:',
                                    reply_markup=client_kd.btn_reg2, parse_mode='HTML')
    await call.message.delete()


# @dp.callback_query_handler(text='kod_register')
async def kod_register(call: types.CallbackQuery) -> None:
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Назад', callback_data='start'))
    await call.message.answer('<b>Введіть код реєстрації</b> 🔑️:', reply_markup=markup, parse_mode='HTML')
    await call.message.delete()


# @dp.callback_query_handler(text='Зареєструватися по номеру телефона')
async def start(call: types.CallbackQuery) -> None:
    pass


def register_handlers_client(disp: Dispatcher):
    disp.register_message_handler(info, commands=['start'])
    disp.register_callback_query_handler(registration, text='create_account')
    disp.register_callback_query_handler(kod_register, text='kod_register')
    # disp.register_callback_query_handler(start, text='start')






