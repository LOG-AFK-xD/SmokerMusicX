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
        caption=f"""**𝐓𝐡𝐢𝐬 𝐈𝐬 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 🥀𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐮𝐬𝐢𝐜 🎶 𝐁𝐨𝐭 𝐑𝐮𝐧 𝐎𝐧 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 🥀 𝐕𝐩𝐬 💫𝐒𝐞𝐫𝐯𝐞𝐫 🌎 𝐅𝐞𝐞𝐥 ❤️ 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐌𝐮𝐬𝐢𝐜 🎧 𝐈𝐧 𝐕𝐜 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 = [ᗩɴᴋɪᴛ & Ꮶʜᴜsʜɪ](t.me/ANKIT_SHUKLA_XD)

𝐂𝐫𝐞𝐚𝐭𝐨𝐫 :- [ᗩɴᴋɪᴛ & Ꮶʜᴜsʜɪ](t.me/KHUSHI_SHUKLA_XD)


𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐀𝐧𝐝 𝐇𝐞𝐥𝐩 𝐓𝐡𝐞𝐧 𝐃𝐦 𝐌𝐲 𝐁𝐨𝐬𝐬 = [ᗩɴᴋɪᴛ & Ꮶʜᴜsʜɪ](t.me/UNIQUE_SOCIETY)**""",
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("❣️ ᗩɴᴋɪᴛ", url=f"t.me/Ankit_shukla_xD"),
                InlineKeyboardButton("Ꮶʜᴜsʜɪ ❣️", url=f"t.me/khushi_shukla_xD"),
            ],
            [
                InlineKeyboardButton(
                    "🚑 Տᴜᴘᴘᴏʀᴛ", url=f"https://t.me/UNIQUE_SOCIETY"
                ),
                InlineKeyboardButton("Ⴎᴘᴅᴀᴛᴇs 📢", url=f"https://t.me/UNIQUE_LIFELINE"),
            ],
        ]
    )
