import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/55fdbedd3115d8c363d2f.jpg",
        caption=f"""**⛦➪ Tʜɪs Is Aᴅᴠᴀɴᴄᴇ Tᴇʟᴇɢʀᴀᴍ Mᴜsɪᴄ Bᴏᴛ Rᴜɴ Oɴ Pᴜʙʟɪᴄ Բʀᴇᴇ VPS Sᴇʀᴠᴇʀ Fᴇᴇʟ Hɪɢʜ Qᴜᴀʟɪᴛʏ Mᴜsɪᴄ Iɴ Vᴄ  Dᴇᴠᴇʟᴏᴘᴇᴅ Bʏ ➪ [ᗩɴᴋɪᴛ Ꮶʜᴜsʜɪ](t.me/UNIQUE_LIFELINE)

⛦➪ Ꮯʀᴇᴀᴛᴏʀ :- [ᗩɴᴋɪᴛ Ꮶʜᴜsʜɪ](t.me/KHUSHI_SHUKLA_XD)


⛦➪ Ꭻᴏɪɴ Ꮇʏ Ꮯʜᴀᴛᴛɪɴɢ Ꮐʀᴏᴜᴘ = [❣️ ᗩɴᴋɪᴛ Ꮶʜᴜsʜɪ ❣️](t.me/UNIQUE_SOCIETY)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌸 ᗩᴅᴅ ᗰᴇ Ꭹᴏᴜʀ Ꮐʀᴏᴜᴘ 🌸", url=f"t.me/khushi_robot?startgroup=true")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 Ꭻᴏɪɴ Ꮇʏ Ꮯʜᴀᴛᴛɪɴɢ Ꮐʀᴏᴜᴘ 💞", url=f"https://t.me/UNIQUE_SOCIETY")
                ]
            ]
        ),
    )
