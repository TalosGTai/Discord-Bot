from discord.ext import tasks
from disnake.ext import commands
import os, disnake
from git.repo import Repo


class Server(commands.Cog):
    '''Команды для управления'''

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.git_update_auto.start()


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load_all(self, ctx):
        for filename in os.listdir('./Discord/cogs'):
            if filename.endswith('.py'):
                try:
                    self.bot.load_extension(
                        f'Discord.src.cogs.{filename[:-3]}')
                    print(f'Разрешение {filename[:-3]} успешно загружено.')
                except Exception as ex:
                    print(f'Не удалось загрузить {filename[:-3]}.', ex)
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, extension):
        try:
            self.bot.load_extension(
                f'src.cogs.{extension}')
            print(f'Разрешение {extension} успешно загружено.')
        except Exception as ex:
            print(f'Не удалось загрузить {extension}.', ex)
            print(Exception)
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, extension):
        try:
            self.bot.unload_extension(
                f'src.cogs.{extension}')
            self.bot.load_extension(
                f'src.cogs.{extension}')
            print(f'Разрешение {extension} успешно перезагружено.')
        except Exception as ex:
            print(f'Не удалось перезагрузить {extension}.', ex)
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, extension):
        try:
            self.bot.unload_extension(
                f'src.cogs.{extension}')
            print(f'Разрешение {extension} успешно выгружено.')
        except Exception as ex:
            print(f'Не удалось выгрузить {extension}.', ex)
        await ctx.message.delete()


    @tasks.loop(hours=12)
    async def git_update_auto(self):
        path = f'dina.py'
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
        path = f'dina.py'
        repo = Repo(path, search_parent_directories=True)
        
        if repo.remote('origin').exists():
            repo.remote('origin').fetch()
            repo.remote('origin').pull()
            print('Загружена последняя версия.')
        else:
            print('Репозитория не существует.')


def setup(bot: commands.Bot):
    bot.add_cog(Server(bot))