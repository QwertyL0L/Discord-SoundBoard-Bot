import asyncio
from discord.ext import commands
import discord
from discord import FFmpegPCMAudio
from gtts import gTTS

activity = discord.Activity(type=discord.ActivityType.playing, name="Gen Z Sounds")

bot = commands.Bot(command_prefix="k!",activity = activity,case_insensitive=True,intents=discord.Intents.all())
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f"Logged In As {bot.user.name}")

@bot.command(pass_context = True)
async def speak(ctx, *, text: str):
    language = 'en'
    myobj = gTTS(text=f'{text}', lang=language, slow=False)
    myobj.save("tts.mp3")
    source = FFmpegPCMAudio('tts.mp3')
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    player = voice.play(source)
    await ctx.reply("playing audio...")
    while voice.is_playing(): #Checks if voice is playing
        await asyncio.sleep(1) #While it's playing it sleeps for 1 second
    else:
        await asyncio.sleep(1) #If it's not playing it waits 1 second
    while voice.is_playing(): #and checks once again if the bot is not playing
        break #if it's playing it breaks
    else:
        await voice.disconnect() #if not it disconnects

@bot.command()
async def oof(ctx):
    source = FFmpegPCMAudio('C:/Users/paris/Downloads/soundboard_sounds/roblox-death-sound.mp3')
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    player = voice.play(source)
    await ctx.reply("**playing audio...**")
    while voice.is_playing(): #Checks if voice is playing
        await asyncio.sleep(1) #While it's playing it sleeps for 1 second
    else:
        await asyncio.sleep(1) #If it's not playing it waits 1 second
    while voice.is_playing(): #and checks once again if the bot is not playing
        break #if it's playing it breaks
    else:
        await voice.disconnect() #if not it disconnects
    while voice.is_playing(): #Checks if voice is playing
        await asyncio.sleep(1) #While it's playing it sleeps for 1 second
    else:
        await asyncio.sleep(1) #If it's not playing it waits 1 second
    while voice.is_playing(): #and checks once again if the bot is not playing
        break #if it's playing it breaks
    else:
        await voice.disconnect() #if not it disconnects

@bot.command()
async def funi(ctx):
    source = FFmpegPCMAudio('C:/Users/paris/Downloads/soundboard_sounds/rickroll.mp3')
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    player = voice.play(source)
    await ctx.reply("**playing audio...**")
    while voice.is_playing(): #Checks if voice is playing
        await asyncio.sleep(1) #While it's playing it sleeps for 1 second
    else:
        await asyncio.sleep(1) #If it's not playing it waits 1 second
    while voice.is_playing(): #and checks once again if the bot is not playing
        break #if it's playing it breaks
    else:
        await voice.disconnect() #if not it disconnects

@bot.command()
async def error(ctx):
    source = FFmpegPCMAudio('C:/Users/paris/Downloads/soundboard_sounds/winerror.mp3')
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    player = voice.play(source)
    await ctx.reply("**playing audio...**")
    while voice.is_playing(): #Checks if voice is playing
        await asyncio.sleep(1) #While it's playing it sleeps for 1 second
    else:
        await asyncio.sleep(1) #If it's not playing it waits 1 second
    while voice.is_playing(): #and checks once again if the bot is not playing
        break #if it's playing it breaks
    else:
        await voice.disconnect() #if not it disconnects


@bot.command()
async def wow(ctx):
    source = FFmpegPCMAudio('C:/Users/paris/Downloads/soundboard_sounds/anime-wow.mp3')
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    player = voice.play(source)
    await ctx.reply("**playing audio...**")
    while voice.is_playing(): #Checks if voice is playing
        await asyncio.sleep(1) #While it's playing it sleeps for 1 second
    else:
        await asyncio.sleep(1) #If it's not playing it waits 1 second
    while voice.is_playing(): #and checks once again if the bot is not playing
        break #if it's playing it breaks
    else:
        await voice.disconnect() #if not it disconnects


@bot.command()
async def pew(ctx):
    source = FFmpegPCMAudio('C:/Users/paris/Downloads/soundboard_sounds/pew.mp3')
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    player = voice.play(source)
    await ctx.reply("**playing audio...**")
    while voice.is_playing(): #Checks if voice is playing
        await asyncio.sleep(1) #While it's playing it sleeps for 1 second
    else:
        await asyncio.sleep(1) #If it's not playing it waits 1 second
    while voice.is_playing(): #and checks once again if the bot is not playing
        break #if it's playing it breaks
    else:
        await voice.disconnect() #if not it disconnects


