from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp
from aiogram import types


class FSMAdmin(StatesGroup):
    name = State()


@dp.message_handler(commands='f', state=None)
async def f_f(message: types.Message):
    pass


