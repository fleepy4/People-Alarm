from aiogram.bot import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from bot_files import db, keyboard
storage = MemoryStorage()
bot = Bot(token='5537898680:AAHYtK67uW1aui_dvM5P6mA7G2v8wc1Pc2Y')
dp = Dispatcher(bot, storage=storage)
passwd = 'si5Jofdg434f'


class Register(StatesGroup):
    enter_pass = State()


@dp.message_handler(commands=['start'])
async def start(m: Message, state: FSMContext):
    await bot.send_message(m.from_user.id, 'Для авторизации и получения доступа к боту, введите пароль')
    await Register.enter_pass.set()


@dp.message_handler(content_types=['text'], state=Register.enter_pass)
async def check_pswd(m: Message, state: FSMContext):
    if m.text == passwd:
        await bot.send_message(m.from_user.id, 'Процесс аутентификации успешно завершен!\n\n'
                                               'Вы получили доступ ко всем функциям!')
        db.auth(m.from_user.id)
    else:
        await bot.send_message(m.from_user.id, 'Пароль введен не верно!')
    await state.finish()