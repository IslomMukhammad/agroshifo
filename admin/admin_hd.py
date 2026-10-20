import asyncio
from aiogram import Router,types,F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from config import ADMIN_ID
from admin.admin_kb import admin_keyboard,cancel_keyboard
from database.users_db import get_all_users,get_users_count,get_pro_users_count

router=Router()

class AdminState(StatesGroup):
    waiting_for_broadcast=State()
    waiting_for_card=State()
    waiting_for_price=State()

@router.message(Command("admin"), F.from_user.id.in_(ADMIN_ID))
async def admin_panel(message: types.Message, state: FSMContext):
    await state.clear()
    
    text = (
        "👨‍💻 <b>Admin panelga xush kelibsiz!</b>\n\n"
    )
    await message.answer(text=text, reply_markup=admin_keyboard)

@router.callback_query(F.data=="cancel", F.from_user.id.in_(ADMIN_ID))
async def cancel_button(callback: types.CallbackQuery, state:FSMContext):
    await state.clear()
    text = (
        "👨‍💻 <b>Admin panelga xush kelibsiz!</b>\n\n"
        "Kerakli bo'limni tanlang:"
    )
    await callback.message.edit_text(text, reply_markup=admin_keyboard)
    await callback.answer("Amal bekor qilindi")

@router.callback_query(F.data=="statistika", F.from_user.id.in_(ADMIN_ID))
async def static_handle(callback: types.CallbackQuery):
    total=get_users_count()
    pro=get_pro_users_count()

    text = (
        "📊 <b>Bot statistikasi:</b>\n\n"
        f"👥 <b>Jami obunachilar:</b> {total} ta\n"
        f"💎 <b>PRO obunachilar:</b> {pro} ta"
    )
    await callback.message.edit_text(text, reply_markup=admin_keyboard)
    await callback.answer()


@router.callback_query(F.data=="ads", F.from_user.id.in_(ADMIN_ID))
async def ask_ads(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(AdminState.waiting_for_broadcast)
    await callback.message.edit_text("📢 Tarqatilishi kerak bo'lgan xabarni yuboring:", reply_markup=cancel_keyboard)
    await callback.answer()

@router.message(AdminState.waiting_for_broadcast, F.from_user.id.in_(ADMIN_ID))
async def send_ads(message: types.Message, state: FSMContext):
    await state.clear()
    users=get_all_users()
    sent_count=0
    block_count=0
    status_send=await message.answer("⏳ Reklama tarqatilmoqda, iltimos kuting...")

    for user_id in users:
        try:
            await message.copy_to(chat_id=user_id)
            sent_count+=1
            await asyncio.sleep(0.05)
        except Exception:
            block_count+=1

    await status_send.edit_text(
        f"✅ <b>Reklama tarqatish yakunlandi!</b>\n\n"
        f"📬 Yetib bordi: <b>{sent_count} ta</b>\n"
        f"🚫 Bloklagan/O'chirilgan: <b>{block_count} ta</b>",
        reply_markup=admin_keyboard
    )