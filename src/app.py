import discord
from discord.ext import commands
import json
import os

import colorama
colorama.init(autoreset=True)

import requests

import socket


def ping_server(host: str, port: int = 25565) -> bool:
    try:
        sock = socket.create_connection((host, port), timeout=5)
        sock.close()
        return True
    except (socket.timeout, socket.error):
        return False


def parseOnline():
    url = 'https://whiterise.su/'
    response = requests.get(url)
    return


script_dir = os.path.dirname(os.path.abspath(__file__))
token_path = os.path.join(script_dir, "token.json")


ip_keywords = ["какой ip", "какой айпи", "ip?", "какой айпишник"]
is_awake_keywords = ["какой онлайн", "серв офнули?", "серв"]

def parseToken():
    with open(token_path, "r", encoding="UTF-8") as temp:
      data = json.load(temp)
    return data['token']

 # replace with YOUR_TOKEN

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"{colorama.Fore.GREEN}Logged in as {colorama.Fore.WHITE}'{bot.user}' {colorama.Fore.GREEN}(ID: {bot.user.id})")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if any(keyword in message.content.lower() for keyword in ip_keywords):
        await message.reply("Айпи сервера:\n\t\tрусский айпи: `mc.whiterise.su`\n\t\tукраинский айпи: `eu.whiterise.su`\nОнлайн магазин: https://whiterise.su")

    elif any(keyword in message.content.lower() for keyword in is_awake_keywords):
        server_is_online_rus = ping_server("mc.whiterise.su")
        server_is_online_ua = ping_server("eu.whiterise.su")
        
        if server_is_online_ua:
            await message.reply(f"Сервер онлайн (eu.whiterise.su)") # , количество игроков на данный момент: {online_players}

        if server_is_online_rus:
            online_players = parseOnline()
            await message.reply(f"Сервер онлайн (mc.whiterise.su)") # , количество игроков на данный момент: {online_players}
             
        else:
            await message.reply("Сервер офлайн или не доступен.")

    else:
        print(f"{colorama.Fore.LIGHTRED_EX}{message.author}: {colorama.Fore.LIGHTYELLOW_EX}{message.content}")

if __name__ == "__main__":
    bot.run(TOKEN)

