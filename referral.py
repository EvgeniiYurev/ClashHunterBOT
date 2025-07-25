import aiosqlite
from db import DB_PATH

async def handle_referral(new_user_id: int, referrer_id: int):
    if new_user_id == referrer_id:
        return  # self-ref not allowed

    async with aiosqlite.connect(DB_PATH) as db:
        # check if already referred
        cursor = await db.execute("SELECT referred_by FROM users WHERE user_id = ?", (new_user_id,))
        row = await cursor.fetchone()
        if row and row[0]:
            return

        # update referral
        await db.execute("UPDATE users SET referred_by = ? WHERE user_id = ?", (referrer_id, new_user_id))
        await db.execute("UPDATE users SET referrals = referrals + 1, creative_limit = creative_limit + 1 WHERE user_id = ?", (referrer_id,))
        await db.execute("UPDATE users SET creative_limit = creative_limit + 1 WHERE user_id = ?", (new_user_id,))
        await db.commit()

async def get_referral_stats(user_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT referrals FROM users WHERE user_id = ?", (user_id,))
        row = await cursor.fetchone()
        return row[0] if row else 0