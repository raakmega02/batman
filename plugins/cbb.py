#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Direct Mega Links😊😍 : <a href='https://t.me/+QPyHEA1xCVtlNTcx'>CLICK HERE⚡️</a>\n○ Daily Special Mega Links🥰: <a href='https://t.me/+SNSFScToH4piNTk1'>CLICK HERE⚡️</a>\n○ TeraBox 🎁 unlimited Links : <a href='https://t.me/+S7SN-3vnD1s4YjEx'>CLICK HERE⚡️</a>\n○ Special Leak Updates🔥 : <a href='https://t.me/+wxDSKyTwAMowZGFl'>CLICK HERE⚡️</a>\n○ Main Channel⚡️ : <a href='https://t.me/+kxI_UMH4ZxljODg1'>CLICK HERE⚡️</a>\n○ ❤️‍🩹Join Our All Stuff Channels in Single Click🔥 : https://t.me/addlist/RPm4cp5PE_Q5MzM1⚡️</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
