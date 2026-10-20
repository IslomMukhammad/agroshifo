from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from config import CHANNEL_ID
from keyboards.subscibe_kb import subs_buttons


class CheckSubMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        if isinstance(event, CallbackQuery) and event.data=="check_sub":
            return await handler(event, data)

        bot=data["bot"]

        user_id=event.from_user.id
        member= await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)

        if member.status in ["member", "administrator","creator"]:
            return await handler(event, data)

        else:
            if isinstance(event, Message):
                await event.answer("Botdan foydalanish uchun quyidagi kanalimizga obuna bo'ling:", reply_markup=subs_buttons)

            elif isinstance(event, CallbackQuery):
                await event.answer("Siz kanaldan chiqib ketgansiz! Avval obuna bo'ling.", show_alert=True)

            return 
