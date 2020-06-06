# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# AnonymouserBot 
#

""" UserBot yardım komutu """

from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^.anonymous(?: |$)(.*)")
async def anonymous(event):
    """ .anonymous komutu için """
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("Lütfen bir AnonymouserBot modülü adı belirtin.")
    else:
        await event.edit("Lütfen hangi AnonymouserBot modülü için yardım istediğinizi belirtin !!\
            \nKullanım: .anonymous <modül adı>")
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\n"
        await event.reply(string)
