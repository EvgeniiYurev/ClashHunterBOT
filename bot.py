import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

from handlers import start, creative, offers

start.register_handlers(dp)
creative.register_handlers(dp)
offers.register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
