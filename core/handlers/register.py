from aiogram import Dispatcher
from aiogram.filters import Command

from core.handlers.basic import start_command, change_day

async def register_handler(dp: Dispatcher):
    dp.message.register(start_command, Command(commands=['start']))
    dp.message.register(change_day)