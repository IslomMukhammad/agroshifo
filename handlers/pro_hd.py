from aiogram import Router,types,F
from components.texts import PRO_TEXT

router=Router()

@router.message(F.text=="AgroShifo Pro 🌟")
async def pro_handle(message:types.Message):
    await message.answer(text=PRO_TEXT,)