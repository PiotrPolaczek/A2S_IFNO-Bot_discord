import time
import requests
import a2s
from discord import SyncWebhook

address = ("IP", PORT)

while True:
    try:
        response = a2s.info(address)

        if response:
            print("MESSENGER")
    except TimeoutError:
        webhook = SyncWebhook.from_url("webhook_url")
        webhook.send("Hello World")

    time.sleep(60)


