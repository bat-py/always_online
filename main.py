from telethon.sync import TelegramClient
from telethon import functions, types
import time

name = 'account'
api_id = 5193417
api_hash = '55909d877eef1f996884aee6734dddb9'

while True:
    time.sleep(2)
    with TelegramClient(name, api_id, api_hash) as client:
        result = client(functions.account.UpdateStatusRequest(
            offline=False
        ))
