from aiogram import types, Dispatcher

async def cmd_creative(message: types.Message):
    await message.answer(
        "Скоро здесь появится генерация AI-креативов ✨"
    )

def register_creative_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_creative, commands=["creative"])