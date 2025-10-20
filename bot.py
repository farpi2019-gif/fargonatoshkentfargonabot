import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

BOT_TOKEN = "7945144503:AAEr5CWHcIcuDsQBuUmnE8o3ePR3jMRdrHI"  # shu joyga o'z tokeningizni yozing

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()

# /start komandasi
@router.message(Command("start"))
async def start_command(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Farg‘ona"), KeyboardButton("Toshkent"))
    await message.answer("Qayerga borasiz?", reply_markup=markup)

# Farg‘ona yoki Toshkent tanlansa
@router.message(lambda message: message.text in ["Farg‘ona", "Toshkent"])
async def choose_city(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Kontaktni yuborish 📞", request_contact=True))
    await message.answer("Iltimos, telefon raqamingizni yuboring:", reply_markup=markup)

# Kontakt yuborilganda
@router.message(lambda message: message.contact is not None)
async def get_contact(message: types.Message):
    contact = message.contact.phone_number
    await message.answer(f"Raqamingiz qabul qilindi: {contact}")

# Botni ishga tushirish
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())