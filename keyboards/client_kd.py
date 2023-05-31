from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


start_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('📞 Контакти УК', url='https://telegra.ph'),
        InlineKeyboardButton('Розклад руху 🚆', url='https://telegra.ph/rfgrgfefdgdfgfdgfdg-04-14'),
    ],
    [InlineKeyboardButton('💳 Реквізити для оплати', url='https://telegra.ph')],
    [InlineKeyboardButton('🛠 Cтворити особистий кабінет', callback_data='create_account')]
])

btn_reg2 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Реєстрація по телефону', request_contact=True)]
], resize_keyboard=True)

account = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('📞 Контакти УК', url='https://telegra.ph'),
        InlineKeyboardButton('Розклад руху 🚆', url='https://telegra.ph/rfgrgfefdgdfgfdgfdg-04-14'),
    ],
    [InlineKeyboardButton('💳 Реквізити для оплати', url='https://telegra.ph')],
    [InlineKeyboardButton('📝 Передати показники ', callback_data='submit_meter')]
])

meter = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('💧 Холодна вода', callback_data='water')],
    [InlineKeyboardButton('⚡️ Електроенергія', callback_data='electricity')],
    [InlineKeyboardButton('🔥 Опалення', callback_data='heating')],
    [InlineKeyboardButton(text='« Назад', callback_data='5555555')]
])

back_meters = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='« Назад', callback_data='submit_meter')]
    ])
