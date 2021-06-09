import logging

from aiogram import Bot, Dispatcher, executor, types
import config


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)
sti = open('stickers/sticker.webp','rb')


@dp.message_handler()
async def filter_message(message: types.Message):
    if config.Ban_world1 in message.text :
        await message.delete()
        await message.bot.kick_chat_member(chat_id=config.GROUP_ID,user_id=message.from_user.id)
    if config.Ban_world2 in message.text :
       await message.delete()
       await message.bot.kick_chat_member(chat_id=config.GROUP_ID, user_id=message.from_user.id)

    if config.Ban_world3 in message.text :
       await message.delete()
       await message.bot.kick_chat_member(chat_id=config.GROUP_ID, user_id=message.from_user.id)
    if "Правила" in message.text :
        await message.bot.send_message(chat_id=config.GROUP_ID,text=config.Rule)

@dp.message_handler(content_types=["new_chat_members"])
async def on_user_joined(message: types.Message):
    await message.bot.send_sticker(chat_id=config.GROUP_ID,sticker=sti)
    await message.bot.send_message(chat_id=config.GROUP_ID,text=config.HI)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)