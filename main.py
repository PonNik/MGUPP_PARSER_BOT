import logging
import os
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from dotenv import load_dotenv
from parce import parce

from core.handlers.basic import start_command
from core.utils.commands import set_commands

async def main():
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - [%(levelname)s] - %(name)s - '
                        '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()

    await set_commands(bot)

    dp.message.register(start_command, Command(commands=['start']))

    try: 
        await dp.start_polling(bot)
    finally:
        bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())