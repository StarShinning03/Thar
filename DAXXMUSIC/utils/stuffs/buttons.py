from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("Cʜᴀᴛɢᴘᴛ", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton("ɢʀᴏᴜᴘs", callback_data="mplus HELP_Group"),InlineKeyboardButton("sᴛɪᴄᴋᴇʀs", callback_data="mplus HELP_Sticker")],
    [InlineKeyboardButton("Tᴀɢ-Aʟʟ", callback_data="mplus HELP_TagAll"),
    InlineKeyboardButton("Iɴꜰᴏ", callback_data="mplus HELP_Info"),InlineKeyboardButton("Exᴛʀᴀ", callback_data="mplus HELP_Extra")],
    [InlineKeyboardButton("Iᴍᴀɢᴇ", callback_data="mplus HELP_Image"),
    InlineKeyboardButton("Aᴄᴛɪᴏɴ", callback_data="mplus HELP_Action"),InlineKeyboardButton("Sᴇᴀʀᴄʜ", callback_data="mplus HELP_Search")],    
    [InlineKeyboardButton("Fᴏɴᴛ", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("Gᴀᴍᴇs", callback_data="mplus HELP_Game"),InlineKeyboardButton("Ⓣ-ɢʀᴀᴘʜ", callback_data="mplus HELP_TG")],
    [InlineKeyboardButton("Iᴍᴘᴏsᴛᴇʀ", callback_data="mplus HELP_Imposter"),
    InlineKeyboardButton("Tʀᴜᴛʜ-Dᴀʀᴇ", callback_data="mplus HELP_TD"),InlineKeyboardButton("ʜᴀsᴛᴀɢ", callback_data="mplus HELP_HT")], 
    [InlineKeyboardButton("Tᴛs", callback_data="mplus HELP_TTS"),
    InlineKeyboardButton("Fᴜɴ", callback_data="mplus HELP_Fun"),InlineKeyboardButton("ǫᴜᴏᴛʟʏ", callback_data="mplus HELP_Q")],          
    [InlineKeyboardButton("◁", callback_data=f"settings_back_helper"), 
    InlineKeyboardButton("▷", callback_data=f"managebot123 settings_back_helper"),
    ]]
