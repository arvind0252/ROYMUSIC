from pyrogram.types import InlineKeyboardButton

import config
from DAXXMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["𝐒𝐔𝐌𝐌𝐎𝐍 𝐌𝐄"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["𝐒𝐔𝐌𝐌𝐎𝐍 𝐌𝐄"], url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["𝐎𝐖𝐍𝐄𝐑"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["𝐂𝐇𝐀𝐍𝐍𝐄𝐋"], url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text=_["𝐂𝐎𝐌𝐀𝐍𝐃𝐒"], callback_data="settings_back_helper"),
        ],
    ]
    return buttons
