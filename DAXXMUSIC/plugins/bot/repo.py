from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME

start_txt = """
✦ ʜᴇʏ ᴛʜᴇʀᴇ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ !

❅ ɪ ᴀᴍ ๛𝗠𝗔𝗡𝗡𝗨𝗠𝗨𝗦𝗜𝗖 ༗ ᴍ ᴜ s ɪ ᴄ

❅ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ๛𝗠𝗔𝗡𝗡𝗨𝗠𝗨𝗦𝗜𝗖 ༗ ʙᴏᴛ ʀᴇᴘᴏ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/monstarlove"),
          InlineKeyboardButton("ʀᴇᴘᴏ", url="https://t.me/monstarqueen"),
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/8bc05d47bec1beaa095b6.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
