from aiogram import Bot
from aiogram.types import Message

from core.requests_parse import parse

async def start_command(message: Message , bot: Bot):
    try:
        await message.reply('Ща бля, Заебал')
        data = parse()
        print (data[4]['day'])
        names = ''
        for f in data[4]['data_lessons']:
            names += f['name']
            names += '\n'
        await message.answer(names)
    except:
        await message.reply('Технические шоколадки, еблан иди проспись')