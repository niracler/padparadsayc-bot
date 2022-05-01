import re
import os
import sys
import time
from telethon import TelegramClient, events, sync

import socks
import logging

logging.basicConfig(level=logging.DEBUG)

def get_env(name, message, cast=str):
    """Helper to get environment variables interactively"""
    if name in os.environ:
        return os.environ[name]
    while True:
        value = input(message)
        try:
            return cast(value)
        except ValueError as e:
            print(e, file=sys.stderr)
            time.sleep(1)

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
SESSION = os.environ.get('TG_SESSION', 'interactive')
API_ID = get_env('TG_API_ID', 'Enter your API ID: ', int)
API_HASH = get_env('TG_API_HASH', 'Enter your API hash: ')
PROXY = (socks.SOCKS5, '127.0.0.1', 1080)
client = TelegramClient(SESSION, API_ID, API_HASH, proxy=PROXY)

client.start()
channel_username = 'niracler_channel'  # your channel
for message in client.get_messages(channel_username, limit=50, reverse=False):
    # jsonStr = json.dumps(message.__dict__)
    if message.message and "#niracler的豆瓣动态" in message.message:
        # Reduce redundant line breaks and adjust the offse for the correct entity
        for entity in message.entities:
            if entity.offset == 0:
                continue
            if entity.offset > 0:
                entity.offset -= 1

        # client.edit_message(message, re.sub("[\n]+", "\n", message.message), formatting_entities=message.entities) 
        print(message)
        break
