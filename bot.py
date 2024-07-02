import os
import _thread
import time
import discord
from discord.ext import commands
from dotenv import load_dotenv
import subprocess

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

if TOKEN is None:
    raise ValueError("No DISCORD_TOKEN found in the environment variables.")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

botspam = 806893179462090754 

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    channel = bot.get_channel(botspam)
    if channel is not None:
        _thread.start_new_thread(os.system, ('./securestart.sh',))
        time.sleep(10)
        await channel.send('Der Server ist hochgefahren.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!start'):
        try:
            result = subprocess.run(['screen', '-list'], stdout=subprocess.PIPE)
            if b'.minecraft' in result.stdout:
                await message.channel.send('Der Server ist schon oben.')
            else:
                await message.channel.send('Der Server wird gestartet.')
                await message.channel.send('IP: 9i0tcipxck3hneib.myfritz.net:1910')
                _thread.start_new_thread(os.system, ('./securestart.sh',))
                
        except Exception as e:
            await message.channel.send(f"Ahh, sag nicht Rangi, dass: {e}")

    if message.content.startswith('!stop'):
        try:
            result = subprocess.run(['screen', '-list'], stdout=subprocess.PIPE)
            if b'.minecraft' in result.stdout:
                await message.channel.send('Stopping minecraft server')
                _thread.start_new_thread(os.system, ('./stop.sh',))
            else:
                await message.channel.send("Minecraft Server ist schon aus.")
        except Exception as e:
            await message.channel.send(f"Ahh, sag nicht Rangi, dass: {e}")


    if message.content.startswith('!pause'):
        try:
            result = subprocess.run(['screen', '-list'], stdout=subprocess.PIPE)
            if b'.minecraft' in result.stdout:
                await message.channel.send('Stopping minecraft server')
                _thread.start_new_thread(os.system, ('./stop.sh',))
            else:
                await message.channel.send("Minecraft Server ist schon aus.")
        except Exception as e:
            await message.channel.send(f"Ahh, sag nicht Rangi, dass: {e}")

    if message.content.startswith('!status'):
        try:
            result = subprocess.run(['screen', '-list'], stdout=subprocess.PIPE)
            if b'.minecraft' in result.stdout:
                await message.channel.send("Minecraft Server läuft.")
            else:
                await message.channel.send("Minecraft Server ist heruntergefahren. !start um zu starten")
        except Exception as e:
            await message.channel.send(f"Ahh, sag nicht Rangi, dass: {e}")

    if message.content.startswith('!whitelistcommanddonttelleveryone'):
        try:
            result = subprocess.run(['screen', '-list'], stdout=subprocess.PIPE)
            if b'.minecraft' in result.stdout:
                parts = message.content.split()
                if len(parts) > 1:
                    username = parts[1]
                    whitelist_command = f"screen -S minecraft -X stuff 'whitelist add {username}\n'"
                    _thread.start_new_thread(os.system, (whitelist_command,))
                    await message.channel.send(f'{username} zur Whitelist geadded.')
                else:
                    await message.channel.send('Maan, du musst schon sagen, wer zur Whitelist hinzugefügt werden muss.')
            else:
                await message.channel.send("Minecraft Server ist heruntergefahren, du Teilzeitdenker.")
        except Exception as e:
            await message.channel.send(f"Ahh, sag nicht Rangi, dass: {e}")

    await bot.process_commands(message)

bot.run(TOKEN)
