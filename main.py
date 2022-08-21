import discord
from discord.ext import commands
from keep_alive import keep_alive
import os

bot = commands.Bot(command_prefix='$', intents=discord.Intents().all())

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Weisman's Bots"))
    logChannel = bot.get_channel(906780579872272424)
    await logChannel.send("The Watcher is online.")

@bot.event
async def on_member_update(before, after):
    if before.bot:
        if before.status.name != after.status.name:
            logChannel = bot.get_channel(906780579872272424)
            await logChannel.send(f"{before.name} is {after.status.name}.")

keep_alive()
bot.run(os.getenv('Token'))