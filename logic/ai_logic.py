import io
from aiogram import types
from database.users_db import get_user_ai_int, change_ai_int
from api.ai_api import fetch_ai_diagnosis

def check_user_limit(user_id: int)->int:
    return get_user_ai_int(user_id)

async def procces_plant_image(message:types.Message, user_id:int,current_limit:int)->tuple[bool,str]:
    photo=message.photo[-1]
    image_stream=io.BytesIO()
    await message.bot.download(photo,destination=image_stream)
    image_bytes=image_stream.getvalue()
    result_txt=await fetch_ai_diagnosis(image_bytes)

    if "o'simlik aniqlanmadi" in result_txt.lower():
        return False, result_txt

    change_ai_int(user_id,-1)

    remaining_limit=current_limit-1
    final_text=(
        f"{result_txt}\n\n"

        f"AI xato qilishi mumkin!"
    )
    return True, final_text