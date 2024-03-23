import asyncio
import os


from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ContentTypes, callback_query
from dotenv import load_dotenv

import aiogram
from aiogram import Bot, Dispatcher, executor, types

from keyboard import *


load_dotenv()
storage = MemoryStorage()
tg_token = '7063562748:AAGk0xoUOVrPLcHqcKrCKZ1DsedXopc_2Ss'
bot = Bot(token=tg_token)
dp = Dispatcher(bot, storage=MemoryStorage())
contact = ''

def get_contact(msg):
    global contact
    contact = msg.text
    contact_log = open ('User\Contacts.txt', 'a')
    contact_log.write(f'Contact {msg.from_user.id}')
    contact_log.close()

class W(StatesGroup):
    waiting_for_photo = State()
    waiting_for_contact = State()


@dp.callback_query_handler(text=['bonus'])
async def main_menu (call: types.CallbackQuery):
        await call.message.answer (text='Где вы делали заказ?', reply_markup=marketplace())

@dp.message_handler(commands=['start'])
async def start_msg (msg: types.Message):
    text = 'Здравствуйте! Спасибо, что обратились в службу поддержки "Yhata"⭐️\n\nВыберите, пожалуйста, один из вариантов.'
    await msg.answer(text, reply_markup=start())

@dp.callback_query_handler(text=['support'])
async def msg_support (call: types.CallbackQuery):
    await call.message.answer (text='Для связи с администратором используйте адрес электронной почты: qwerty@example.ru или телеграмм @example', reply_markup=back_to_menu())

@dp.callback_query_handler(text=['back'])
async def menu1 (call: types.CallbackQuery):
    await call.message.answer (text='Вы вернулись в главное меню', reply_markup=start())

@dp.callback_query_handler(text=['shop'])
async def our_shop(call: types.CallbackQuery): 
    await call.message.answer (text='Ниже представлены ссылки на наш магазин:', reply_markup=our_shop_urls())

