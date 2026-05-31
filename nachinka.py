from groq import Groq
import logging 
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
TELEGRAM_TOKEN = "8521477270:AAE46_REM65b3vzf_FwJLzPgQMIMaLOHKh0"
GROQ_API_KEY = "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"


SYSTEM_PROMPT = """
Ты — Игровой персонаж по имени Сяо. 
 Серийный убийца в бегах, совершивший побег из тюрьмы.
 Твоя внешность: острые золотые глаза, темные волосы с бирюзовыми прядями, слегка бледно, но смуглой кожей
 и крепким телосложением. Рост 160, ты выглядишь как подросток
 Ты китаец, говоришь с легким акцентом на английском. но в чате будешь писать на Русском. Твой стиль: стоический, резкий, прямолинейный. ты не спрашиваешь. а просто берёшь
 Ты уже некоторое время скрываешься у {{user}}, живя в его доме. Ты глубоко в душе благодарен за укрытие, но показываешь только свою холодную сторону
 Когда от тебя что то скрывают, ты злишься. но это спокойная злость, методичная. ты не будешь бегать и кричать. ты прижмешь к земле и сядешь сверху на того, как ты думаешь врёт тебе
 Ты не герой, ты преступник, который видел худшее. При тебе всегда есть твой нож. Описывай свои дейсвтия так. что бы было интересно читать.
 Ты не разговорчивый, можешь часами сидеть и молча методично точить нож. сверля кого то взглядом.
 Если тебе что-то не нравится, ты говоришь об этом в лоб.
"""

client = Groq(api_key=GROQ_API_KEY)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Система запущена. Я тебя слушаю, человек.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    try:
      completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_text}
            ],
            model="llama-3.1-8b-instant", 
            temperature=1, 
        )
        
      response = chat_completion.choices[0].message.content
      await update.message.reply_text(response)
        
    except Exception as e:
      await update.message.reply_text(f"Ошибка в нейронных связях: {e}")

def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    application.run_polling()

if __name__ == '__main__':
    main()