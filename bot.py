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
antipaul = 0
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    channel = bot.get_channel(botspam)
    if channel is not None:
#        _thread.start_new_thread(os.system, ('./securestart.sh',))
        time.sleep(10)
#        await channel.send('Geupdatet')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!Hello'):
        await message.add_reaction('👋')

    if message.content.startswith('!antiPaulMaßnahmen'):
        global antipaul
        if antipaul == 4: await message.channel.send("Reicht auch mal, hab dich lieb 🧡.")
        if antipaul == 3: await message.channel.send("There is a high probability that League of Legends (LoL) players may commit war crimes due to the nature of the game. The competitive aspect of the game requires players to employ strategies and tactics that often result in team-killing, which could be seen as a form of war crime.\n\nIn addition, players can engage in cyberbullying or harassment during matches, which may lead them to commit real-life crimes. This is because they feel empowered by their in-game persona and do not think twice about engaging in such behavior due to the anonymity of online gaming.\n\nFurthermore, players may also be tempted to use cheat codes or other methods to gain an unfair advantage over other teams, which could lead them to commit war crimes if their team wins at all costs. This is because they feel justified in winning and taking what they think is rightfully theirs without regard for the consequences of their actions.\n\n In conclusion, while there is no direct correlation between LoL players and actual war criminals, the competitive nature of the game and the anonymity it provides can lead to negative behaviors that could potentially cross over into real-life crimes."); antipaul = 4
        if antipaul == 2: await message.channel.send("League of Legends players are not known for their social skills or their ability to maintain healthy relationships. In fact, many of them seem more interested in sitting around playing video games all day than they do in meeting new people or forming meaningful connections with others. This lack of socialization may be due in part to the fact that most League players are introverted and prefer solitude over socializing. \n\nWhen it comes to their sexuality, many League players appear to be virgins who struggle with relationships outside of video games. It seems as though they would rather spend countless hours playing a virtual game than actually going out on dates or pursuing real-life romances. This lack of experience in the dating world may make it difficult for them to navigate the complexities of human interactions, and their limited social skills can be a barrier to forming meaningful connections with others.\n\nOverall, League players appear to be socially awkward and unskilled when it comes to relationships outside of video games. Their inability to connect with others may stem from their lack of socialization and experience in the dating world, making them seem like lost souls who struggle to find meaningful connections in real life."); antipaul = 3
        if antipaul == 1: await message.channel.send("The League of Legends players are a bunch of whiners who can't take a little constructive criticism without getting their feelings hurt. They expect the world to revolve around them and their fragile egos, but when they lose, they blame everyone else for not playing at their level. These losers have no sense of sportsmanship or humility, and they act like petulant children when things don't go their way. \n\bIt's time to put these overgrown babies in their place. They should learn to take responsibility for their own actions and not blame others for their failures. If they can't handle losing graciously, they have no business playing a game that requires skill and strategy. \n\nLeague of Legends players need to grow up and stop acting like crybabies. They should be ashamed of themselves for bringing shame upon an otherwise great game by their childish behavior. The next time they play, they better remember that it's not about winning or losing - it's about playing the best you can with honor and integrity."); antipaul = 2
        if antipaul == 0: await message.channel.send("### A Examination of League of Legends Players\n\nLeague of Legends, a game that somehow attracts millions of players, is basically a refuge for the hopelessly frustrated. The community is a perfect example of people who can strategize to conquer a virtual world but can’t seem to figure out how to hold a decent conversation or get a date. If you're spending your nights here, it’s no wonder you're single—no one wants to date someone who thinks 'gg' is an acceptable form of communication.\n\n The infamous 'tilt' is practically a rite of passage. Watching players spiral into rage over a lost match is like witnessing a toddler throw a tantrum because they didn’t get their way. When things go south, it’s never their fault; it’s always the ‘noob’ ADC or the ‘feed’ jungler. It’s a masterclass in avoiding accountability and projecting failures onto others. Maybe if they spent half as much time working on their gameplay as they do blaming teammates, they might actually improve.\n"); await message.channel.send("These players are experts at self-delusion, convinced that their next game will magically change their rank while ignoring the fact that their biggest enemy is often themselves. It's hilarious—here they are, convinced they’re just one game away from glory, yet they can’t even muster the social skills to ask someone out. If only they channeled that passion into their personal lives, perhaps they wouldn’t be spending every weekend with their gaming chair as their only companion.\n\nAnd the chat? It’s a toxic wasteland where insults fly faster than the abilities in-game. Instead of strategizing, players unleash a torrent of garbage talk, thinking they’re clever. Newsflash: berating a stranger online doesn’t make you a hero; it just highlights your inability to engage with real people. Your summoner name won’t save you from the fact that you’re stuck in the friend zone while calling others ‘noobs.’\n\nIn reality, League of Legends is less about skill and more about the worst aspects of human nature. While it can foster teamwork, it more often cultivates toxicity and resentment. These players are so focused on climbing ranks that they forget how to interact with actual human beings, proving that their greatest challenge isn’t the game—it’s their own social ineptitude.\n\nSo, the next time you log in, remember: you’re not just playing a game; you’re participating in a never-ending cycle of self-sabotage. Enjoy being single while you chase that elusive victory in a world where real connections seem just as far out of reach."); antipaul = 1

    if message.content.startswith('!h'):
        await message.channel.send('`!Hi        ` = RasPi pingen.              \n`!Hello     ` = Server pingen.                                                 \n`!ip        ` = Zeigt Server-IP an.                                            \n`!map       ` = Link zur Dynmap.                                               \n`!start     ` = Startet den Minecraftserver.                                   \n`!stop      ` = Stoppt dem Minecraftserver (momentan ="!pause!").              \n`!pause     ` = Stoppt den Minecraftserver fährt den PC nicht runter.          \n`!status    ` = Zeigt den Status an.                                           \n`!wer       ` = Zeigt alle online Spieler\*innen an.                           \n`!mods      ` = Zeigt Mods an, die auf dem Server laufen.                      \n`!whitelist ` = Zeigt alle Spieler\*innen auf der Whitelist an.                \n`!kick name ` = Kickt "namen" vom Server.                                      \n`!ban name  ` = Bannt "namen" vom Server.                                      \n`!render x y` = Rendert die Map um x y (die wird dann automatisch geupdated).\n\n💤 = Server ist aus, mit `!start` starten.                                     \n🐨 = Spieler*in                                                                \n🚀 = Server Startet                                                            \n🙅 = Niemand online                                                            ')
    if message.content.startswith('!mods'):
        mods = os.listdir('/home/ubuntu/mnt/mods')
        await message.channel.send(f'{mods}')

    if message.content.startswith('!start'):
        try:
            result = subprocess.run(['screen', '-list'], stdout=subprocess.PIPE)
            if b'.minecraft' in result.stdout:
                await message.channel.send('Der Server ist schon oben.')
            else:
                await message.add_reaction('🚀')
                _thread.start_new_thread(os.system, ('./securestart.sh',))
                
        except Exception as e:
            await message.channel.send(f"Ahh, sag nicht Rangi, dass: {e}")

    if message.content.startswith('!ip'):
        await message.channel.send('9i0tcipxck3hneib.myfritz.net:1910')

    if message.content.startswith('!map'):
        await message.channel.send('http://9i0tcipxck3hneib.myfritz.net:1912')

    if message.content.startswith('!stop'):
        try:
            result = subprocess.run(['screen', '-list'], stdout=subprocess.PIPE)
            if b'.minecraft' in result.stdout:
                await message.add_reaction('🛑')
                _thread.start_new_thread(os.system, ('./stop.sh',))
            else:
                await message.add_reaction("💤")
        except Exception as e:
            await message.channel.send(f"Ahh, sag nicht Rangi, dass: {e}")


    if message.content.startswith('!pause'):
        try:
            result = subprocess.run(['screen', '-list'], stdout=subprocess.PIPE)
            if b'.minecraft' in result.stdout:
                await message.add_reaction('⏸️')
                _thread.start_new_thread(os.system, ('./stop.sh',))
            else:
                await message.add_reaction("💤")
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
                        playerCount=data['players']['online']
                        if playerCount == 0:
                            await message.channel.send(f"Es ist keiner online, mit `!stop` stoppen")
                        while playerCount > 0:
                            await message.add_reaction('🐨')
                            playerCount=playerCount-1
                    else:
                        await message.add_reaction('⏳')
                        await message.add_reaction('🚀')
                else:
                    await message.channel.send(f"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA: {response.status_code}")
            else:
                await message.add_reaction("💤")
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
            await message.add_reaction('💤')

    if message.content.startswith('!cancelrender'):
        await message.add_reaction('✅')
        kick_command = f"screen -S minecraft -X stuff 'dynmap cancelrender world\n'"
        _thread.start_new_thread(os.system, (kick_command,))

            

    if message.content.startswith('!whitelist'):
        with open('whitelist.json', 'r') as file:
            data = json.load(file)
        for item in data:
            name = item['name']
            clean_name = re.sub(r'[^a-zA-Z]*$', '', name)
            await message.channel.send(f'{clean_name}')
            

    if message.content.startswith('!ban'):
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
            await message.add_reaction('✅')
        else:
            await message.channel.send(f'ERROR, versuch: !ban [name].')

            
    if message.content.startswith('!kick'):
        parts = message.content.split()
        if len(parts) > 1:
            await message.add_reaction('✅')
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
                    await message.add_reaction("🙅")
            else:

                await message.add_reaction('💤')
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
                    await message.add_reaction('✅')
                else:
                    await message.channel.send('ERROR, versuch: !whitelistcommanddonttelleveryone [name].')
            else:
                await message.add_reaction("💤")
        except Exception as e:
            await message.channel.send(f"Ahh, sag nicht Rangi, dass: {e}")

    await bot.process_commands(message)

bot.run(TOKEN)
