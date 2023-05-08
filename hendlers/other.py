from aiogram import types
from create_bot import dp, Dispatcher


# @dp.message_handler()
async def no_such_command(message: types.Message):
    await message.answer('Такої команди не існує.')
    await message.delete()


def register_handlers_other(disp: Dispatcher):
    disp.register_message_handler(no_such_command)
