import logging
import os

from aiogram import executor

from handlers.handlers import dp

DEBUG = os.environ.get('LOCAL_DEBUG', False)
logging_level = logging.DEBUG if DEBUG else logging.INFO
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging_level)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
