from asyncio import events
from typing import AsyncContextManager
import discord
from discord import guild
from discord import member
from discord import client
from discord.ext import commands
from config import settings
from discord.guild import Guild
import session
import users_stats
import os


bot = commands.Bot(command_prefix = settings['prefix'])
Users = []

# Events
@bot.event
async def on_ready():
    print('Приветствую, Господин.')
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')
    print('Все модули загружены.')


@bot.event
async def on_member_join(member):
    print(f'{member} присоединился на сервер.')


@bot.event
async def on_member_remove(member):
    print(f'{member} покинул сервер.')


@bot.event
async def on_message(message):
    #print(f'{message.author}: {message.content}')
    new_author = True

    for obj in session.all_users:
        if obj.name == message.author.name:
            obj.count_messages += 1
            new_author = False
            break
    
    if new_author:
        # create new author with start stats
        new_user = users_stats.User(message.author.name)
        session.all_users.append(new_user)

    # так как on_message перекрывает все команды
    await bot.process_commands(message)

bot.run(settings['token'])