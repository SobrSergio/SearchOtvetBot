from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

storage = MemoryStorage() #хранение памяти 
bot = Bot(token="5682643007:AAE_AMWsw3kOxMrI3lF0uDlGhVKxSiJeHtc") # Объект бота
dp = Dispatcher(bot, storage=storage) # Диспетчер

logging.basicConfig(level=logging.INFO) # Включаем логирование, чтобы не пропустить важные сообщения