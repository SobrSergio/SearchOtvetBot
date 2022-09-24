from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType


# resize = уменьшение кнопки 
#главные кнопки для главного меню 
main_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(KeyboardButton('📸 Поиск по фото'), KeyboardButton('📝 Поиск по тексту')).add(KeyboardButton('🆘 Помощь'))

#кнопка назад для вызова главного меню 
back_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('🏡 Главное меню'))