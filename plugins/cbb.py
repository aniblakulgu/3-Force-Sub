#(©)Codeflix-Bots

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>𓆰𝒀𝒖𝒖𝒊𝒄𝒉𝒊~𝑺𝒂𝒎𝒂𓂀</a>\n○ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href='https://t.me/Coco_ShareBot?start=Z2V0LTEwNzgyNjgyNjU4MzI4NDg'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n○ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/Animes_vq'>ᴀɴɪᴍᴇ ᴜɴɪᴛʏ</a>\n○ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href='https://t.me/THE_VANQUISHERS'>ᴛʜᴇ ᴠᴀɴϙᴜɪsʜᴇʀs</a>\n○ ᴀɴɪᴍᴇ ᴄʜᴀᴛ : <a href='https://t.me/weebsunity'>ᴡᴇᴇʙs ᴜɴɪᴛʏ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ᴅᴏɴᴀᴛᴇ ᴜs', url='https://t.me/THE_VANQUISHERS/28')
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
