import os
import _thread
import time
import discord
from discord.ext import commands
from dotenv import load_dotenv
import subprocess
import requests
import json
import re

server_ip = "9i0tcipxck3hneib.myfritz.net"
server_port = "1910"
url = f"https://api.mcsrvstat.us/2/{server_ip}:{server_port}"


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
#        _thread.start_new_thread(os.system, ('./securestart.sh',))
        time.sleep(10)
#        await channel.send('Der Server ist hochgefahren.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!h'):
        await message.channel.send('`!hi        ` = RasPi pingen.              \n`!hello     ` = Server pingen.                                                 \n`!start     ` = Startet den Minecraftserver.                                   \n`!stop      ` = Stoppt dem Minecraftserver (momentan ="!pause!").              \n`!pause     ` = Stoppt den Minecraftserver fährt den PC nicht runter.          \n`!status    ` = Zeigt den Status an.                                           \n`!wer       ` = Zeigt alle online Spieler\*innen an.                           \n`!mods      ` = Zeigt Mods an, die auf dem Server laufen.                      \n`!whitelist ` = Zeigt alle Spieler\*innen auf der Whitelist an.                \n`!kick name ` = Kickt "namen" vom Server.                                      \n`!stoftkick ` = Diskonnectet "namen" vom Server.                               \n`!render x y` = Rendert die Map um x y (die wird dann automatisch geupdated).')

    if message.content.startswith('!mods'):
        mods = os.listdir('/home/ubuntu/mnt/mods')
        await message.channel.send(f'{mods}')

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
#                await message.channel.send("Minecraft Server läuft.")
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    if data['online']:
                        await message.channel.send(f"Es sind {data['players']['online']} Leute online (!wer ist online).")
                    else:
                        await message.channel.send('Fährt grad hoch.')
                else:
                    await message.channel.send(f"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA: {response.status_code}")
            else:
                await message.channel.send("Minecraft Server ist heruntergefahren. !start um zu starten")
        except Exception as e:
            await message.channel.send(f"Ahh, sag nicht Rangi, dass: {e}")

    if message.content.startswith('!render'):
        result = subprocess.run(['screen', '-list'], stdout=subprocess.PIPE)
        if b'.minecraft' in result.stdout:
            parts = message.content.split()
            if len(parts) > 2:
                radius = 32
                x = parts[1]
                y = parts[2]
                if len(parts) == 4:
                    radius = parts[3]

                render_command = f"screen -S minecraft -X stuff 'dynmap radiusrender world {x} {y} {radius} \n'"
                _thread.start_new_thread(os.system, (render_command,))
                await message.channel.send(f'{int(radius)*int(radius)*4} Blöcke um {x} {y} rendern (dauert c.a. 7 min / 4096 Blöcke). (!cancelrender)')
            else:
                await message.channel.send('ERROR, versuch: !render [name].')
        else:
            await message.channel.send('Server ist aus.')

    if message.content.startswith('!cancelrender'):
        kick_command = f"screen -S minecraft -X stuff 'dynmap cancelrender world\n'"
        _thread.start_new_thread(os.system, (kick_command,))

            

    if message.content.startswith('!whitelist'):
        with open('whitelist.json', 'r') as file:
            data = json.load(file)
        for item in data:
            name = item['name']
            clean_name = re.sub(r'[^a-zA-Z]*$', '', name)
            await message.channel.send(f'{clean_name}')
            

    if message.content.startswith('!kick'):
        parts = message.content.split()
        if len(parts) > 1:
            username = parts[1]
            with open('whitelist.json', 'r') as file:
                data = json.load(file)

            data = [entry for entry in data if entry['name'] != username]
            with open('whitelist.json', 'w') as file:
                json.dump(data, file, indent=4)
            kick_command = f"screen -S minecraft -X stuff 'kick {username}\n'"
            _thread.start_new_thread(os.system, (kick_command,))
            kick_command = f"screen -S minecraft -X stuff 'whitelist reload\n'"
            _thread.start_new_thread(os.system, (kick_command,))
            await message.channel.send(f'{username} von der Whitelist entfernt.')
        else:
            await message.channel.send(f'ERROR, versuch: !kick [name].')

    if message.content.startswith('!softkick'):
        parts = message.content.split()
        if len(parts) > 1:
            username = parts[1]
            kick_command = f"screen -S minecraft -X stuff 'kick {username}\n'"
            _thread.start_new_thread(os.system, (kick_command,))

    if message.content.startswith('!wer'):
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['online']:
                if 'list' in data['players']:
                    for player in data['players']['list']:
                        await message.channel.send(player)
                else:
                    await message.channel.send("keiner")
            else:

                await message.channel.send('Server ist heruntergefahren, mit !start starten')
        else:
            await message.channel.send(f"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA: {response.status_code}")


    if message.content.startswith('!wwhitelistcommanddonttelleveryone'):
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
                    await message.channel.send('ERROR, versuch: !whitelistcommanddonttelleveryone [name].')
            else:
                await message.channel.send("Minecraft Server ist heruntergefahren.")
        except Exception as e:
            await message.channel.send(f"Ahh, sag nicht Rangi, dass: {e}")

    await bot.process_commands(message)

bot.run(TOKEN)
