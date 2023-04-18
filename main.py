import logging
import os
import asyncio

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from core.utils.commands import set_commands
from core.handlers.register import register_handler

async def main():
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - [%(levelname)s] - %(name)s - '
                        '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()

    await set_commands(bot)
    await register_handler(dp)

    try: 
        await dp.start_polling(bot)
    finally:
        bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())