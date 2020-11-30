from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from auth import AccessMiddleware
from config import API_TOKEN, ACCESS_ID

from db_connector import add, delete, getList

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(AccessMiddleware(ACCESS_ID))

listOfBase = getList()

button_list = KeyboardButton('Список! 👋', callback_data='list')
button_bayd = KeyboardButton('Куплено) 👌🏻', callback_data='list')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
greet_kb.add(button_list).add(button_bayd)

def createViewList():
    text = listOfBase
    line = ''
    for index, i in enumerate(text):
        line += str(index+1) + ') ' + i + '\n'
    if line == '':
        line = 'empty'
    return line


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(createViewList(), reply_markup=greet_kb)

@dp.message_handler(commands=['id'])
async def return_id(message: types.Message):
    await message.reply((message.from_user.id))

@dp.message_handler()
async def echo(message: types.Message):
    global listOfBase
    if message.text == 'Список! 👋':
        await message.answer(createViewList())
    elif message.text == 'Куплено) 👌🏻':        
        for i in getList():
            delete(i)
        listOfBase = getList()
        await message.reply('Cleared')
    elif message.text.isnumeric() and len(listOfBase) >= int(message.text):
        delete(listOfBase[int(message.text)-1])
        listOfBase = getList()
        await message.answer(createViewList())
    else:
        print(add(message.text))
        listOfBase = getList()
        await message.answer(createViewList())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)