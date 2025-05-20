from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile

from src.bot.keyboards import StartMenu
from src.bot.functions import main_menu_text
from src.database.quaries import add_customer


router_handler = Router()


@router_handler.message(CommandStart())
async def start(message: Message) -> None:
    user = message.from_user
    add_customer(user.id, user.first_name)
    text, path = main_menu_text()
    photo = FSInputFile(path)
    await message.answer_photo(photo=photo, caption=text, reply_markup=StartMenu)


@router_handler.message(Command("faq"))
async def faq(message: Message) -> None:
    user = message.from_user
    add_customer(user.id, user.first_name)
    await message.answer('Что может этот бот:')


# @router_handler.message(~F.state)
# async def unknown(message: Message) -> None:
#     user = message.from_user
#     add_customer(user.id, user.first_name)
#     await message.answer(text='К сожалению, я вас не понял', reply_markup=BackToMenu)