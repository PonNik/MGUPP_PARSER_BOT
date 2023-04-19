from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButtonPollType


def make_kb_week(data):
    kb = []
    for day in data:
        name_day = day['day']
        kb.append([InlineKeyboardButton(text=name_day)])
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите день: "
    )
    return keyboard