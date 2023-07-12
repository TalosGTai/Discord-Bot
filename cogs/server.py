from discord.ext import tasks
from disnake.ext import commands
import session, os, functions, disnake, db_functions
import datetime as DT
from git.repo import Repo


class Server(commands.Cog):
    '''Команды для управления'''

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.update_rate.start()
        self.save.start()
        self.git_update_auto.start()


    @tasks.loop(minutes=30.0)
    async def update_rate(self):
        '''Обновление всех рейтингов'''

        for user in session.all_users:
            user.update_rate()

        print('Обновлены все рейтинги.')


    @tasks.loop(minutes=30.0)
    async def save(self):
        '''Сохранение всей статистики'''

        db_functions.update_algo(session.all_users)
        minutes = functions.time_format(str(DT.datetime.now().minute))
        hours = functions.time_format(str(DT.datetime.now().hour))
        msg = f'{hours}:{minutes}: Все данные сохранены.'
        
        print(msg)


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def dina_save(self, ctx):
        '''Принудительное сохранение'''

        for user in session.all_users:
            user.update_rate()

        db_functions.update_algo(session.all_users)
        minutes = functions.time_format(str(DT.datetime.now().minute))
        hours = functions.time_format(str(DT.datetime.now().hour))
        msg = 'Обновлены все рейтинги.' + '\n'
        msg += f'{hours}:{minutes}: Все данные сохранены.'

        print(msg)
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load_all(self, ctx):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                try:
                    self.bot.load_extension(f'cogs.{filename[:-3]}')
                    print(f'Разрешение {filename[:-3]} успешно загружено.')
                except Exception:
                    print(f'Не удалось загрузить {filename[:-3]}.')
                self.bot.load_extension(f'cogs.{filename[:-3]}')
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, extension):
        try:
            self.bot.load_extension(f'cogs.{extension}')
            print(f'Разрешение {extension} успешно загружено.')
        except Exception:
            print(f'Не удалось загрузить {extension}.')
            print(Exception)
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, extension):
        try:
            self.bot.unload_extension(f'cogs.{extension}')
            self.bot.load_extension(f'cogs.{extension}')
            print(f'Разрешение {extension} успешно перезагружено.')
        except Exception:
            print(f'Не удалось перезагрузить {extension}.')
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, extension):
        try:
            self.bot.unload_extension(f'cogs.{extension}')
            print(f'Разрешение {extension} успешно выгружено.')
        except Exception:
            print(f'Не удалось выгрузить {extension}.')
        await ctx.message.delete()


    @tasks.loop(hours=12)
    async def git_update_auto(self):
        path = 'dina.py'
        repo = Repo(path, search_parent_directories=True)

        if repo.remote('origin').exists():
            repo.remote('origin').fetch()
            repo.remote('origin').pull()
            print('Загружена последняя версия.')
        else:
            print('Репозитория не существует.')


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def git_update(self, inter: disnake.ApplicationCommandInteraction):
        path = 'dina.py'
        repo = Repo(path, search_parent_directories=True)
        
        if repo.remote('origin').exists():
            repo.remote('origin').fetch()
            repo.remote('origin').pull()
            print('Загружена последняя версия.')
        else:
            print('Репозитория не существует.')


def setup(bot: commands.Bot):
    bot.add_cog(Server(bot))