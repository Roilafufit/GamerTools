# GamerTools
A social Discord bot created for the Discord Hack Week competition.

### Features
##### .game command
The .game command makes the bot broadcast to the server that you want to play a game. Then, people will be able to join you by reacting to the message. You can set the amount of people for the game, so only a certain number of people will be able to join you. Players that join you will be asked to move to your voice channel, and the bot will even try to move them automatically when they join.


##### .afk command
When typing .afk, the bot now considers you as AFK. While AFK, if other people tag you, the bot will tell them that your'e AFK. If your'e in a voice channel while you use the .afk command, the bot will move you to the server's AFK voice channel (if the server has one). To go out of AFK mode, simply type .afk again.

### Technical Information
The bot was coded in Python 3.6 using the [discord.py](https://github.com/Rapptz/discord.py) package, version 0.16.12. [![discord.py version 0.16.12 on PyPI](https://img.shields.io/pypi/v/discord.py/0.16.12.svg)](https://pypi.org/project/discord.py/0.16.12/)

The bot might work in other Python versions, however, I did not test that.

It's important that the version of the discord.py package will be 0.16.12, newer versions have major changes that I'm not familliar enough with. (This is why I used version 0.16.12 although it's outdated)

### More Info
To invite the bot to your discord server: [https://discordapp.com/api/oauth2/authorize?client_id=592640446342365185&permissions=8&scope=bot](https://discordapp.com/api/oauth2/authorize?client_id=592640446342365185&permissions=8&scope=bot)

After the hack week competition ends, there's a chance that the bot will not be hosted anymore, it depends on my decision. However, I'm planning to keep this repository open. I'm NOT going to delete it, make it private or archive it.

### Credits
The bot's profile picture was made by [Pettycon](https://pixabay.com/users/Pettycon-3307648/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2389216) on [Pixabay](https://pixabay.com/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=2389216).
