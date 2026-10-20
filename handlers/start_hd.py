from aiogram import Router,types, F
from config import CHANNEL_ID
from keyboards.subscibe_kb import subs_buttons
from components.texts import MAIN_TEXT
from keyboards.main_kb import main_buttons
from aiogram.filters import Command

from database.users_db import add_user


router=Router()

@router.message(Command("start"))
async def main_message(message: types.Message, user_id: int=None):
    uid = user_id or message.from_user.id

    member=await message.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=uid)

    if member.status in ["member", "administrator", "creator"]:
        await message.answer(MAIN_TEXT, reply_markup=main_buttons)
        add_user(uid)
    else:
        await message.answer(f"Botdan foydalanish uchun quyidagi kanalimizga obuna bo'ling:", reply_markup=subs_buttons)


@router.callback_query(F.data=="check_sub")
async def check_subscription(callback:types.CallbackQuery):
    user_id=callback.from_user.id
    member=await callback.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=callback.from_user.id)
    if member.status in ["member","administrator", "creator"]:
        
        add_user(user_id)
        
        await callback.message.delete()
        await callback.message.answer(MAIN_TEXT, reply_markup=main_buttons)
    else:
        await callback.answer("Siz kanalga azo bo'lmagansiz", show_alert=True)
