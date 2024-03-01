import asyncio
import config
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import logging
import random

#Включаем логгирование
logging.basicConfig(level=logging.INFO)

#Создаем объект бота
bot = Bot(token=config.token)

#Диспечер
dp = Dispatcher()

#Хэндлер на команду /start
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.reply(f'Привет, {name}! Доступные команды: /start, /stop, /random, /info, /user')


#Хэндлер на команду /stop
@dp.message(Command('stop'))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.reply(f'Спасибо, {name}!')


#Хэндлер на команду /random
@dp.message(Command('random'))
async def cmd_random(message: types.Message):
    name = message.chat.first_name
    await message.reply(f'Случайное число: {random.randint(1, 100)}')

#Хэндлер на команду /info
@dp.message(Command('info'))
async def cmd_info(message: types.Message):
    name = message.chat.first_name
    await message.reply(f'Информация о боте: {name}')

#Хэндлер на команду /user
@dp.message(Command('user'))
async def cmd_user(message: types.Message):
    name = message.chat.first_name
    await message.reply(f'Информация о пользователе: {name}')

# Если написали любое сообщение, то отправляем доступные команды
@dp.message()
async def cmd_any(message: types.Message):
    name = message.chat.first_name
    await message.reply(f'Неизвестная команда: {name} Список команд: /start, /stop, /random, /info, /user')

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())