@bot.command()
async def slowoof(ctx):
    source = FFmpegPCMAudio('C:/Users/paris/Downloads/soundboard_sounds/slowoof.mp3')
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    player = voice.play(source)
    await ctx.reply("**playing audio...**")
    while voice.is_playing(): #Checks if voice is playing
        await asyncio.sleep(1) #While it's playing it sleeps for 1 second
    else:
        await asyncio.sleep(1) #If it's not playing it waits 1 second
    while voice.is_playing(): #and checks once again if the bot is not playing
        break #if it's playing it breaks
    else:
        await voice.disconnect() #if not it disconnects


@bot.command()
async def loudoof(ctx):
    source = FFmpegPCMAudio('C:/Users/paris/Downloads/soundboard_sounds/loudoof.mp3')
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    player = voice.play(source)
    await ctx.reply("**playing audio...**")
    while voice.is_playing(): #Checks if voice is playing
        await asyncio.sleep(1) #While it's playing it sleeps for 1 second
    else:
        await asyncio.sleep(1) #If it's not playing it waits 1 second
    while voice.is_playing(): #and checks once again if the bot is not playing
        break #if it's playing it breaks
    else:
        await voice.disconnect() #if not it disconnects

@bot.command()
async def yeet(ctx):
    source = FFmpegPCMAudio('C:/Users/paris/Downloads/soundboard_sounds/yeet.mp3')
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    player = voice.play(source)
    await ctx.reply("**playing audio...**")
    while voice.is_playing(): #Checks if voice is playing
        await asyncio.sleep(1) #While it's playing it sleeps for 1 second
    else:
        await asyncio.sleep(1) #If it's not playing it waits 1 second
    while voice.is_playing(): #and checks once again if the bot is not playing
        break #if it's playing it breaks
    else:
        await voice.disconnect() #if not it disconnects

@bot.command()
async def vineboom(ctx):
    source = FFmpegPCMAudio('C:/Users/paris/Downloads/soundboard_sounds/vineboom.mp3')
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    player = voice.play(source)
    await ctx.reply("**playing audio...**")
    while voice.is_playing(): #Checks if voice is playing
        await asyncio.sleep(1) #While it's playing it sleeps for 1 second
    else:
        await asyncio.sleep(1) #If it's not playing it waits 1 second
    while voice.is_playing(): #and checks once again if the bot is not playing
        break #if it's playing it breaks
    else:
        await voice.disconnect() #if not it disconnects

@bot.command()
async def mario(ctx):
    source = FFmpegPCMAudio('C:/Users/paris/Downloads/soundboard_sounds/marioscream.mp3')
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    player = voice.play(source)
    await ctx.reply("**playing audio...**")
    while voice.is_playing(): #Checks if voice is playing
        await asyncio.sleep(1) #While it's playing it sleeps for 1 second
    else:
        await asyncio.sleep(1) #If it's not playing it waits 1 second
    while voice.is_playing(): #and checks once again if the bot is not playing
        break #if it's playing it breaks
    else:
        await voice.disconnect() #if not it disconnects

@bot.command()
async def minecraft(ctx):
    source = FFmpegPCMAudio('C:/Users/paris/Downloads/soundboard_sounds/minecraft_hit_sound.mp3')
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    player = voice.play(source)
    await ctx.reply("**playing audio...**")
    while voice.is_playing(): #Checks if voice is playing
        await asyncio.sleep(1) #While it's playing it sleeps for 1 second
    else:
        await asyncio.sleep(1) #If it's not playing it waits 1 second
    while voice.is_playing(): #and checks once again if the bot is not playing
        break #if it's playing it breaks
    else:
        await voice.disconnect() #if not it disconnects

@bot.command()
async def spongebobfail(ctx):
    source = FFmpegPCMAudio('C:/Users/paris/Downloads/soundboard_sounds/spongebob-fail.mp3')
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    player = voice.play(source)
    await ctx.reply("**playing audio...**")
    while voice.is_playing(): #Checks if voice is playing
        await asyncio.sleep(1) #While it's playing it sleeps for 1 second
    else:
        await asyncio.sleep(1) #If it's not playing it waits 1 second
    while voice.is_playing(): #and checks once again if the bot is not playing
        break #if it's playing it breaks
    else:
        await voice.disconnect() #if not it disconnects

