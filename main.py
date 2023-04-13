import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from p import parce

logging.basicConfig(level=logging.INFO)

load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

data = []

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    global data
    kb = [
        [types.InlineKeyboardButton(text="Понедельник"), types.InlineKeyboardButton(text="Вторник")],
        [types.InlineKeyboardButton(text="Среда"), types.InlineKeyboardButton(text="Четверг")],
        [types.InlineKeyboardButton(text="Пятница"), types.InlineKeyboardButton(text="Суббота")]
    ]
    await message.reply('Ща бля, Заебал')
    if data == []:
        data = await parce()

    await message.reply('Э, какой день интересует?', reply_markup=types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="День выбирай: "
    ))

@dp.message_handler()
async def echo(message: types.Message):
    itog = ''
    for i in data:
        if message.text == i['day']:
            for textmessage in i['lessons']:
                itog += textmessage
    await message.answer(itog, reply_markup=types.ReplyKeyboardRemove())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)