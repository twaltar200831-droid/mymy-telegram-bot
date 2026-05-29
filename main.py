from datetime import datetime, timezone, timedelta
import asyncio
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

# BOT INFO
BOT_TOKEN = "8940580343:AAGUVHxKNKCg7QNALlDp-b1l-bohevhl8Mc"
CHANNEL_ID = "@thihanaing573"

# မြန်မာအချိန် (UTC+6:30)
MYANMAR_TZ = timezone(timedelta(hours=6, minutes=30))

def get_myanmar_time():
    return datetime.now(MYANMAR_TZ)

# POSTS CONTENT
SCHEDULED_POSTS = {
    "09:00": "Tik tok Boosting service💝\n\n24နာရီအတွင်း order all done\n\nLike တွေပြန်မကျတဲ့ဈေးနှုန်းလေး\n\nLike 100._600ks\nLike 300 - 1700 ks\nLike 500 - 2500 ks\nLike 1k - 3500 ks\nLike 2k - 7000 ks\nLike 4k - 13000 ks\nLike 5k - 15500ks\n\n#Daezy",
    "12:00": "Telegram channel sub တသက်သာပြန်မကျ ဈေးနှုန်း\n\nSub -100 -2000ks\nSub -200 -3800ks\nSub -500 -8500ks\n\nဝယ်ယူရန် @thiha3124\n\n#Daezy",
    "15:00": "Instagram Like & Follower Service 😘\n\nInstagram like 1k - 3500\nInstagram follower 1k - 12500ks\n\nဝယ်ယူရန် - @thiha3124\n\n#Daezy",
    "18:00": "💖 FB Myanmar User Boost Service 💖\n\nFb like&follow 1k - 11500\nFb post like 1k - 11500\n\nဝယ်ယူရန် - @thiha3124\n\n#Daezy",
    "20:00": "YouTube Like / View Service 🎬\n\nLike 1k - 3500ks\nView 1k - 10000ks\n\nဝယ်ယူရန် - @thiha3124\n\n#Daezy",
    "21:30": "🚀 Boost Service owner ခဏမအားသေးပါ\n\n⏰ 9:00 PM – 11:00 PM\n\nOrder တွေထားခဲ့ပေးနော် ✅\nအားတာနဲ့ချက်ချင်း Reply ပြန်ပေးပါမယ် 🔥"
}

# AUTO POST (မြန်မာအချိန်နဲ့)
async def auto_post(context: ContextTypes.DEFAULT_TYPE):
    now = get_myanmar_time().strftime("%H:%M")
    if now in SCHEDULED_POSTS:
        try:
            await context.bot.send_message(chat_id=CHANNEL_ID, text=SCHEDULED_POSTS[now])
            print(f"✅ Posted at {now} (Myanmar Time)")
        except Exception as e:
            print(f"❌ Error at {now}: {e}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = get_myanmar_time().strftime("%H:%M %p")
    await update.message.reply_text(f"🤖 Schedule Bot Running Successfully!\n\n🇲🇲 မြန်မာအချိန်: {now}")

if __name__ == '__main__':
    app = Application.builder().token(BOT_TOKEN).connection_pool_size(8).read_timeout(30).write_timeout(30).build()

    app.add_handler(CommandHandler("start", start))
    app.job_queue.run_repeating(auto_post, interval=60, first=5)

    print("🚀 Bot Started Successfully (Myanmar Timezone UTC+6:30)")
    app.run_polling(drop_pending_updates=True)
  
