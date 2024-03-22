from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatActions, ReplyKeyboardMarkup, KeyboardButton, callback_game

from aiogram import types

# Стартовые кнопки
def start():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text="🍨Бонус за отзыв", callback_data='bonus'),
        types.InlineKeyboardButton(text="🌺Бонус за отметку в инстаграмм", callback_data='insta_bonus'),
        types.InlineKeyboardButton(text="❓Задать вопрос", callback_data='support'),      
        types.InlineKeyboardButton(text="🧸Наш магазин", callback_data='shop')
    ]
    keyboard.add(*buttons)
    return keyboard


    
# Выбор маркетплейса
def marketplace():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text='Wildberries', callback_data='wildberries'),
        types.InlineKeyboardButton(text='Ozon', callback_data='ozon'),
        types.InlineKeyboardButton(text='⬅️Вернуться в главное меню', callback_data='back')
    ]
    keyboard.add(*buttons)
    return keyboard


def back_to_menu():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text='⬅️Обратно в меню', callback_data='back')
    
    ]
    keyboard.add(*buttons)
    return keyboard


    
# Отзывы с Озона
def ozon_review():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
         types.InlineKeyboardButton(text='Я оставил(а) отзыв', callback_data='review_ozon'),
         types.InlineKeyboardButton(text='⬅️Вернуться в главное меню', callback_data='back')
    ]
    keyboard.add(*buttons)
    return keyboard

def check():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text='Отправить скриншот', callback_data='photo'),
        types.InlineKeyboardButton(text='⬅️Вернуться в главное меню', callback_data='back')

    ]
    keyboard.add(*buttons)
    return keyboard


#Отзывы с Вб 
def wb_review():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text='Я оставил(а) отзыв', callback_data='review_wb'),
        types.InlineKeyboardButton(text='⬅️Вернуться в главное меню', callback_data='back')
    ]

    keyboard.add(*buttons)
    return keyboard


#Отзывы с инстаграмм
def inst_review():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
         types.InlineKeyboardButton(text='Я оставил(а) пост/сторис', callback_data='review_inst'),
         types.InlineKeyboardButton(text='⬅️Вернуться в главное меню', callback_data='back')
    ]
    keyboard.add(*buttons)
    return keyboard


#Ссылки на магазин
def our_shop_urls():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
         types.InlineKeyboardButton(text='Wildberries', url='https://www.wildberries.ru/brands/yhata'),
         types.InlineKeyboardButton(text='Ozon', url='https://www.ozon.ru/seller/yhata-204817/products/?miniapp=seller_204817'),
         types.InlineKeyboardButton(text='⬅️Вернуться в главное меню', callback_data='back')
    ]
    keyboard.add(*buttons)
    return keyboard
    