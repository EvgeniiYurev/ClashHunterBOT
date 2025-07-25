LANG_MESSAGES = {
    "ru": {
        "start": "👋 Привет! Добро пожаловать в CashFlow Hunter.\nЗдесь ты найдешь лучшие офферы и сможешь зарабатывать.",
        "no_offers": "❌ Офферы не найдены для твоей страны.",
        "generating": "🧠 Генерирую креатив...",
        "no_creatives": "⚠️ У тебя закончились креативы. Пригласи друзей или оформи подписку.",
    },
    "en": {
        "start": "👋 Welcome to CashFlow Hunter!\nDiscover top offers and start earning today.",
        "no_offers": "❌ No offers found for your country.",
        "generating": "🧠 Generating your creative...",
        "no_creatives": "⚠️ You’ve run out of creative tokens. Invite friends or upgrade.",
    }
}

def get_language_from_locale(locale_code: str):
    if locale_code.startswith("ru"):
        return "ru"
    return "en"

async def get_message(lang: str, key: str):
    return LANG_MESSAGES.get(lang, LANG_MESSAGES["en"]).get(key, key)