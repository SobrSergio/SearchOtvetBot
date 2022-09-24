from aiogram.dispatcher.filters.state import StatesGroup, State





class RequestQuestion(StatesGroup): #поиск по тексту
    text = State()


class RequestQuestion_image(StatesGroup): #поиск по картинке 
    image = State()
    
