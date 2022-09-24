from aiogram import types, Dispatcher
from create_bot import bot
from handlers import client
from aiogram.dispatcher.filters import Text
from keyboard.client_buttons import *
from states.create_states import *
from keyboard.client_inline_buttons import *


# last_msg = []

# async def Znanija_types(call: types.CallbackQuery):   
#     last_msg.append(call.data.split('_')[0])
#     res = call.data.split('_')[1]
#     await call.answer()
    
#     if res == 'foto':
#         await bot.edit_message_text(text='Отправьте фото с текстом задачи! 📪\n\
# Поиск по Znanija! ⚡️', chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=inl_back, parse_mode="HTML")
# #STATE

#     elif res == 'text':
#         await bot.edit_message_text(text='Отправьте текст задачи! 📪\n\
# Поиск по Znanija! ⚡️', chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=inl_back, parse_mode="HTML")
# #STATE




# async def Otvetmail_types(call: types.CallbackQuery):   
#     last_msg.append(call.data.split('_')[0])
#     res = call.data.split('_')[1]
#     await call.answer()
    
#     if res == 'foto':
#         await bot.edit_message_text(text='Отправьте фото с текстом задачи! 📪\n\
# Поиск по Otvet.mail! ⚡️', chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=inl_back, parse_mode="HTML")
# #STATE

#     elif res == 'text':
#         await bot.edit_message_text(text='Отправьте текст задачи! 📪\n\
# Поиск по Otvet.mail! ⚡️', chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=inl_back, parse_mode="HTML")
# #STATE





# async def back(call: types.CallbackQuery):
#     print('Кнопка сработала!')
#     await call.answer()
#     if last_msg[-1] == 'Znanija':
#         await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
#         await client.znanija_handler(call.message)
#     elif last_msg[-1] == 'Otvetmail':
#         await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
#         await client.otvetmail_handler(call.message)




# def register_call_handlers(dp: Dispatcher):
#     dp.register_callback_query_handler(Znanija_types, Text(startswith='Znanija_'))
#     dp.register_callback_query_handler(back, Text(startswith='back'))
#     dp.register_callback_query_handler( Otvetmail_types, Text(startswith='Otvetmail_'))