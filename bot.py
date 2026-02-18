import os
import random
import logging
from pathlib import Path
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import FSInputFile
import asyncio

# Настройки
logging.basicConfig(level=logging.INFO)
BOT_TOKEN = os.getenv("BOT_TOKEN")
MEDIA_FOLDER = Path("media")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(F.text.lower() == "овнер")
async def cat_reply(message: types.Message):
    await message.answer("Ильяс, он же W140_2016, — легендарный " \
    "киберспортсмен в Мир танков. Любит ПТ-САУ и в них практически " \
    "непобедим: точность, стратегия и молниеносные реакции делают его " \
    "страшным противником. Его статистика одна из лучших в мире, а бой с его участием всегда превращается в маленькое произведение искусства.")

@dp.message(F.text.lower() == "илья")
async def cat_reply(message: types.Message):
    await message.answer("АЛО НАХ")

@dp.message(F.text.lower() == "даня")
async def cat_reply(message: types.Message):
    await message.answer("Даня — фанат здорового питания и правильного образа жизни. " \
    "Всегда следит за тем, что ест, советует другим, читает составы и калории, " \
    "и иногда может быть слегка занудным, но зато с ним точно не съешь ничего лишнего")

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("приветик, это я, кариночка 💋")

@dp.message(Command("pazor"))
async def start(message: types.Message):
    await message.answer("Пазор — особая субстанция стыда, тонкая грань между «фу» и «смешно»" \
    "впервые переосмысленная и слегка исказная Ильей. Пазоркинс — маленький, почти милый пазор. " \
    "Пазорище — настоящий, такой, что от него глаза на лоб лезут. В отличие от обычного позора, " \
    "пазор обратим: сегодня ты пазорник, а завтра — легенда. Это квинтэссенция кринжа, ставшая родной.")

@dp.message(F.text.lower().contains("лярва"))
async def send_random_media(message: types.Message):
    files = [f for f in MEDIA_FOLDER.iterdir() if f.is_file()]
    if not files:
        return
    
    random_file = random.choice(files)
    ext = random_file.suffix.lower()
    
    try:
        if ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
            await message.answer_photo(FSInputFile(random_file))
        elif ext in ['.mp4', '.avi', '.mov', '.mkv']:
            await message.answer_video(FSInputFile(random_file))
        else:
            await message.answer_document(FSInputFile(random_file))
    except Exception as e:
        logging.error(f"Ошибка: {e}")

# Запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())