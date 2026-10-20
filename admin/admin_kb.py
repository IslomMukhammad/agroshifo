from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_keyboard=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📊 Statistika", callback_data="statistika")],
    [InlineKeyboardButton(text="📢 Xabar tarqatish", callback_data="ads")],
])

cancel_keyboard=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="❌ Bekor qilish", callback_data="cancel")]
    ]
)

