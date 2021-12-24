import discord
import os
from discord.ext import commands
import asyncio 
import logging
import random 
from colorama import init
from colorama import Fore, Style
import requests
import json
import datetime
import random
import threading
import random
import time
import threading

init()
os.system("cls" or "clear")

token = input('{}\n[>] {} Twój TOKEN: {}'.format(Fore.RESET, Fore.LIGHTBLUE_EX, Fore.RESET))
prefix = input('{}\n[>] {} Twój PREFIX: {}'.format(Fore.RESET, Fore.LIGHTBLUE_EX, Fore.RESET))
client = commands.Bot(command_prefix=prefix, case_insensitive=True,
                      self_bot=True)

client.remove_command('help')
header = {"Authorization": f'Bot {token}'}
os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls' if os.name == 'nt' else 'clear')

intents = discord.Intents.all()
intents.members = True

@client.event
async def on_ready():
    print('\n{}=-=-=-=-=-=-{}=-=-=-=-=-=-{}=-=-=-=-=-=-{}=-=-=-=-=-=-{}\n'.format(Fore.RED, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.RESET))
    print('{}\n[{}»»»{}] {} Server Cloner włączony... {}'.format(Fore.RESET, Fore.YELLOW, Fore.RESET, Fore.MAGENTA, Fore.RESET))
    print('{}\n[{}»»»{}] {} Komenda:{} {}kopiuj {}\n'.format(Fore.RESET, Fore.YELLOW, Fore.RESET, Fore.MAGENTA, Fore.CYAN, prefix, Fore.RESET))
    print('     » {} Zalogowano jako: {} '.format(Fore.GREEN, Fore.CYAN) + client.user.name + '{}'.format(Fore.RESET))
    print('     » {} ID użytkownika: {} '.format(Fore.GREEN, Fore.CYAN) + str(client.user.id))
    print('\n{}=-=-=-=-=-=-{}=-=-=-=-=-=-{}=-=-=-=-=-=-{}=-=-=-=-=-=-{}\n'.format(Fore.RED, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.RESET))

@client.command()
async def kopiuj(ctx): 
    await ctx.message.delete()
    wow = await client.create_guild(f'Klon-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in client.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
            print(ctx.guild.roles)
    for role in ctx.guild.roles[::-1]:
        if role.name != "@everyone":
            try:
                await wow.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)
                print(f' Stworzono rolę : {role.name}')
            except:
                break

client.run(token, bot=False)
