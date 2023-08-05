from src.config import settings
from disnake.ext import commands
import os
import disnake
from src.modules.users import User
from src.data.db_help_functional import create_user
from src.functions.embeds import embeds_welcome
from src.functions.main_func import delete_reverse_slash
from src.functions.discord import find_user, add_user_count_msg


bot = commands.Bot(command_prefix=settings['prefix'],
                   intents=disnake.Intents().all(),
                   test_guilds=[settings['server']])


@bot.event
async def on_ready():
    print('Приветствую, Господин.')
    print('Загрузка модулей.')
    for filename in os.listdir('./src/cogs'):
        if filename.endswith('.py'):
            print(filename[:-3])
            bot.load_extension(f'src.cogs.{filename[:-3]}')
    print('Все модули загружены.')


@bot.event
async def on_member_join(member: disnake.Member):
    print(f'{member} присоединился на сервер.')

    member_name = delete_reverse_slash(member.name)
    if find_user(member_name) is None:
        new_user = User(member_name)
        create_user(new_user)

    role = member.mutual_guilds[0].get_role(848161737655058463)
    await member.send(embeds=embeds_welcome(bot, member))
    await member.add_roles(role)


@bot.event
async def on_member_remove(member: disnake.Member):
    print(f'{member} покинул сервер.')


@bot.event
async def on_command_error(ctx, error):
    print(error)

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author}, у тебя недостаточно прав для выполнения данной команды!')
    elif isinstance(error, commands.UserInputError):
        await ctx.send(f'Правильное использование команды:\n \'{ctx.prefix}{ctx.command.name}\'' +
                       f' ({ctx.command.brief})')


@bot.event
async def on_message(message):
    author = message.author.name
    author = delete_reverse_slash(author)
    new_user = find_user(author)

    if new_user:
        add_user_count_msg(author, 1)
    else:
        # create new author with start stats
        new_user = User(message.author.name)
        create_user(new_user)

    # так как on_message перекрывает все команды
    await bot.process_commands(message)


bot.run(settings['token'])