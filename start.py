from aiogram import types, Dispatcher

async def cmd_start(message: types.Message):
    await message.answer(
        "Добро пожаловать в CashFlow Hunter 💸\n\n"
        "Ты можешь зарабатывать на офферах прямо из Telegram.\n"
        "👉 Используй /offers чтобы начать."
    )

def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])