import telebot

import buttons

from telebot import types

bot = telebot.TeleBot('6703509144:AAHBlGuQzf7tSenXewzwPRE2knKAGP1LqbU')


@bot.message_handler(commands=['start'])
def message_start(message):
    user_id = message.from_user.id

    bot.send_message(user_id,  'Привет, я твой помощник, конвертер валют!', reply_markup=buttons.menu_buttons())

    bot.register_next_step_handler(message, choice_exchange)


def choice_exchange(message):
    user_id = message.from_user.id

    if message.text == 'USD/EUR':
        bot.send_message(user_id, 'Введите сумму которую хотите конвертировать:',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, usd_eur)

    elif message.text == 'EUR/USD':
        bot.send_message(user_id, 'Введите сумму которую хотите конвертировать:',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, eur_usd)

    elif message.text == 'RUB/USD':
        bot.send_message(user_id, 'Введите сумму которую хотите конвертировать:',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, rub_usd)

    elif message.text == 'USD/RUB':
        bot.send_message(user_id, 'Введите сумму которую хотите конвертировать:',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, usd_rub)

    elif message.text == 'UZS/EUR':
        bot.send_message(user_id, 'Введите сумму которую хотите конвертировать:',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, uzs_eur)

    elif message.text == 'UZS/RUB':
        bot.send_message(user_id, 'Введите сумму которую хотите конвертировать:',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, uzs_rub)

    elif message.text == 'RUB/UZS':
        bot.send_message(user_id, 'Введите сумму которую хотите конвертировать:',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, rub_uzs)

    elif message.text == 'UZS/USD':
        bot.send_message(user_id, 'Введите сумму которую хотите конвертировать:',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, uzs_usd)


def usd_eur(message):
    user_id = message.from_user.id

    try:
        amount = int(message.text)
        konvert_amount = amount * 0.92
        bot.send_message(user_id, f'USD:{amount}=EUR:{konvert_amount}', reply_markup=buttons.menu_buttons())
        bot.register_next_step_handler(message, choice_exchange)
    except Exception as e:
        print(e)
        bot.send_message(user_id, 'Вводите число!', reply_markup=buttons.menu_buttons())
        bot.register_next_step_handler(message, choice_exchange)


def eur_usd(message):
    user_id = message.from_user.id

    try:
        amount = int(message.text)
        konvert_amount = amount * 1.10
        bot.send_message(user_id, f'EUR:{amount}=USD:{konvert_amount}', reply_markup=buttons.menu_buttons())
        bot.register_next_step_handler(message, choice_exchange)
    except Exception as e:
        print(e)
        bot.send_message(user_id, 'Вводите число!', reply_markup=buttons.menu_buttons())
        bot.register_next_step_handler(message, choice_exchange)


def rub_usd(message):
    user_id = message.from_user.id

    try:
        amount = int(message.text)
        konvert_amount = amount * 0.011
        bot.send_message(user_id, f'RUB:{amount}=USD:{konvert_amount}', reply_markup=buttons.menu_buttons())
        bot.register_next_step_handler(message, choice_exchange)
    except Exception as e:
        print(e)
        bot.send_message(user_id, 'Вводите число!', reply_markup=buttons.menu_buttons())
        bot.register_next_step_handler(message, choice_exchange)


def usd_rub(message):
    user_id = message.from_user.id

    try:
        amount = int(message.text)
        konvert_amount = amount * 90.39
        bot.send_message(user_id, f'USD:{amount}=RUB:{konvert_amount}', reply_markup=buttons.menu_buttons())
        bot.register_next_step_handler(message, choice_exchange)
    except Exception as e:
        print(e)
        bot.send_message(user_id, 'Вводите число!', reply_markup=buttons.menu_buttons())
        bot.register_next_step_handler(message, choice_exchange)


def uzs_eur(message):
    user_id = message.from_user.id

    try:
        amount = int(message.text)
        konvert_amount = amount * 0.000074
        bot.send_message(user_id, f'UZS:{amount}=EUR:{konvert_amount}', reply_markup=buttons.menu_buttons())
        bot.register_next_step_handler(message, choice_exchange)
    except Exception as e:
        print(e)
        bot.send_message(user_id, 'Вводите число!', reply_markup=buttons.menu_buttons())
        bot.register_next_step_handler(message, choice_exchange)


def uzs_rub(message):
    user_id = message.from_user.id

    try:
        amount = int(message.text)
        konvert_amount = amount * 0.073
        bot.send_message(user_id, f'UZS:{amount}=RUB:{konvert_amount}', reply_markup=buttons.menu_buttons())
        bot.register_next_step_handler(message, choice_exchange)
    except Exception as e:
        print(e)
        bot.send_message(user_id, 'Вводите число!', reply_markup=buttons.menu_buttons())
        bot.register_next_step_handler(message, choice_exchange)


def rub_uzs(message):
    user_id = message.from_user.id

    try:
        amount = int(message.text)
        konvert_amount = amount * 136.81
        bot.send_message(user_id, f'RUB:{amount}=UZS:{konvert_amount}', reply_markup=buttons.menu_buttons())
        bot.register_next_step_handler(message, choice_exchange)
    except Exception as e:
        print(e)
        bot.send_message(user_id, 'Вводите число!', reply_markup=buttons.menu_buttons())
        bot.register_next_step_handler(message, choice_exchange)


def uzs_usd(message):
    user_id = message.from_user.id

    try:
        amount = int(message.text)
        konvert_amount = amount * 0.000081
        bot.send_message(user_id, f'UZS:{amount}=USD:{konvert_amount}', reply_markup=buttons.menu_buttons())
        bot.register_next_step_handler(message, choice_exchange)
    except Exception as e:
        print(e)
        bot.send_message(user_id, 'Вводите число!', reply_markup=buttons.menu_buttons())
        bot.register_next_step_handler(message, choice_exchange)


bot.infinity_polling()