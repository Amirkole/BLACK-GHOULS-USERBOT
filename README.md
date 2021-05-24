
# BLACK GHOULS User Bot

![logo](https://telegra.ph/file/6e1201c7913ad1fa74d82.jpg)


[![Build Status](https://travis-ci.com/WolfGangIndia/WolfUserBot.svg?branch=sql-extended)](https://travis-ci.com/WolfGangIndia/WolfUserBot) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/38fee611df7c4312be63a15cad64a50a)](https://www.codacy.com/manual/WolfGangIndia/WolfUserBot?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=WolfGangIndia/WolfUserBot&amp;utm_campaign=Badge_Grade) ![Last Commit](https://img.shields.io/github/last-commit/WolfGangIndia/WolfUserBot) ![Contributers](https://img.shields.io/github/contributors/WolfGangIndia/WolfUserBot) ![Forks](https://img.shields.io/github/forks/WolfGangIndia/WolfUserBot)
<a href="https://deepsource.io/gh/WolfGangIndia/WolfUserBot/?ref=repository-badge" target="_blank"><img alt="DeepSource" title="DeepSource" src="https://static.deepsource.io/deepsource-badge-light-mini.svg"></a>

## What is it?

WolfUserBot is a modular Telegram userbot running on Python3, which can be coupled up with Heroku.

WolfUserBot is currently maintained by [Rajveer](https://t.me/Smart_S54) [Ï»Ê€ ð—¦á´„1¤7á´á´Êâ”ƒWá´ÊŸêœ°Gá´„1¤7É´É¢â”„1¤7 ðŸº ](https://t.me/Mr_Semmy). It started as a simple bot,

which helped with group management, [WolfUserBot](https://github.com/WolfGangIndia/WolfUserBot).

It has since evolved, becoming extremely modular and simple to use.

## How To Host?

The easiest way to deploy this great bot! is click on button below
Make sure you have an account of heroku and follow all the steps required.

Deploy to Heroku:
[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/WolfGangIndia/WolfUserBot)
<p align="center">
  <a href="https://github.com/WolfGangIndia/WolfUserBot/fork">
    <img src="https://img.shields.io/github/forks/WolfGangIndia/WolfUserBot?label=Fork&style=social">
    
  </a>
  <a href="https://github.com/WolfGangIndia/WolfUserBot">
    <img src="https://img.shields.io/github/stars/WolfGangIndia/WolfUserBot?style=social">
  </a>
</p>

### The Easy Way to deploy the bot
Get APP ID and API HASH from [HERE](https://my.telegram.org) and BOT TOKEN from [Bot Father](https://t.me/botfather) and then Generate stringsession by clicking on run.on.repl.it button below and then click on deploy to heroku . Before clicking on deploy to heroku just click on fork and star just below


[![opghoulsbot logo](https://telegra.ph/file/6e1201c7913ad1fa74d82.jpg)](https://heroku.com/deploy)


**Heroku Configuration**
Simply just leave the Config as it is.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`

    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org

- The userbot will not work without setting the mandatory vars.

```python3
from sample_config import Config
class Development(Config):
  APP_ID = 6
  API_HASH = "3eeb1aeb98ae0f581eeb06d4abfb49dc"
  TG_BOT_TOKEN_BF_HER = ""
  TG_BOT_USER_NAME_BF_HER = ""
  UB_BLACK_LIST_CHAT = []
  # specify LOAD and NO_LOAD
  LOAD = []
  NO_LOAD = []
```
## Groups and support

if you want new features, or announcements, you can follow our [Project Updates Channel](https://t.me/RkProjects).

For discussion, bug reporting, and help, you can join [WolfUserBot Support Group](https://t.me/Wolf_User_Bot).

## How to setup Google Drive
[![SetGDRIVE](https://telegra.ph/file/fde15d05e4bde3448b01a.png)](https://telegra.ph/How-To-Setup-Google-Drive-04-03)


```
#include <std/disclaimer.h>
/**
    Your Telegram account may get banned.
    I am not responsible for any improper use of this bot
    This bot is intended for the purpose of having fun with memes,
    as well as efficiently managing groups.
    You ended up spamming groups, getting reported left and right,
    and you ended up in a Finale Battle with Telegram and at the end
    Telegram Team deleted your account?
    And after that, then you pointed your fingers at us
    for getting your acoount deleted?
    I will be rolling on the floor laughing at you.
/**
```
### Credits

- [lonami](https://lonami.dev) for creating [Telethon](https://github.com/lonamiwebs/Telethon)
- [Telegram Userbot](https://github.com/RaphielGang/Telegram-UserBot)
- [Paperlane Extended](https://github.com/AvinashReddy3108/PaperplaneExtended)
- [Plus](https://github.com/amitsharma123234/Plus)
- [oub-remix](https://github.com/sahyam2019/oub-remix)
- [OpenUserBot](https://github.com/mkaraniya/OpenUserBot)
- [TG-UserBot](https://github.com/TG-UserBot/TG-UserBot)
- [X-tra-Telegram](https://github.com/Dark-Princ3/X-tra-Telegram)
- [catuserbot](https://github.com/sandy1709/catuserbot)
- [One4uBot](https://github.com/MoveAngel/One4uBot)

## License

This userbot licensed on [WolfGangIndia/WolfUserBot is licensed under the GNU General Public License v3.0](https://github.com/WolfGangIndia/WolfUserBot/blob/master/LICENSE) - Version 3, 29 June 2007
