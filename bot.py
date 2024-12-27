import os
import time

from telegram import Bot
from telegram.request import HTTPXRequest
from dotenv import load_dotenv
from devops_check_submodule.main import message

if __name__ == '__main__':
    load_dotenv()
    devops_test_bot_token = os.getenv("BOT_TOKEN")
    test_channel = os.getenv("CHANNEL_ID")
    t_request = HTTPXRequest(connection_pool_size=25)
    devops_test_bot = Bot(token=devops_test_bot_token, request=t_request)
    devops_test_bot.send_message(chat_id=test_channel,
                                 text="Get Message from submodule")
    time.sleep(1)
    try:
        devops_test_bot.send_message(chat_id=test_channel,
                                     text=message)
    except Exception as e:
        devops_test_bot.send_message(chat_id=test_channel,
                                     text=f"Couldn't get message from submodule - {e}")
