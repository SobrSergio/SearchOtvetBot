from create_bot import dp, bot
from aiogram.utils import executor
import asyncio
from handlers import client, client_callbackes
from states import states
import torch

print(torch.cuda.is_available())

client.register_message(dp)
states.register_states_client(dp)
# client_callbackes.register_call_handlers(dp)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    