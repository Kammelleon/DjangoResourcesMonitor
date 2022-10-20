import json
from asyncio import sleep
from channels.generic.websocket import AsyncWebsocketConsumer
from ..database import Database


class GraphConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
        db = Database()
        while True:
            print("w petli")  # TODO: Zdefiniować wartości do wyslania na frontend
            await self.send(json.dumps({"wynik": "hello world"}))
            await sleep(1)