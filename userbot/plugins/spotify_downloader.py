""" Spotify / Deezer downloader plugin by @anubisxx | Syntax: .sdd link"""
import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserAlreadyParticipantError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from userbot.utils import admin_cmd

@borg.on(admin_cmd("sdd ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("` I need a link to download something pro.`**(._.)**")
    else:
        await event.edit("🎶**Initiating Download!**🎶")
    bot = "@DeezLoadBot"
    
    async with borg.conversation("@DeezLoadBot") as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              try:
                  await borg(ImportChatInviteRequest('AAAAAFZPuYvdW1A8mrT8Pg'))
              except UserAlreadyParticipantError:
                  await asyncio.sleep(0.00000069420)
              await conv.send_message(d_link)
              details = await conv.get_response()
              await borg.send_message(event.chat_id, details)
              await conv.get_response()
              songh = await conv.get_response()
              await borg.send_file(event.chat_id, songh, caption="🔆**Here's the requested song!**🔆")
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @DeezLoadBot `and retry!`")
              
@borg.on(admin_cmd(outgoing=True, pattern="spd(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@SpotifyMusicDownloaderBot"
    await event.edit("```Getting Your Music```")
    async with bot.conversation(chat) as conv:
          await asyncio.sleep(2)
          await event.edit("`Downloading music taking some times,  Stay Tuned.....`")
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=752979930))
              msg = await bot.send_message(chat, link)
              respond = await response
              res = conv.wait_event(events.NewMessage(incoming=True,from_users=752979930))
              r = await res
              """ - don't spam notif - """
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError:
              await event.reply("```Please unblock @SpotifyMusicDownloaderBot and try again```")
              return
          await bot.forward_messages(event.chat_id, respond.message)
    await event.client.delete_messages(conv.chat_id,
                                       [msg.id, r.id, respond.id])
    await event.delete()
