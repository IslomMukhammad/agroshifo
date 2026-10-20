import ssl
import base64
import certifi
import aiohttp
from config import GEMINI_API_KEY

AI_MODELS = [
    "gemini-3.8-flash",
    # "gemini-3.1-pro-preview",
    "gemini-3.5-flash-lite"
]

AGRO_PROMPT = """
Sen tajribali agronom va o'simliklar shifokori (fitopatolog) san.
Foydalanuvchi yuborgan rasmni diqqat bilan tahlil qil va O'ZBEK TILIDA quyidagi tuzilishda aniq, to'liq va batafsil javob ber:

Agar rasmda o'simlik, daraxt, barg, meva yoki ekin bo'lmasa:
Faqatgina "⚠️ Kechirasiz, bu rasmda o'simlik aniqlanmadi. Iltimos, kasallangan o'simlik yoki barg rasmini aniqroq qilib yuboring." deb javob qaytar.

Agar rasmda o'simlik bo'lsa, quyidagi bandlarni to'ldirib yoz (HTML teglaridan faqat <b> va <i> ishlat, Markdown ** yoki # belgilarini UMUMAN ishlatma):

🌱 <b>O'simlik nomi:</b> (O'simlik turini yoz)
🔍 <b>Tashxis (Kasallik yoki zararkunanda):</b> (Kasallik nomi, uning kelib chiqish sababi va rasmda ko'rinib turgan belgilari)

💊 <b>Dori vositalari bilan davolash (Kimyoviy usul):</b>
• Qaysi fungitsid, insektitsid yoki dori vositalarini ishlatish kerakligi (aniq dori nomlari, masalan: Fundazol, Skore va ularni necha litr suvga qancha miqdorda qo'shib sepish me'yorlari).

🌿 <b>Milliy va tabiiy usulda yechim (Xalqona usul):</b>
• Kimyoviy dorilarsiz, uy sharoitida qo'llaniladigan xalqona usullar (masalan: kul, sarimsoqpiyoz damlamasi, kir sovun eritmasi yoki boshqa tabiiy vositalar bilan davolash va agrotexnik choralar).

🛡 <b>Oldini olish (Profilaktika):</b>
• Kelajakda bu kasallik qaytarilmasligi uchun nimalarga e'tibor berish kerakligi.
"""

async def fetch_ai_diagnosis(image_bytes: bytes)-> str:
    ssl_context=ssl.create_default_context(cafile=certifi.where())

    handlers={
        "Content-Type":"aplication/json",
        "x-goog-api-key":GEMINI_API_KEY
    }

    base64_image=base64.b64encode(image_bytes).decode("utf-8")

    payload={
        "contents":[
            {
                "parts":[
                    {"text":AGRO_PROMPT},
                    {
                        "inline_data":{
                            "mime_type":"image/jpeg",
                            "data":base64_image        
                        }
                    }
                ]
            }
        ],
        "generationConfig":{
            "temperature":0.4,
            "maxOutputTokens":1500
        }
    }
    timeout=aiohttp.ClientTimeout(total=90)
    last_error=None
    async with aiohttp.ClientSession(timeout=timeout) as session:
        for model_name in AI_MODELS:
            url=f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent"

            try:
                async with session.post(url, headers=handlers,json=payload, ssl=ssl_context) as resp:
                    data=await resp.json()
                    if resp.status==200 and "candidates" in data:
                        text=data["candidates"][0]["content"]["parts"][0]["text"]
                        print(f"{model_name} javob berdi")
                        return text
                    else:
                        error=data.get("error",{}).get("message","nomalum xato")
                        print(f"⚠️ {model_name} xato qaytardi ({resp.status}): {error}")
                        last_error=error
            except Exception as e:
                print(f"⚠️ {model_name} ulanish xatosi: {e}")
                last_error = e
                continue

    raise Exception(f"Barcha AI modellar band: {last_error}")