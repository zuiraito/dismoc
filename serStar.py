import os
import _thread
import discord
from dotenv import load_dotenv
import subprocess
import RPi.GPIO as GPIO
import time

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

ip = '192.168.178.33'

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
time.sleep(1)
p.ChangeDutyCycle(0)

if TOKEN is None:
    raise ValueError("No DISCORD_TOKEN found in the environment variables.")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        await message.channel.send('!hello  = Selbsterklärend.\n!start  = Startet den Minecraftserver.\n!poweroff=Fährt den Server komplett runter\n!stop   = Stoppt dem Minecraftserver.\n!status= Zeigt den Status an.\n!mods  = Zeigt Mods an, die auf dem Server laufen.\n\nWhitelist kann jamand machen, der den Rank "whitelister" hat.')

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!hi'):
        await message.channel.send('hi!')

    if message.content.startswith('!mods'):
        await message.channel.send('c2me\nfabric-api\ncarpet\nferritecore\nlithium\nSimple Voice Chat')

    if message.content.startswith('!status'):
        result = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            await message.channel.send('Server ist heruntergefahren, mit !start starten')

    if message.content.startswith('!start'):
        result = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            await message.channel.send('Server wird hochgefahren...')
            time.sleep(0.5)
            p.ChangeDutyCycle(6)
            time.sleep(0.5)
            p.ChangeDutyCycle(2.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(0)
            await message.channel.send('...')
            time.sleep(5)

    if message.content.startswith('!stop'):
        result = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            time.sleep(30)
            await message.channel.send('Server wird heruntergefahren...')
            time.sleep(0.5)
            p.ChangeDutyCycle(6)
            time.sleep(0.5)
            p.ChangeDutyCycle(2.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(0)
            time.sleep(5)

client.run(TOKEN)
