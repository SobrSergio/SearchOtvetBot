from aiogram import types, Dispatcher
from create_bot import bot
from states.create_states import *
from aiogram.dispatcher import FSMContext
from functions.search_otvet import searchotvet
from functions.imagetotext import text_recognition
from keyboard.client_buttons import *
import os 


async def back_kb_image(message, state): #функция возращения в главное меню 
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) #удаление сообщения 🏡 Главное меню
    await bot.send_message(message.chat.id, '🏡 Вы вернулись в главное меню!', reply_markup=main_kb) #оповещение о возрате в меню
    await state.finish()
    
    
    
    
     
async def set_request_question(message: types.Message, state: FSMContext):
    
    if message.text == '🏡 Главное меню':  #возращения в главное меню 
        await back_kb_image(message, state)
        return
    

    await bot.send_message(message.chat.id, 'Подождите 🔄...')
    
    list_otvet = searchotvet(message.text) #переменная с 5 результатами поиска
    
    if len(list_otvet) < 5: 
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id + 1)
        await message.answer('❌ По вашему запросу ничего не найдено')
        
    else:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id + 1)
        await message.answer(f"""
Вот сайты с ответом на ваш запрос! ✉️
                             
<a href="{list_otvet[0]}">Ответ-1</a>

<a href="{list_otvet[1]}">Ответ-2</a>

<a href="{list_otvet[2]}">Ответ-3</a>

<a href="{list_otvet[3]}">Ответ-4</a>

<a href="{list_otvet[4]}">Ответ-5</a>
                         """, parse_mode='HTML', reply_markup=main_kb)
    await state.finish()





async def set_request_question_image(message: types.Message, state: FSMContext):
    if message.text == '🏡 Главное меню': #возращения в главное меню 
        await back_kb_image(message, state)
        return
    if not message.photo: 
        await bot.send_message(message.chat.id, 'Нужно отправить фотографию!')
    else:
        await bot.send_message(message.chat.id, 'Подождите 🔄...')
        file_info = await bot.get_file(message.photo[-1].file_id) #берем информацию о отправленном файле
        file_name = file_info.file_path.split('photos/')[1] #берем его имя
        await message.photo[-1].download(destination_file=f'image/{file_name}') #качаем файл в наш проект 
        
        file_text = text_recognition(f'image/{file_name}') #перевод изображения в текст (список)
        myString = ' '.join(file_text) #список в строку
        print(file_text) #----------------------------------------------------------------------------------------------------------------------------------------------
        list_otvet = searchotvet(myString) #переменная с 5 результатами поиска
        
        if len(list_otvet) < 5:
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id + 1)
            await bot.send_message(message.chat.id, '❌ По вашему запросу ничего не найдено')
            
        else:
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id + 1)
            await bot.send_message(message.chat.id, f"""                      
Вот сайты с ответом на ваш запрос! ✉️
                                    
<a href="{list_otvet[0]}">Ответ-1</a>

<a href="{list_otvet[1]}">Ответ-2</a>

<a href="{list_otvet[2]}">Ответ-3</a>

<a href="{list_otvet[3]}">Ответ-4</a>

<a href="{list_otvet[4]}">Ответ-5</a>""", parse_mode='HTML', reply_markup=main_kb)
            
        if(os.path.isfile(f"image/{file_name}")): #удаление изображения из проекта
            os.remove(f"image/{file_name}")
            
        await state.finish()






def register_states_client(dp: Dispatcher): #диспетчер
    
    dp.register_message_handler(set_request_question, state=RequestQuestion.text)
    dp.register_message_handler(set_request_question_image, state=RequestQuestion_image.image, content_types=['photo', 'text']) #content_types = что может принимать функция
    