@dp.callback_query_handler(text=['photo'])
async def screen (call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(text='Отправьте скриншот отзыва', reply_markup=back_to_menu())
    await W.waiting_for_photo.set()


@dp.message_handler(content_types=ContentTypes.PHOTO, state=W.waiting_for_photo)
async def screen_photo (msg:types.Message, state: FSMContext):
    await msg.answer(text='Отлично! Спасибо за отзыв! Укажите, пожалуйста, номер телефона, ФИО и банк для получения бонуса, например: +79259999999, Иванов Иван Иванович, Сбербанк', reply_markup=back_to_menu())
    photo_info = await bot.get_file(msg.photo[-1].file_id) 
    photo_name = f'photo_{msg.from_user.id}.jpg'
    if not os.path.exists('Media'):
        os.makedirs('Media')
    dest_dir = f'Media\{photo_name}'
    await photo_info.download(dest_dir)
    await W.waiting_for_contact.set()


@dp.message_handler(state=W.waiting_for_contact)
async def get_contact (msg: types.Message, state: FSMContext):
    global contact
    contact = msg.text
    if not os.path.exists('Media'):
        os.makedirs('Media')
    contact_log = open(f'Media/Anketa_{msg.from_user.id}.txt', 'a')
    contact_log.write(f'Contact {msg.from_user.id}, {msg.text}')
    contact_log.close()
    await msg.answer(text='Контактные данные получены. Спасибо за отзыв! Бонус будет начислен после проверки скриншота - обычно это занимает 2-3 часа.', reply_markup=start())
    await state.finish()


@dp.callback_query_handler(text=['wildberries'])
async def bonus_wb (call: types.CallbackQuery):
    await call.message.answer (text='''Чтобы получить бонус, выполните несколько простых действий.\n1. Откройте приложение Wildberries на телефоне. \n2. Нажмите на иконку профиля в нижнем правом углу. \n3. Выберите категорию «Мои покупки».\n4. Выберите товар, на который хотите оставить отзыв. \n5. Найдите строчку «Отзывы», находится обычно под описанием товара. \n6. Нажмите кнопку «Написать отзыв» (или «Оценить»). \n7. Оцените наш товар звездочками.\n8. Напишите текстовый отзыв.\nЗа текстовый отзыв бонус 100р, за отзыв с 2 фото 150р''', reply_markup=wb_review())

@dp.callback_query_handler(text=['review_wb'])
async def r_wb(call: types.CallbackQuery):
    await call.message.answer(text='Предоставьте скриншот отзыва:\n(1) Пройдите по ссылке https://www.wildberries.ru/lk/discussion/feedback\nИз браузера, не переходя в приложение, нажмите в правом нижнем углу иконку профиля и выполните ВХОД в АККАУНТ. \n(2) Отобразится Ваш оставленный отзыв. Сделайте скриншот отзыва и пришлите его сюда.\n(3) Если отзыв не отображается, перейдите по иконке профиля и затем в раздел «Отзывы и вопросы», найдите нужный отзыв и сделайте скриншот.\n(4) Нажмите кнопку «Отправить скриншот», введите все нужные данные и отправьте Ваш скриншот чат-боту.', reply_markup=check())


@dp.callback_query_handler(text=['ozon'])
async def bonus_ozon(call: types.CallbackQuery):
    await call.message.answer (text='''Чтобы получить бонус, выполните несколько простых действий.\n1. Откройте приложение Ozon на телефоне. \n2. Нажмите на иконку профиля в нижнем правом углу. \n3. Выберите категорию «Покупки».\n4. Выберите товар, на который хотите оставить отзыв. \n5. Нажмите кнопку «Написать» (или «Оценить»). \n6. Оцените наш товар звездочками.\n7. Напишите текстовый отзыв.\nЗа текстовый отзыв бонус 100р, за отзыв с 2 фото 150р, с видео 200р''', reply_markup=ozon_review())


@dp.callback_query_handler(text=['review_ozon'])
async def r_ozon(call: types.CallbackQuery):
    await call.message.answer(text='Предоставьте скриншот отзыва:\n(1) Пройдите по ссылке https://www.ozon.ru/my/reviews\nИз браузера, не переходя в приложение, нажмите в правом нижнем углу иконку профиля и выполните ВХОД в АККАУНТ. \n(2) Отобразится Ваш оставленный отзыв. Сделайте скриншот отзыва и пришлите его сюда.\n(3) Если отзыв не отображается, перейдите по иконке профиля и затем в раздел «Мои отзывы», найдите нужный отзыв и сделайте скриншот.\n(4) Нажмите кнопку «Отправить скриншот», введите все нужные данные и отправьте Ваш скриншот чат-боту.', reply_markup=check())


@dp.callback_query_handler(text=['review_inst'])
async def r_inst(call: types.CallbackQuery):
    await call.message.answer (text='Пришлите в диалог скриншот после того, как сторис или пост «провисит» указанное время (10-12 часов) (отправляйте, пожалуйста, только скриншот, без текста).', reply_markup=check())


@dp.callback_query_handler(text=['insta_bonus'])
async def bonus_inst(call: types.CallbackQuery):
    await call.message.answer (text='Мы дарим 300₽ за отметку в сторис или посте Instagram каждому клиенту с АКТИВНЫМ аккаунтом от 50 подписчиков. (1 товар = 1 бонус)\nЧтобы получить бонус, сделайте несколько простых действий.\n1. Опубликуйте фото в сторис или посте.\n2. На фото должны быть Вы с товаром или товар который Вы приобрели у нас.\n3. В сторис или посте должен быть указан артикул товара, приобретенного в нашегом магазине. Артикул должен быть ЗАМЕТЕН для Ваших подписчиков, а сторис или пост должны находиться на странице не меньше 10-12 часов.', reply_markup=inst_review())



    

if '__main__' == __name__:
    executor.start_polling(dp,
                           skip_updates=True)