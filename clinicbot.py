import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = "7660014302:AAGFiB5RliA-JgzEcBk4NGJ9UU9_YQ6DOuA"  # BotFather bergan tokenni shu joyga yoz

# Logging
logging.basicConfig(level=logging.INFO)

# Bot va dispatcher
bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

# Asosiy menyu tugmalari
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(
    KeyboardButton("📝 Ro'yxatdan o'tish"),
    KeyboardButton("👨‍⚕️ Doktor bilan bog'lanish"),
    KeyboardButton("⏰ Ish vaqti")
)


# /start komandasi
@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.answer(
        "🏥 <b>KlinikBot</b> ga xush kelibsiz!\n\n"
        "Quyidagi menyudan tanlang:",
        reply_markup=main_menu
    )


# /help komandasi
@dp.message_handler(commands=["help"])
async def send_help(message: types.Message):
    await message.answer(
        "ℹ️ Men yordamchi KlinikBotman.\n"
        "Buyruqlar:\n"
        "/start - botni qayta ishga tushirish\n"
        "/help - yordam olish"
    )


# Tugmalar uchun javoblar
@dp.message_handler(lambda m: m.text == "📝 Ro'yxatdan o'tish")
async def register(message: types.Message):
    await message.answer("Iltimos, ismingizni yuboring:")
    # Bu yerda keyinchalik foydalanuvchini bazaga yozsa bo‘ladi


@dp.message_handler(lambda m: m.text == "👨‍⚕️ Doktor bilan bog'lanish")
async def doctor(message: types.Message):
    await message.answer("Doktor bilan bog‘lanish uchun: +998 90 123 45 67 ☎️")


@dp.message_handler(lambda m: m.text == "⏰ Ish vaqti")
async def working_hours(message: types.Message):
    await message.answer("Bizning ish vaqti: Dushanba - Shanba, 9:00 - 18:00 🕘")


# Default javob
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("❌ Men sizni tushunmadim. Iltimos, menyudan foydalaning.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
