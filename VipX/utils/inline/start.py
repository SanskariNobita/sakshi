from typing import Union
import re
import os
from os import getenv

from dotenv import load_dotenv

from pyrogram import filters


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
load_dotenv()
YOUR_GROUP = getenv("YOUR_GROUP", "")
YOUR_CHANNEL = getenv("YOUR_CHANNEL", "")
OWNER_USERNAME = getenv("OWNER_USERNAME", "")

def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="💝 𝐀ԃԃ 𝐌ҽ 𝐁αႦყ 🍁",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🦋𝐅𝐄𝐀𝐓𝐔𝐑𝐄🦋",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="⚙️𝐒𝐄𝐓𝐓𝐈𝐍𝐆⚙️", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="💝 𝐀ԃԃ 𝐌ҽ 𝐁αႦყ 🍁",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="😎 𝐎ɯɳҽɾ 😎", url=f"https://t.me/{OWNER_USERNAME}",
            ),
            InlineKeyboardButton(
                text="🔰 𝐇ҽʅρ 🔰", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🎄𝐒υρρσɾƚ🎄", url=f"https://t.me/{YOUR_GROUP}",
            ),
            InlineKeyboardButton(
                text="😎 𝐔ρԃαƚҽʂ 😎", url=f"https://t.me/{YOUR_CHANNEL}",
            )
        ],
        [
            InlineKeyboardButton(
                text="🍁 𝐒ᴏᴜʀᴄᴇ 🍁",
                url=f"https://t.me/ABOUT_NOBITA_XD",
            )
        ],
     ]
    return buttons
