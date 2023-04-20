from aiogram import Bot
from aiogram.types import Message

from core.requests_parse import parse
from core.keyboards.reply import make_kb_week, start_kb
#from core.keyboards.inline import every_msg_kb # inline keyboard on all messages
from core.utils.parse_json import parse_Lessons

data = ''

async def start_command(message: Message , bot: Bot):
    await message.answer('Категорически приветствую', reply_markup=start_kb())
    
    
async def help_command(message: Message, bot: Bot):
    await message.answer('Опа, кто-то не разобрался?\nОкей, данный бот, прямо сейчас, умеет только показывать актуальное рассписание\nЧье? Конечно мое!')

async def load_schedule(message: Message , bot: Bot):
    global data
    try:
        await message.reply('Ожидайте...')
        data = parse()
        keyboard = make_kb_week(data)
        await message.answer('Готово, какой день?', reply_markup=keyboard)
    except:
        await message.answer('Технические шоколадки')
    
async def change_day(message: Message, bot: Bot):
    for day in data:
        if day['day'].lower() == message.text.lower():
            msgs = await parse_Lessons(day['data_lessons'])
            for msg in msgs: 
                await message.answer(msg) # add keyboard reply_markup=every_msg_kb