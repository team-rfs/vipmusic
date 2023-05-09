from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="☆ 𝗔𝗱𝗱 𝗠𝗲 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽  ☆",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ 𝐇𝐞𝐥𝐩 ✯",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="✯ 𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬 ✯", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="☆ 𝗔𝗱𝗱 𝗠𝗲 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽  ☆",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ 𝐎𝐰𝐧𝐞𝐫 ✯", user_id=OWNER
            ),
            InlineKeyboardButton(
                text="✯ 𝐇𝐞𝐥𝐩 ✯", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ 𝐆𝐫𝐨𝐮𝐩 ✯", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="✯ 𝗨𝗽𝗱𝗮𝘁𝗲𝘀 ✯", url=f"https://t.me/Katil_bots",
            )
        ],
        [
            InlineKeyboardButton(
                text="🌱ƨσʋяcɛ🌱",
                url=f"https://github.com/team-katil/zedzemusic",
            )
        ],
     ]
    return buttons
