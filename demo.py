from telethon import TelegramClient, events, sync

import socks
import logging
logging.basicConfig(level=logging.DEBUG)


# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = ""
api_hash = ""
client = TelegramClient(
    'anon', 
    api_id, api_hash, 
    proxy=(socks.SOCKS5, '127.0.0.1', 1080)
)

client.start()
channel_username = 'niracler_channel'# your channel
for message in client.get_messages(channel_username, limit=10):
    # client.edit_message(channel_username, message.id, message.message + '\n\nEdited by me')
    print(message.message)