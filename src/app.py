import discord # важное
from discord.ext import commands # важное

import json # можно удалить 
import os # можно удалить 

import requests # работа с сетью, важное
import socket # раюота с сетью, важное

import colorama # для цветного вывода в консоль
colorama.init(autoreset=True)


def ping_server(host: str, port: int = 25565) -> bool: # проверка онлайн ли сервер
    try:
        sock = socket.create_connection((host, port), timeout=5)
        sock.close()
        return True
    except (socket.timeout, socket.error):
        return False


def parseOnline(): # не рабочая функцию по парсингу онлайна
    url = 'https://whiterise.su/'
    response = requests.get(url)
    return


script_dir = os.path.dirname(os.path.abspath(__file__)) # кривой фикс путя к моему json файлу, потому что у меня питон умственно отсталый
token_path = os.path.join(script_dir, "token.json") # это просто путь к файлу


ip_keywords = ["какой ip", "какой айпи", "ip?", "какой айпишник"] # сюда можно добавить слова на которые будет реагировать бот (это для айпишника)
is_awake_keywords = ["какой онлайн", "серв офнули?", "серв"] # это для пинга сервера

def parseToken(): # парсим токен из json 
    try:
        with open(token_path, "r", encoding="UTF-8") as temp:
           data = json.load(temp)
        return data['token']
    except:
        return None


intents = discord.Intents.default() # discord.py init
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents) #хуй знает зачем ему здесь префикс, но пусть будет

@bot.event
async def on_ready():
    print(f"{colorama.Fore.GREEN}Logged in as {colorama.Fore.WHITE}'{bot.user}' {colorama.Fore.GREEN}(ID: {bot.user.id})") # инит бота в консоли

@bot.event
async def on_message(message): # хендлер сообщений
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
    TOKEN = parseToken() # replace with YOUR_TOKEN
    bot.run(TOKEN)

