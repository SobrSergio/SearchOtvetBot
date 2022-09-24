from aiogram import types, Dispatcher
from create_bot import bot
from keyboard.client_buttons import *
from states.create_states import *
from keyboard.client_inline_buttons import *



async def default_commands(message: types.Message): #стандартные команды
    if message.text == '/start':
        await bot.send_message(message.chat.id, f"""Привет, {message.from_user.full_name}!
🤖SearchOtvetBot  -  Уникальный бот, который позволяет искать ответы по всему интернету по фото или тексту! 

Нажмите на одну из этих кнопок👇:
        
📸 Поиск по фото  -  отправьте изображение боту и получите ответ на вашу задачу! Поиск будет выполнен по всему интернету.

📝 Поиск по тексту  -  отправьте текст боту и получите ответ на вашу задачу! Поиск будет выполнен по всему интернету.


Обратная связь: @SergeyManakhimov
(Для других контактов:  🆘 Помощь)""", parse_mode='HTML', reply_markup=main_kb)





async def main_kb_handler(message: types.Message): #основная клавиатура
    
    if message.text == '📸 Поиск по фото':
        await bot.send_message(message.chat.id, """Отправьте фото с текстом задачи! 📪
                               
Чем качественнее фото, тем лучше будет результат""", reply_markup=back_kb)
        await RequestQuestion_image.image.set()
        
        
    if message.text == '📝 Поиск по тексту':
        await bot.send_message(message.chat.id, """Отправьте текст задачи! 📪
                               
Пример:  В треугольнике ABC угол C равен 90°, AC = 4,8, sinA = 7/25, Найдите AB""", reply_markup=back_kb)
        
        await RequestQuestion.text.set()
        
        
    if message.text == '🆘 Помощь':
        await bot.send_message(message.chat.id, """
Все контакты для обратной связи🧑‍💻:

Telegram - @SergeyManakhimov,
Email - sergeymanakhimov@gmail.com
Instagram - @sergey_manakhimov""")


# async def znanija_handler(message: types.Message):
#     await bot.send_message(message.chat.id, """⚡️ Znanija
# Выберите способ поиска ответов""", reply_markup=Znanija_frame) 



# async def otvetmail_handler(message: types.Message):
#         await bot.send_message(message.chat.id, """📧 Otvet.mail
# Выберите способ поиска ответов""", reply_markup=Otvetmail_frame) 




def register_message(dp: Dispatcher):  #регистрация всех хэндлеров
    
    dp.register_message_handler(default_commands, commands=['start', 'help'])
    
    dp.register_message_handler(main_kb_handler, lambda message: (message.text == '📸 Поиск по фото' or message.text == '📝 Поиск по тексту' or message.text == '🆘 Помощь'), state = None)
    
    # dp.register_message_handler(znanija_handler, lambda message: (message.text == '⚡️ Znanija'))
    
    # dp.register_message_handler(otvetmail_handler, lambda message: (message.text == '📧 Otvet.mail'))