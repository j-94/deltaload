---
title: Quick-Start — Telethon 1.37.0 documentation
description: 
url: https://docs.telethon.dev/en/stable/basic/quick-start.html
timestamp: 2025-01-20T16:18:20.051Z
domain: docs.telethon.dev
path: en_stable_basic_quick-start.html
---

# Quick-Start — Telethon 1.37.0 documentation



## Content

Let’s see a longer example to learn some of the methods that the library has to offer. These are known as “friendly methods”, and you should always use these if possible.

from telethon import TelegramClient

\# Remember to use your own values from my.telegram.org!
api\_id \= 12345
api\_hash \= '0123456789abcdef0123456789abcdef'
client \= TelegramClient('anon', api\_id, api\_hash)

async def main():
    \# Getting information about yourself
    me \= await client.get\_me()

    \# "me" is a user object. You can pretty-print
    \# any Telegram object with the "stringify" method:
    print(me.stringify())

    \# When you print something, you see a representation of it.
    \# You can access all attributes of Telegram objects with
    \# the dot operator. For example, to get the username:
    username \= me.username
    print(username)
    print(me.phone)

    \# You can print all the dialogs/conversations that you are part of:
    async for dialog in client.iter\_dialogs():
        print(dialog.name, 'has ID', dialog.id)

    \# You can send messages to yourself...
    await client.send\_message('me', 'Hello, myself!')
    \# ...to some chat ID
    await client.send\_message(\-100123456, 'Hello, group!')
    \# ...to your contacts
    await client.send\_message('+34600123123', 'Hello, friend!')
    \# ...or even to any username
    await client.send\_message('username', 'Testing Telethon!')

    \# You can, of course, use markdown in your messages:
    message \= await client.send\_message(
        'me',
        'This message has \*\*bold\*\*, \`code\`, \_\_italics\_\_ and '
        'a \[nice website\](https://example.com)!',
        link\_preview\=False
    )

    \# Sending a message returns the sent message object, which you can use
    print(message.raw\_text)

    \# You can reply to messages directly if you have a message object
    await message.reply('Cool!')

    \# Or send files, songs, documents, albums...
    await client.send\_file('me', '/home/me/Pictures/holidays.jpg')

    \# You can print the message history of any chat:
    async for message in client.iter\_messages('me'):
        print(message.id, message.text)

        \# You can download media from messages, too!
        \# The method will return the path where the file was saved.
        if message.photo:
            path \= await message.download\_media()
            print('File saved to', path)  \# printed after download is done

with client:
    client.loop.run\_until\_complete(main())

Here, we show how to sign in, get information about yourself, send messages, files, getting chats, printing messages, and downloading files.

You should make sure that you understand what the code shown here does, take note on how methods are called and used and so on before proceeding. We will see all the available methods later on.

Important

Note that Telethon is an asynchronous library, and as such, you should get used to it and learn a bit of basic [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "(in Python v3.13)"). This will help a lot. As a quick start, this means you generally want to write all your code inside some `async def` like so:

client \= ...

async def do\_something(me):
    ...

async def main():
    \# Most of your code should go here.
    \# You can of course make and use your own async def (do\_something).
    \# They only need to be async if they need to await things.
    me \= await client.get\_me()
    await do\_something(me)

with client:
    client.loop.run\_until\_complete(main())

After you understand this, you may use the `telethon.sync` hack if you want do so (see [Compatibility and Convenience](https://docs.telethon.dev/en/stable/misc/compatibility-and-convenience.html#compatibility-and-convenience)), but note you may run into other issues (iPython, Anaconda, etc. have some issues with it).

## Metadata

```json
{
  "title": "Quick-Start — Telethon 1.37.0 documentation",
  "description": "",
  "url": "https://docs.telethon.dev/en/stable/basic/quick-start.html",
  "content": "Let’s see a longer example to learn some of the methods that the library has to offer. These are known as “friendly methods”, and you should always use these if possible.\n\nfrom telethon import TelegramClient\n\n\\# Remember to use your own values from my.telegram.org!\napi\\_id \\= 12345\napi\\_hash \\= '0123456789abcdef0123456789abcdef'\nclient \\= TelegramClient('anon', api\\_id, api\\_hash)\n\nasync def main():\n    \\# Getting information about yourself\n    me \\= await client.get\\_me()\n\n    \\# \"me\" is a user object. You can pretty-print\n    \\# any Telegram object with the \"stringify\" method:\n    print(me.stringify())\n\n    \\# When you print something, you see a representation of it.\n    \\# You can access all attributes of Telegram objects with\n    \\# the dot operator. For example, to get the username:\n    username \\= me.username\n    print(username)\n    print(me.phone)\n\n    \\# You can print all the dialogs/conversations that you are part of:\n    async for dialog in client.iter\\_dialogs():\n        print(dialog.name, 'has ID', dialog.id)\n\n    \\# You can send messages to yourself...\n    await client.send\\_message('me', 'Hello, myself!')\n    \\# ...to some chat ID\n    await client.send\\_message(\\-100123456, 'Hello, group!')\n    \\# ...to your contacts\n    await client.send\\_message('+34600123123', 'Hello, friend!')\n    \\# ...or even to any username\n    await client.send\\_message('username', 'Testing Telethon!')\n\n    \\# You can, of course, use markdown in your messages:\n    message \\= await client.send\\_message(\n        'me',\n        'This message has \\*\\*bold\\*\\*, \\`code\\`, \\_\\_italics\\_\\_ and '\n        'a \\[nice website\\](https://example.com)!',\n        link\\_preview\\=False\n    )\n\n    \\# Sending a message returns the sent message object, which you can use\n    print(message.raw\\_text)\n\n    \\# You can reply to messages directly if you have a message object\n    await message.reply('Cool!')\n\n    \\# Or send files, songs, documents, albums...\n    await client.send\\_file('me', '/home/me/Pictures/holidays.jpg')\n\n    \\# You can print the message history of any chat:\n    async for message in client.iter\\_messages('me'):\n        print(message.id, message.text)\n\n        \\# You can download media from messages, too!\n        \\# The method will return the path where the file was saved.\n        if message.photo:\n            path \\= await message.download\\_media()\n            print('File saved to', path)  \\# printed after download is done\n\nwith client:\n    client.loop.run\\_until\\_complete(main())\n\nHere, we show how to sign in, get information about yourself, send messages, files, getting chats, printing messages, and downloading files.\n\nYou should make sure that you understand what the code shown here does, take note on how methods are called and used and so on before proceeding. We will see all the available methods later on.\n\nImportant\n\nNote that Telethon is an asynchronous library, and as such, you should get used to it and learn a bit of basic [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio \"(in Python v3.13)\"). This will help a lot. As a quick start, this means you generally want to write all your code inside some `async def` like so:\n\nclient \\= ...\n\nasync def do\\_something(me):\n    ...\n\nasync def main():\n    \\# Most of your code should go here.\n    \\# You can of course make and use your own async def (do\\_something).\n    \\# They only need to be async if they need to await things.\n    me \\= await client.get\\_me()\n    await do\\_something(me)\n\nwith client:\n    client.loop.run\\_until\\_complete(main())\n\nAfter you understand this, you may use the `telethon.sync` hack if you want do so (see [Compatibility and Convenience](https://docs.telethon.dev/en/stable/misc/compatibility-and-convenience.html#compatibility-and-convenience)), but note you may run into other issues (iPython, Anaconda, etc. have some issues with it).",
  "usage": {
    "tokens": 937
  }
}
```
