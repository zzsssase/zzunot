# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.

from telethon.errors import (
    BotMethodInvalidError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
)

from . import LOG_CHANNEL, LOGS, Button, asst, kazu_cmd, eor, get_string

REPOMSG = """
◈ **ʙʟᴀᴄᴋ ᴛʜᴏɴ​** ◈\n
◈ 𝘶𝘱𝘥𝘢𝘵𝘦𝘴 -  [ʙʟᴀᴄᴋ ᴛʜᴏɴ¹](t.me/FH_KN)
◈ 𝘶𝘱𝘥𝘢𝘵𝘦𝘴 -  [ʙʟᴀᴄᴋ ᴛʜᴏɴ²](t.me/FH_KP)
◈ 𝘶𝘱𝘥𝘢𝘵𝘦𝘴 - [ʙʟᴀᴄᴋ ᴛʜᴏɴ³](t.me/FH_KP)
"""

RP_BUTTONS = [
    [
        Button.url("𝘶𝘱𝘥𝘢𝘵𝘦𝘴", "https://t.me/FH_KN"),
    ],
    [Button.url("ᴜᴘᴅᴀᴛᴇs", "t.me/FH_KP")],
]

KAZUSTRING = """» **شڪرا لتنصيب بلاك ثون!**

◈ **اليك بعض الاشياء الاساسيه لمعرفة ڪيفبة الاستخدام**."""



@kazu_cmd(pattern="بلاك ثون$")
async def useAyra(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        KAZUSTRING,
        file="https://graph.org/file/d37e4a00d0779a80af603.jpg",
        buttons=button,
    )
    if not (rs.chat_id == LOG_CHANNEL and rs.client._bot):
        await eor(rs, f"**[Click Here]({msg.message_link})**")
