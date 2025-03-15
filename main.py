from telethon import TelegramClient
from os import path
from telethon.tl.types import PeerUser
from typing import Optional
import asyncio
import logging


logging.basicConfig(filename="log.txt", filemode="a",format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


config = {
    "apiID": 123,
    "apiHash": "",
    "botToken": "",
    "directory": r"./log.txt", 
    "adminUserId": 2056493966,
}


async def main() -> None:

    client = TelegramClient(
        session="bot",
        api_id=config["apiID"],
        api_hash=config["apiHash"]
    )
    
    await client.start(bot_token=config["botToken"]) 
    
    if not check_file():
        print("File does not exist.")
        return
        
    try:
        await client.send_file(PeerUser(config["adminUserId"]), config["directory"], caption='with love ⚡️')
        print("File sent successfully.")
    except Exception as ex:
        print(f"An error occurred: {ex}")
    finally:
        await client.disconnect()

def check_file(dir: Optional[str] = config.get('directory', None)) -> bool:
    
    return (dir and path.exists(dir))

if __name__ == "__main__":
    asyncio.run(main())
