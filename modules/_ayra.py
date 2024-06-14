# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.


from . import LOG_CHANNEL, Button, asst, ayra_cmd, eor, get_string

REPOMSG = """
◈ **˹ꭙ͢ᴅᴏᴋᴛ͢ᴇꝛ˼ ꭙ ᴜꜱᴇʀʙᴏᴛ​** ◈\n
◈ Repo - [Click Here](https://github.com/barcacoty2024/Naya-Userbot)
◈ Support - @Top_Mutualan_Indonesia
"""

RP_BUTTONS = [
    [
        Button.url(get_string("bot_3"), "https://github.com/barcacoty2024/Naya-Userbot"),
    ],
    [Button.url("Support Group", "t.me/Top_Mutualan_Indonesia")],
]

AYSTRING = """🎇 **Thanks for Deploying Dan-Userbot**

• Here, are the Some Basic stuff from, where you can Know, about its Usage."""


@ayra_cmd(pattern="Repo$")
async def useAyra(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        rs.chat_id,
        AYSTRING,
        file="https://graph.org/file/60408fea8439e6702674d.jpg",
        buttons=button,
    )
    if not (rs.chat_id == LOG_CHANNEL and rs.client._bot):
        await eor(rs, f"**[Click Here]({msg.message_link})**")