@bot.command()
async def defaultdance(ctx):
    source = FFmpegPCMAudio('C:/Users/paris/Downloads/soundboard_sounds/default-dance-bass-boost.mp3')
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    player = voice.play(source)
    await ctx.reply("**playing audio...**")
    while voice.is_playing(): #Checks if voice is playing
        await asyncio.sleep(1) #While it's playing it sleeps for 1 second
    else:
        await asyncio.sleep(1) #If it's not playing it waits 1 second
    while voice.is_playing(): #and checks once again if the bot is not playing
        break #if it's playing it breaks
    else:
        await voice.disconnect() #if not it disconnects

@bot.command()
async def victorymusic(ctx):
    source = FFmpegPCMAudio('C:/Users/paris/Downloads/soundboard_sounds/victory_fanfare.mp3')
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    player = voice.play(source)
    await ctx.reply("**playing audio...**")
    while voice.is_playing(): #Checks if voice is playing
        await asyncio.sleep(1) #While it's playing it sleeps for 1 second
    else:
        await asyncio.sleep(1) #If it's not playing it waits 1 second
    while voice.is_playing(): #and checks once again if the bot is not playing
        break #if it's playing it breaks
    else:
        await voice.disconnect() #if not it disconnects

@bot.command()
async def trumpet(ctx):
    source = FFmpegPCMAudio('C:/Users/paris/Downloads/soundboard_sounds/trumpet.mp3')
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    player = voice.play(source)
    await ctx.reply("**playing audio...**")
    while voice.is_playing(): #Checks if voice is playing
        await asyncio.sleep(1) #While it's playing it sleeps for 1 second
    else:
        await asyncio.sleep(1) #If it's not playing it waits 1 second
    while voice.is_playing(): #and checks once again if the bot is not playing
        break #if it's playing it breaks
    else:
        await voice.disconnect() #if not it disconnects

@bot.command()
async def trolldrip(ctx):
    source = FFmpegPCMAudio('C:/Users/paris/Downloads/soundboard_sounds/trolldrip.mp3')
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    player = voice.play(source)
    await ctx.reply("**playing audio...**")
    while voice.is_playing(): #Checks if voice is playing
        await asyncio.sleep(1) #While it's playing it sleeps for 1 second
    else:
        await asyncio.sleep(1) #If it's not playing it waits 1 second
    while voice.is_playing(): #and checks once again if the bot is not playing
        break #if it's playing it breaks
    else:
        await voice.disconnect() #if not it disconnects

@bot.command()
async def help(ctx):
    embed = discord.Embed(color=0x0BA8B4, title="Basic Commands")
    embed.add_field(name="**k!speak**", value="***makes bot say your text in vc***", inline=False)
    embed.add_field(name="**k!oof**", value="***plays roblox oof sound***", inline=False)
    embed.add_field(name="**k!funi**", value="***plays a funi link***", inline=False)
    embed.add_field(name="**k!error**", value="***plays windows error sound***", inline=False)
    embed.add_field(name="**k!wow**", value="***plays wow sound***", inline=False)
    embed.add_field(name="**k!yeet**", value="***plays yeet sound***", inline=False)
    embed.add_field(name="**k!wow**", value="***plays wow sound***", inline=False)
    embed.add_field(name="**k!pew**", value="***plays pew sound***", inline=False)
    embed.add_field(name="**k!slowoof**", value="***plays slow oof sound***", inline=False)
    embed.add_field(name="**k!loudoof**", value="***plays loud oof sound***", inline=False)
    embed.add_field(name="**k!vineboom**", value="***plays vineboom sound***", inline=False)
    embed.add_field(name="**k!minecraft**", value="***plays minecraft hit sound***", inline=False)
    embed.add_field(name="**k!spongebobfail**", value="***plays spongebob fail sound***", inline=False)
    embed.add_field(name="**k!mario**", value="***plays mario screaming***", inline=False)
    embed.add_field(name="**k!defaultdance**", value="***plays bass boosted default dance***", inline=False)
    embed.add_field(name="**k!victorymusic**", value="***plays victory music***", inline=False)
    embed.add_field(name="**k!trumpet**", value="***plays trumpet***", inline=False)
    embed.add_field(name="**k!trolldrip**", value="***plays troll face drip***", inline=False)
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
     if isinstance(error, commands.CommandNotFound): 
         await ctx.reply("Invalid Command. Type **k!help** for a list of commands")

bot.run("TOKEN HERE")
