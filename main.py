from aiogram import executor, types
from create_bot import dp

from hendlers import admin, client, other


async def on_startup(_):
    print('Бот включился')


client.register_handlers_client(dp)
other.register_handlers_other(dp)


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)
