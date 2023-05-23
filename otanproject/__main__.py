import importlib

from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from otanproject import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots
from otanproject.helpers.misc import create_botlog, git, heroku

MSG_ON = """
🥵 **OTAN-PYROBOT Berhasil Di Aktifkan**
━━
➠ **Userbot Version -** `{}`
➠ **Ketik** `{}alive` **untuk Mengecheck Bot**
━━
"""


async def main():
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("gbtnyaOtan")
            await bot.join_chat("cemarayeah")
            try:
                await bot.send_message(
                    BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER)
                )
            except BaseException:
                pass
            LOGGER("otanproject").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("otanproject").info(f"OTAN-PYROBOT v{BOT_VER} [🥵 BERHASIL DIAKTIFKAN! 🥵]")
    if bot1 and not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    if bot1 and str(BOTLOG_CHATID).startswith("-100"):
        bot1.me = await bot1.get_me()
        chat = await bot1.get_chat(BOTLOG_CHATID)
        desc = "Group Log untuk OTAN-PYROBOT.\n\nHARAP JANGAN KELUAR DARI GROUP INI.\n\n✨ Powered By ~ @gbtnyaOtan ✨"
        lolo = f"LOGS | FOR {bot1.me.first_name}"
        if chat.description != desc:
            await bot1.set_chat_description(BOTLOG_CHATID, desc)
        if chat.title != lolo:
            await bot1.set_chat_title(BOTLOG_CHATID, lolo)
        await bot1.set_chat_photo(BOTLOG_CHATID, photo="otanproject/resources/logo.jpg")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("otanproject").info("Starting OTAN-PYROBOT")
    install()
    git()
    heroku()
    LOOP.run_until_complete(main())
