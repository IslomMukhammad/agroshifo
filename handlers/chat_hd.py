from aiogram import Router, types, F

router =Router()

@router.message(F.text=="Qo'llab-quvvatlash 💬")
async def help_handle(message: types.Message):
    await message.answer("Admin bilan bog'lanish: ",)