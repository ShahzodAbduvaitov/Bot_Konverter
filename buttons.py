from telebot import types


def menu_buttons():

    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn1 = types.KeyboardButton('USD/EUR')

    btn2 = types.KeyboardButton('EUR/USD')

    btn3 = types.KeyboardButton('RUB/USD')

    btn4 = types.KeyboardButton('USD/RUB')

    btn5 = types.KeyboardButton('UZS/EUR')

    btn6 = types.KeyboardButton('UZS/RUB')

    btn7 = types.KeyboardButton('RUB/USZ')

    btn8 = types.KeyboardButton('UZS/USD')

    buttons.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)

    return buttons
















