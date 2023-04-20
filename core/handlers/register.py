from aiogram import Dispatcher, filters
from aiogram.filters import Command

from core.handlers.basic import start_command, help_command, change_day, load_schedule

DAYS_WEEK = [
        'Понедельник',
        'Вторник', 
        'Среда',  
        'Четверг', 
        'Пятница', 
        'Суббота',
    ]

async def register_handler(dp: Dispatcher):
    dp.message.register(start_command, Command(commands=['start']))
    dp.message.register(help_command, Command(commands=['help']))
    dp.message.register(change_day, filters.Text(text=DAYS_WEEK, ignore_case=True))
    dp.message.register(load_schedule, filters.Text(text='Посмотреть рассписание', ignore_case=True))
    dp.message.register(load_schedule, filters.Text(text='Обновить расписание', ignore_case=True))