from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


click_pay_keyboard=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Click orqali to'lash", callback_data="click_pay")]
    ]
)