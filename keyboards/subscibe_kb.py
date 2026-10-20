from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CHANNEL_URL

subs_buttons=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Kanalga o'tish 📢", url=CHANNEL_URL)],
    [InlineKeyboardButton(text="Tekshirish ✅", callback_data="check_sub")]
])