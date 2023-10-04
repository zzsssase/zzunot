# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.

import re

from . import *

STRINGS = {
    1: """ **شڪرا لتنصيب بلاك ثون**

◈ اليك بعض الاشباء الاساسيه لمعرفة ڪيفيه الاستخدام.""",
    2: """◈** ʙʟᴀᴄᴋ ᴛʜᴏɴ**
السـورس يحتوي الا مميزات عديده اڪتسفها بنفسك 😂...

~ 𝘤𝘳𝘦𝘢𝘵𝘦𝘥 𝘣𝘺 **@FH_ME**""",
    3: """**𝘶𝘱𝘥𝘢𝘵𝘦𝘴**

◈ 𝘶𝘱𝘥𝘢𝘵𝘦𝘴 -  [ʙʟᴀᴄᴋ ᴛʜᴏɴ¹](t.me/FH_KN)
◈ 𝘶𝘱𝘥𝘢𝘵𝘦𝘴 -  [ʙʟᴀᴄᴋ ᴛʜᴏɴ²](t.me/FH_KP)
◈ 𝘶𝘱𝘥𝘢𝘵𝘦𝘴 - [ʙʟᴀᴄᴋ ᴛʜᴏɴ³](t.me/FH_KP)
.""",
    4: f"""◈ **لمعرفة ڪافة الاوامـر اڪتب**

  - `{HNDLR}الاوامر`""",
    5: """• **اي استفسار او اقتراح **
  - انضم **[ʙʟᴀᴄᴋ ᴛʜᴏɴ](t.me/FH_KP)**.""",
}


@callback(re.compile("initft_(\\d+)"))
async def init_depl(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 5:
        return await e.edit(
            STRINGS[5],
            buttons=Button.inline("<< Back", "initbk_4"),
            link_preview=False,
        )

    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("السابق", f"initbk_{str(CURRENT - 1)}"),
            Button.inline("التالي", f"initft_{str(CURRENT + 1)}"),
        ],
        link_preview=False,
    )


@callback(re.compile("initbk_(\\d+)"))
async def ineiq(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 1:
        return await e.edit(
            STRINGS[1],
            buttons=Button.inline("Start Back >>", "initft_2"),
            link_preview=False,
        )

    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", f"initbk_{str(CURRENT - 1)}"),
            Button.inline(">>", f"initft_{str(CURRENT + 1)}"),
        ],
        link_preview=False,
    )
