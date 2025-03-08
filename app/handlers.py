import asyncio
from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    """Ответ бота на комманду старт"""
    await message.answer("Привет", reply_markup=kb.main)
    await message.reply("Как дела?")


@router.message(Command("help"))
async def cmd_help(message: Message):
    """Ответ бота на определенную комманду"""
    await message.answer(" Вы нажали на кнопуку помощи")


@router.message(F.text == "У меня все хорошо")
async def nice(message: Message):
    """Ответ бота на определенный текст"""
    await message.answer("Я очень рад")
