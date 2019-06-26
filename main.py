####################################################################
# GamerTools bot by Roilafufit
# Python 3.6.7
# Discord PyPI package, version 0.16.12 is required.
####################################################################

# Imports
import sys
try:
    import pkg_resources
    pkg_resources.require("discord.py==0.16.12")
except pkg_resources.VersionConflict:
    print("You have a wrong version of the discord.py package installed.")
    print("Please install version 0.16.12 of the discord.py package.")
    sys.exit("")
except pkg_resources.DistributionNotFound:
    print("You don't have the discord.py package installed.")
    print("Please install version 0.16.12 of the discord.py package.")
    sys.exit("")
from discord.ext import commands
from discord import Game


# Define some handy things for later
bot = commands.Bot(command_prefix='.')
token = ""  # I didn't write the bot token here for obvious reasons, but this is where it should be.
version = "1.0.0"
afk_list = []


bot.remove_command("help")


@bot.event
async def on_ready():
    await bot.change_presence(game=Game(name=".help", type=2))
    print("GamerTools bot by Roilafufit started successfully.")


@bot.event
async def on_message(msg):
    channel = msg.channel
    for userid in afk_list:  # This is for the AFK command
        if userid in msg.content:
            await bot.send_message(channel, (msg.server.get_member(user_id=userid).display_name + " is currently AFK."))
    await bot.process_commands(msg)


@bot.event
async def on_command_error(err, ctx):
    msg = ctx.message
    channel = msg.channel
    if type(err) == commands.errors.CommandNotFound:
        await bot.send_message(channel, "```diff\n-Error: Command not found\nType .help for a list of all available commands.```")
    elif type(err) == commands.errors.MissingRequiredArgument:
        await bot.send_message(channel, "```diff\n-Error: Missing required argument\nType .help to see all the required arguments for your desired command.```")
    else:
        await bot.send_message(channel, "```diff\n-Unknown command error\nPlease contact Roilafufit and send the following information:\nError description: " + str(err) + "\nError type: " + str(type(err)) + "```")


@bot.command(pass_context=True)
async def afk(ctx):
    author = ctx.message.author
    server = ctx.message.server
    user_not_already_afk = True
    for userid in afk_list:
        if userid == author.id:
            user_not_already_afk = False
            afk_list.pop(afk_list.index(userid))
            await bot.send_message(author, "You are no longer AFK.")
    if user_not_already_afk:
        afk_list.append(author.id)
        afk_vc = server.afk_channel
        if author.voice.voice_channel and afk_vc:
            await bot.move_member(author, afk_vc)
        await bot.send_message(author, "You are now AFK!")
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def game(ctx, gamename, amount):
    server = ctx.message.server
    author = ctx.message.author
    author_vc = author.voice.voice_channel
    try:
        int(amount)
    except ValueError:
        await bot.say("The amount of players you specified (" + amount + ") is invalid.")
    if author_vc:
        await bot.delete_message(ctx.message)
        broadcast_msg = await bot.say("**" + author.display_name + " is about to play** __**" + gamename + "**__**!\nWant to join? React using the :video_game: emoji below!**\n*If you are in a voice channel, you will automatically get moved into the* __*" + author_vc.name + "*__ *voice channel.\nIf your'e not in a voice channel, please join the* __*" + author_vc.name + "*__ *voice channel manually.* ")
        reaction_msg = await bot.say("**1 out of " + amount + " players joined**")
        await bot.add_reaction(reaction_msg, "ðŸŽ®")
        player_ids = [author.id]
        while int(amount) > len(player_ids):
            player_reaction = await bot.wait_for_reaction(emoji="ðŸŽ®", message=reaction_msg)
            for player in (await bot.get_reaction_users(player_reaction.reaction)):
                if (player.id not in player_ids) and (player.id != "592640446342365185"):
                    # 592640446342365185 is the ID of the bot, if I don't do what I did the bot will be added to the list seen as he reacted to the message.
                    player_ids.append(player.id)
                    await bot.edit_message(reaction_msg, ("**" + str(len(player_ids)) + " out of " + amount + " players joined**"))
                    # The above code won't break if people will remove the reaction and/or re-add it.
                    player_member = server.get_member(user_id=player.id)
                    if player_member.voice.voice_channel:
                        await bot.move_member(player_member, author_vc)
        player_names = ""
        for player in player_ids:
            if player_ids.index(player) == (len(player_ids) - 1):
                player_names = player_names + " and " + (server.get_member(user_id=player)).display_name
            elif player_ids.index(player) == (len(player_ids) - 2):
                player_names = player_names + (server.get_member(user_id=player)).display_name
            else:
                player_names = player_names + (server.get_member(user_id=player)).display_name + ", "
        # The if, elif, and else above are for the player_names string to look pleasant: with "," signs and the word "and" before the last player name.
        await bot.edit_message(broadcast_msg, ("**" + player_names + " are about to play** __**" + gamename + "**__"))
        await bot.edit_message(reaction_msg, "**Game is full!**")
        await bot.clear_reactions(reaction_msg)
    else:
        await bot.say("You must be in a voice channel to use this command!")


@bot.command(pass_context=True)
async def help(ctx):
    await bot.say("```.gamertools\nGeneral info about the bot.\n\n.afk\nToggle in and out of AFK. While AFK, if users tag you, the bot will tell them that your'e AFK. Also, if you're in a voice channel and you go AFK, you will get moved automatially to the server's AFK channel.\n\n.game '<name>' <amount of players>\nThe bot will broadcast in chat that you want to play a game, and users will be able to join it. (According to the amount of players that you set)```")


@bot.command(pass_context=True)
async def gamertools(ctx):
    await bot.say("GamerTools version " + version + " by Roilafufit\nSource code: https://github.com/Roilafufit/GamerTools\nType .help for a list of all available commands\n*Bot profile picture by Pettycon from Pixabay*")


bot.run(token)
