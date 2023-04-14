import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from parce import parce_site

logging.basicConfig(level=logging.INFO)

data = []

async def send_welcome(message: types.Message):
    global data
    kb = [
        [types.InlineKeyboardButton(text="Понедельник"), types.InlineKeyboardButton(text="Вторник")],
        [types.InlineKeyboardButton(text="Среда"), types.InlineKeyboardButton(text="Четверг")],
        [types.InlineKeyboardButton(text="Пятница"), types.InlineKeyboardButton(text="Суббота")]
    ]
    try:
        await message.reply('Ща бля, Заебал')
        if data == []:
            data = await parce_site()
        await message.reply('Э, какой день интересует?', reply_markup=types.ReplyKeyboardMarkup(
            keyboard=kb,
            resize_keyboard=True,
            one_time_keyboard=True,
            input_field_placeholder="День выбирай: "
        ))
    except:
        await message.reply('Технические шоколадки, еблан иди проспись')

async def echo(message: types.Message):
    itog = ''
    for i in data:
        if message.text == i['day']:
            for textmessage in i['lessons']:
                if '2  П.Гр.' in textmessage:
                    itog += textmessage
                elif '1  П.Гр.' not in  textmessage:
                    itog += textmessage
    await message.answer(itog)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=["start"])
    dp.register_message_handler(echo, lambda message: message.text)

if __name__ == '__main__':
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher(bot)

    register_handlers(dp)
    
    executor.start_polling(dp, skip_updates=True)