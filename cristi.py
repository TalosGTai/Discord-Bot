from src.settings import settings
from disnake.ext import commands
import disnake
import os
from src.modules.users import User
from src.data.db_help_functional import create_user
from src.functions.embeds import embeds_welcome
from src.functions.main_func import delete_reverse_slash
from src.functions.discord import find_user


bot = commands.Bot(command_prefix=settings['prefix'],
                   intents=disnake.Intents().all())
                   # test_guilds=[settings['server']])


@bot.event
async def on_ready():
    print('Приветствую, Господин.')
    print('Загрузка модулей.')
    for filename in os.listdir('./src/cogs'):
        if filename.endswith('.py'):
            print(filename[:-3])
            bot.load_extension(f'src.cogs.{filename[:-3]}')
    bot.load_extension('src.bot.cogs.{actions}')
    print('Все модули загружены.')


@bot.event
async def on_member_join(member: disnake.Member):
    print(f'{member} присоединился на сервер.')

    member_name = delete_reverse_slash(member.name)
    if not(find_user(member_name)):
        new_user = User(member_name)
        create_user(new_user)

    await member.send(embeds=embeds_welcome(bot, member))

bot.run(settings['token'])
