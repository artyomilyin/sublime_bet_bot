import logging
from aiogram import executor

from handlers.handlers import dp
from conf import local

DEBUG = getattr(local, 'LOCAL_DEBUG', False)
logging_level = logging.DEBUG if DEBUG else logging.INFO
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging_level)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
