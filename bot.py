import asyncio
from aiogram import Bot, Dispatcher, types
from config import TOKEN
from handlers import ai_hd,chat_hd, privacy_hd, pro_hd, start_hd
from  logic.sub_middleware import CheckSubMiddleware
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from admin import admin_hd
bot=Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp=Dispatcher()



async def main():
    dp.include_router(admin_hd.router)
    await bot.delete_webhook(drop_pending_updates=True)
    dp.message.middleware(CheckSubMiddleware())
    dp.callback_query.middleware(CheckSubMiddleware())
    dp.include_router(start_hd.router)
    dp.include_router(ai_hd.router)
    dp.include_router(pro_hd.router)
    dp.include_router(privacy_hd.router)
    dp.include_router(chat_hd.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())