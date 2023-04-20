from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButtonPollType


def make_kb_week(data):
    kb = []
    for day in data:
        name_day = day['day']
        kb.append([InlineKeyboardButton(text=name_day)])
    kb.append([InlineKeyboardButton(text="Обновить расписание")])
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите день: "
    )
    return keyboard

def start_kb():
    kb = [
        [InlineKeyboardButton(text='Регистрация(не работает)')],
        [InlineKeyboardButton(text='Посмотреть рассписание')],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    return keyboard