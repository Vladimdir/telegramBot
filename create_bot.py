from aiogram import Bot, Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

storage = MemoryStorage()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot, storage=storage)

