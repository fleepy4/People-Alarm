from aiogram.bot import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from bot_files import keyboard
import db

storage = MemoryStorage()
bot = Bot(token='5537898680:AAHYtK67uW1aui_dvM5P6mA7G2v8wc1Pc2Y')
dp = Dispatcher(bot, storage=storage)
passwd = 'si5Jofdg434f'


class Register(StatesGroup):
    enter_pass = State()


@dp.message_handler(commands=['start'])
async def start(m: Message, state: FSMContext):
    if not db.is_auth(m.from_user.id):
        await bot.send_message(m.from_user.id, 'Для авторизации и получения доступа к боту, введите пароль')
        await Register.enter_pass.set()
    else:
        await bot.send_message(
            m.from_user.id,
            'Клавиатура обновлена!',
            reply_markup=keyboard.main_kb()
        )

@dp.message_handler(content_types=['text'], state=Register.enter_pass)
async def check_pswd(m: Message, state: FSMContext):
    if m.text == passwd:
        await bot.send_message(
            m.from_user.id,
            'Процесс аутентификации окончен!\n\nВы получили доступ ко всем функциям!',
            reply_markup=keyboard.main_kb()
        )
        db.auth(m.from_user.id)
    else:
        await bot.send_message(m.from_user.id, 'Пароль введен не верно!')
    await state.finish()

@dp.message_handler(content_types=['text'])
async def text_processor(m: Message):
    if db.is_auth(m.from_user.id):
        if m.text == 'Включить/Выключить сигнализацию':
            if db.change_status() == 0:
                await bot.send_message(
                    m.from_user.id,
                    '❌ Сигнализация успешно отключена!'
                )
            else:
                await bot.send_message(
                    m.from_user.id,
                    '✅ Сигнализация успешно включена!'
                )

if __name__ == '__main__':
    executor.start_polling(dp)
