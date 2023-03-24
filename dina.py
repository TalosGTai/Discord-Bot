from asyncio import events, TimeoutError
from config import settings
from disnake.ext import commands
import os, disnake
import session, functions, users_stats, db_functions
from functions import embed_reason


bot = commands.Bot(command_prefix=settings['prefix'], \
                   intents=disnake.Intents().all(), \
                    test_guilds=[settings['server']])


@bot.event
async def on_ready():
    print('Приветствую, Господин.')
    print('Загрузка модулей.')
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            print(filename[:-3])
            bot.load_extension(f'cogs.{filename[:-3]}')
    print('Все модули загружены.')


@bot.event
async def on_member_join(member: disnake.Member):
    print(f'{member} присоединился на сервер.')

    role = member.mutual_guilds[0].get_role(848161737655058463)
    await member.add_roles(role)
    

@bot.event
async def on_member_remove(member: disnake.Member):
    print(f'{member} покинул сервер.')
    await member.send(embed=embed_reason(str(member)))

    try:
        msg = await bot.wait_for('message', check=check, timeout=600)
    except TimeoutError:
        return await member.send('время вышло')


@bot.event
async def on_command_error(ctx, error):
    print(error)

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author}, у тебя недостаточно прав для выполнения данной команды!')
    elif isinstance(error, commands.UserInputError):
        await ctx.send(f'Правильное использование команды:\n \'{ctx.prefix}{ctx.command.name}\'' + \
            f' ({ctx.command.brief})')


@bot.event
async def on_message(message):
    author = message.author.name
    author = functions.delete_reverse_slash(author)
    new_user = functions.find_user(author, session.all_users)
    
    if new_user:
        new_user.count_messages += 1
    else:
        # create new author with start stats
        new_user = users_stats.User(message.author.name)
        session.all_users.append(new_user)
        db_functions.create_user(new_user)

    # так как on_message перекрывает все команды
    await bot.process_commands(message)


bot.run(settings['token'])
