import aiosqlite
import asyncio
from db import DB_PATH

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            language TEXT,
            referred_by INTEGER,
            referrals INTEGER DEFAULT 0,
            creative_limit INTEGER DEFAULT 0
        )
        """)
        await db.commit()

asyncio.run(init_db())
