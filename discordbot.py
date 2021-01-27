from discord.ext import commands
import os
import traceback
from datetime import datetime, timedelta, timezone

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']




@bot.command()
async def w(ctx):
    JST = timezone(timedelta(hours=+9), 'JST') 
    now = datetime.now(JST).strftime('%H:%M')
    ms = ctx.author.name + "　[" + now + "]"    
    await ctx.send(ms)


bot.run(token)
