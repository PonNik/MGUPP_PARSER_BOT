from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButtonPollType


def every_msg_kb():
    kb = [
        [InlineKeyboardButton(text = 'lol', callback_data="lol")]
    ]
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=kb
    )
    return keyboard