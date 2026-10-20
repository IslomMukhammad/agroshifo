from aiogram import Router,types, F
from components.texts import PRIVACY_TEXT
router=Router()

@router.message(F.text=="Foydalanish siyosati 📑")
async def privacy_hand(message: types.Message):
    await message.answer(PRIVACY_TEXT,)