from telegram.ext import CallbackContext
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

from db import db
from message import message

def start(update: Update, context: CallbackContext):
    if db.get_user_phone(update.message.from_user.id):
        update.message.reply_text(
            message['start'].format(update.message.from_user.full_name),
            reply_markup=ReplyKeyboardMarkup(
                [
                    [
                        KeyboardButton("Buyurtma berish", web_app=WebAppInfo(url='https://uzum.uz')),
                    ],
                    [
                        KeyboardButton("Buyurtmalarim"),
                        KeyboardButton("Sozlamalar"),
                    ],
                    [
                        KeyboardButton("Biz haqimizda"),
                        KeyboardButton("Fikr qoldirish"),
                    ],
                ],
                resize_keyboard=True
            )
        )
    else:
        update.message.reply_text(
            message['first_phone_number'],
            reply_markup=ReplyKeyboardMarkup(
                [
                    [
                        KeyboardButton("Telefon raqamingizni yuboring", request_contact=True)
                    ]
                ],
                resize_keyboard=True
            )
        )
    

def save_contact(update: Update, context: CallbackContext):
    if update.message.contact.user_id != update.message.from_user.id:
        return
    user = update.message.from_user
    db.save_user(user.id, user.username, user.first_name, user.last_name, update.message.contact.phone_number)
    update.message.reply_text(
        message['save_contact'],
        reply_markup=ReplyKeyboardMarkup(
                [
                    [
                        KeyboardButton("Buyurtma berish", web_app=WebAppInfo(url='https://uzum.uz')),
                    ],
                    [
                        KeyboardButton("Buyurtmalarim"),
                        KeyboardButton("Sozlamalar"),
                    ],
                    [
                        KeyboardButton("Biz haqimizda"),
                        KeyboardButton("Fikr qoldirish"),
                    ],
                ],
                resize_keyboard=True
            )
    )
    
    
def orders(update: Update, context: CallbackContext):
    if db.get_user_phone(update.message.from_user.id):
        update.message.reply_text(
            message['orders'],
        )
    else:
        update.message.reply_text(
            message['first_phone_number'],
            reply_markup=ReplyKeyboardMarkup(
                [
                    [
                        KeyboardButton("Telefon raqamingizni yuboring", request_contact=True)
                    ]
                ],
                resize_keyboard=True
            )
        )
        

def info(update: Update, context: CallbackContext):
    if db.get_user_phone(update.message.from_user.id):
        update.message.reply_text(
            "shu yerda joylashganmiz",
        )
        update.message.reply_text(
            "Elektron pochta: abror4work@gmail.com",
        )
    else:
        update.message.reply_text(
            message['first_phone_number'],
            reply_markup=ReplyKeyboardMarkup(
                [
                    [
                        KeyboardButton("Telefon raqamingizni yuboring", request_contact=True)
                    ]
                ],
                resize_keyboard=True
            )
        )

def settings_bot(update: Update, context: CallbackContext):
    pass

def fikr_qoldirish(update: Update, context: CallbackContext):
    if db.get_user_phone(update.message.from_user.id):
        update.message.reply_text(
            """Buyurtma berish uchun asosiy menyudagi “Buyurtma” tugmasidan foydalaning.

Biz sizning fikr-mulohazalaringizni juda qadrlaymiz! Buyurtma berganingizdan so'ng, o'z fikr va mulohazalaringizni shu yerda qoldirishingiz mumkin""",
        )
    else:
        update.message.reply_text(
            message['first_phone_number'],
            reply_markup=ReplyKeyboardMarkup(
                [
                    [
                        KeyboardButton("Telefon raqamingizni yuboring", request_contact=True)
                    ]
                ],
                resize_keyboard=True
            )
        )
    