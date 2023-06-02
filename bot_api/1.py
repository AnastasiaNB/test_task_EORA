import os

from dotenv import load_dotenv
from pyrogram import Client
from pyrogram.enums import parse_mode


load_dotenv()

app = Client(
    "qqq0q", api_id=os.getenv('API_ID'), api_hash=os.getenv('API_HASH')
)


async def main():
    await app.connect()
    code = await app.send_code(phone_number='+79251512979')
    code_hash = code.phone_code_hash
    phone_code = str(input())
    await app.sign_in(phone_number='+79251512979', phone_code_hash=code_hash, phone_code=phone_code)
    await app.send_message(
        chat_id='@EoraTaskBot',
        text='/start'
    )
    await app.disconnect()


app.run(main())