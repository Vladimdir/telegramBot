from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import text
from keyboards import client_kd
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext

from create_bot import dp, bot, Dispatcher


# @dp.message_handler(commands=['start'])
async def info(message: types.Message) -> None:
    await message.answer_photo(photo=open('img/dom.jpg', 'rb'), caption=f'Hello, {message.from_user.first_name}!',
                               reply_markup=client_kd.start_menu)


# @dp.callback_query_handler(text='create_account')
async def registration(call: types.CallbackQuery, state) -> None:
    msg = await call.message.answer_photo(photo=open('img/dom.jpg', 'rb'), caption='<b>ЗАРЕЄСТРУВАТИСЯ</b> ↘️:',
                                    reply_markup=client_kd.btn_reg2, parse_mode='HTML')
    async with state.proxy() as data:
        data['message_id'] = msg.message_id
    await call.message.delete()


# @dp.message_handler(content_types=['contact']) # message.contact.phone_number[-10:]
async def reg_phone(message: types.Message, state) -> None:
    if message.contact is not None:
        print("Номер телефона")
    await message.delete()
    async with state.proxy() as data:
        message_id = data['message_id']
    await bot.delete_message(message.from_user.id, message_id)
    await message.answer_photo(photo=open('img/dom.jpg', 'rb'), caption=f"<b>ОСОБИСТИЙ КАБІНЕТ</b>\n\nОсобовий рахунок"
                                                                        f": {260418}\n\nДо сплати: {4502.36}грн",
                                    reply_markup=client_kd.account, parse_mode='HTML')


# @dp.callback_query_handler(text='kod_register')
async def kod_register(call: types.CallbackQuery) -> None:
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Назад', callback_data='start'))
    await call.message.answer('<b>Введіть код реєстрації</b> 🔑️:', reply_markup=markup, parse_mode='HTML')
    await call.message.delete()


# @dp.callback_query_handler(text='Зареєструватися по номеру телефона')
async def start(call: types.CallbackQuery) -> None:
    pass


# @dp.callback_query_handler(text='submit_meter')
async def meters(call: types.CallbackQuery, state) -> None:
    await call.message.answer_photo(photo=open('img/dom.jpg', 'rb'), caption='<b>Виберіть прилад обліку</b> ↘️:',
                                    reply_markup=client_kd.meter, parse_mode='HTML')
    await call.message.delete()


# @dp.callback_query_handler(text='water')
async def water(call: types.CallbackQuery, state) -> None:

    await call.message.answer_photo(photo=open('img/meterWater.jpg', 'rb'), caption='<b>Введіть показники лічильника ХОЛОДНОЇ ВОДИ (ціле число)</b> ↘️:',
                                    reply_markup=client_kd.back_meters, parse_mode='HTML')
    await call.message.delete()                            
    

async def meters_water(message: types.Message):
    await message.answer('Показники прийняті.')


def register_handlers_client(disp: Dispatcher):
    disp.register_message_handler(info, commands=['start'])
    disp.register_callback_query_handler(registration, text='create_account')
    disp.register_callback_query_handler(kod_register, text='kod_register')
    disp.register_message_handler(reg_phone, content_types=['contact'])
    disp.register_callback_query_handler(meters, text='submit_meter')
    disp.register_callback_query_handler(water, text='water')
    disp.register_message_handler(meters_water)







