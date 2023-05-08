from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


start_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('📞 Контакти УК', url='https://telegra.ph/Kontakti-04-26'),
        InlineKeyboardButton('Розклад руху 🚆', url='https://telegra.ph/rfgrgfefdgdfgfdgfdg-04-14'),
    ],
    [InlineKeyboardButton('💳 Реквізити для оплати', url='https://telegra.ph/REKV%D0%86ZITI-TOV-UK-Kocyubinske-04-26')],
    [InlineKeyboardButton('📝 Cтворити особистий кабінет', callback_data='create_account')]
])


btn_reg = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('🔐 - по коду реєстрації', callback_data='kod_register')],
    [InlineKeyboardButton('📱 - за номером телефону', callback_data='acc_phone')],
    [InlineKeyboardButton('Назад', callback_data='start')]
])

btn_reg2 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Реєстрація по телефону', request_contact=True)]
], resize_keyboard=True)
