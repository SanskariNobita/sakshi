from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from VipX import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@app.on_message(
    filters.command("owner")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/d1ffe1f9581591beea3d7.jpg",
        caption=f"""➳ 𝐂ℓι¢к 𝐓ᴏ 𝐎ɯɳҽɾ's 𝐃ᴍ ✰""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⏤͟͞<♦️𓆩|• 𝐒 𝐀 𝐍 𝐒 𝐊 𝐀 𝐑 𝐈 ꭙ 𝐁 𝐎 𝐘 •|𓆪🍁", url=f"https://t.me/Teri_gf_mere_phan")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("owner")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/d1ffe1f9581591beea3d7.jpg",
        caption=f"""➳ 𝐂ℓι¢к 𝐓ᴏ 𝐎ɯɳҽɾ's 𝐃ᴍ ✰""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⏤͟͞<♦️𓆩|• 𝐒 𝐀 𝐍 𝐒 𝐊 𝐀 𝐑 𝐈 ꭙ 𝐁 𝐎 𝐘 •|𓆪🍁", url=f"https://t.me/Teri_gf_mere_phan")
                ]
            ]
        ),
    )






@app.on_message(
    filters.command("repo")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/d1ffe1f9581591beea3d7.jpg",
        caption=f"""➳ 𝐂ℓι¢к 𝐓ᴏ 𝐎ɯɳҽɾ's 𝐃ᴍ ✰""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍁 𝐒ᴏᴜʀᴄᴇ 🍁", url=f"https://t.me/ABOUT_NOBITA_XD")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("source")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/d1ffe1f9581591beea3d7.jpg",
        caption=f"""➳ 𝐂ℓι¢к 𝐓ᴏ 𝐎ɯɳҽɾ's 𝐃ᴍ ✰""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍁 𝐒ᴏᴜʀᴄᴇ 🍁", url=f"https://t.me/ABOUT_NOBITA_XD")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/d1ffe1f9581591beea3d7.jpg",
        caption=f"""➳ 𝐂ℓι¢к 𝐓ᴏ 𝐎ɯɳҽɾ's 𝐃ᴍ ✰""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍁 𝐒ᴏᴜʀᴄᴇ 🍁", url=f"https://t.me/ABOUT_NOBITA_XD")
                ]
            ]
        ),
    )

