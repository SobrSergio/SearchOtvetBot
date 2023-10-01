from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

storage = MemoryStorage() #хранение памяти 
bot = Bot(token="") # Объект бота
dp = Dispatcher(bot, storage=storage) # Диспетчер

logging.basicConfig(level=logging.INFO) # Включаем логирование, чтобы не пропустить важные сообщения
