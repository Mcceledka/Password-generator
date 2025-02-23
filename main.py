from aiogram import Bot, Dispatcher, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import CommandStart
import asyncio
import logging
from aiogram import F
from password import generate_pass_easy, generate_pass_med, generate_pass_hard, generate_pass_extreme
from config import TOKEN

class myStates(StatesGroup):
    button = State()
    choose_difficult = State()
    input_length_ez = State()
    input_length_md = State()
    input_length_hd = State()
    input_length_ext = State()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message(CommandStart())
async def start(message: Message, state: FSMContext):
    kb = [[types.KeyboardButton(text='Сгенерировать пароль')]]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    
    await message.answer("Добрый день, это бот который генерирует пароли, что вы хотите сделать?", reply_markup=keyboard)
    await state.set_state(myStates.button)

@dp.message(myStates.button, F.text.casefold() == "сгенерировать пароль")
async def choose_diff(message: Message, state: FSMContext):
    kb = [
        [types.KeyboardButton(text="Легкий")],
        [types.KeyboardButton(text="Средний")],
        [types.KeyboardButton(text="Тяжелый")],
        [types.KeyboardButton(text="Очень тяжелый")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Какой уровень сложности пароля вы хотите иметь?", reply_markup=keyboard)
    await state.set_state(myStates.choose_difficult)

@dp.message(myStates.choose_difficult, F.text.casefold() == "легкий")
async def input_length(message: Message, state: FSMContext):
    await message.answer("Введите количество символов в пароле:")
    await state.set_state(myStates.input_length_ez)

@dp.message(myStates.input_length_ez)
async def generate_pass(message: Message, state: FSMContext):
    try:
        length = int(message.text)
    
        if length > 2000:
            await message.answer("Введите число от 1 до 1999:|")
            return
        elif length <= 0:
            await message.answer("Введите положительное число>:(")
            return
        else:
            password = generate_pass_easy(length)
            await message.answer(f"Ваш сгенерированный пароль:{password}")
            await state.clear()
    except ValueError:
        await message.answer("Введите корректное число!")

@dp.message(myStates.choose_difficult, F.text.casefold() == "средний")
async def input_length(message: Message, state: FSMContext):
    await message.answer("Введите количество символов в пароле:")
    await state.set_state(myStates.input_length_md)

@dp.message(myStates.input_length_md)
async def generate_pass(message: Message, state: FSMContext):
    try:
        length = int(message.text)
    
        if length > 2000:
            await message.answer("Введите число от 1 до 1999:|")
            return
        elif length <= 0:
            await message.answer("Введите положительное число>:(")
            return
        else:
            password = generate_pass_med(length)
            await message.answer(f"Ваш сгенерированный пароль:{password}")
            await state.clear()
    except ValueError:
        await message.answer("Введите корректное число!")
    
@dp.message(myStates.choose_difficult, F.text.casefold() == "тяжелый")
async def input_length(message: Message, state: FSMContext):
    await message.answer("Введите количество символов в пароле:")
    await state.set_state(myStates.input_length_hd)

@dp.message(myStates.input_length_hd)
async def generate_pass(message: Message, state: FSMContext):
    try:
        length = int(message.text)
    
        if length > 2000:
            await message.answer("Введите число от 1 до 1999:|")
            return
        elif length <= 0:
            await message.answer("Введите положительное число>:(")
            return
        else:
            password = generate_pass_hard(length)
            await message.answer(f"Ваш сгенерированный пароль:{password}")
            await state.clear()
    except ValueError:
        await message.answer("Введите корректное число!")
    
@dp.message(myStates.choose_difficult, F.text.casefold() == "очень тяжелый")
async def input_length(message: Message, state: FSMContext):
    await message.answer("Введите количество символов в пароле:")
    await state.set_state(myStates.input_length_ext)

@dp.message(myStates.input_length_ext)
async def generate_pass(message: Message, state: FSMContext):
    try:
        length = int(message.text)
    
        if length > 2000:
            await message.answer("Введите число от 1 до 1999:|")
            return
        elif length <= 0:
            await message.answer("Введите положительное число>:(")
            return
        else:
            password = generate_pass_extreme(length)
            await message.answer(f"Ваш сгенерированный пароль:{password}")
            await state.clear()
    except ValueError:
            await message.answer("Введите корректное число!")
            
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    

