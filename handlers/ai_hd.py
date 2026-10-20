from aiogram import Router, types,F
from components.texts import AI_TEXT
from database.users_db import get_user_ai_int
from logic.ai_logic import procces_plant_image
router = Router()

@router.message(F.photo)
async def plant_analize(message:types.Message):
    user_id=message.from_user.id
    ai_limit=get_user_ai_int(user_id)
    if ai_limit<=0:
        await message.answer(
            "⚠️ <b>Sizning bugungi AI limitingiz tugagan!</b>\n\n"
            "🔄 Ertaga yana <b>1 ta bepul limit</b> beriladi.\n"
            )
        return

    wait_txt = await message.answer(
        "🔬 <b>Rasm AI orqali tahlil qilinmoqda...</b>\n"
        "⏳ <i>Iltimos, 1-2 daqiqa kuting...</i>"
    )

    try:
        _,final_text=await procces_plant_image(message, user_id, ai_limit)

        try:
            await wait_txt.edit_text(final_text,)

        except Exception:
            await wait_txt.edit_text(final_text, parse_mode=None,)

    except Exception as e:
        print(f"❌ Umumiy AI Xatolik: {e}")
        await wait_txt.edit_text(
            "❌ <b>Rasmni tahlil qilishda xatolik yuz berdi.</b>\n"
            "Iltimos, birozdan so'ng qayta urinib ko'ring (limitingiz saqlanib qoldi).",
        )