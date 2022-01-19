import session
from discord.ext import commands
import datetime as DT


class Info(commands.Cog):
    '''Информация о пользователе'''
    def __init__(self, client) -> None:
        self.client = client


    @commands.command()
    async def rate(self, ctx):
        '''Рейтинг'''
        author = ctx.message.author.name

        for user in session.all_users:
            if user.name == author:
                await ctx.send(f'Рейтинг пользователя {user.name} = {user.rate}')
                print(f'{author} запросил свой рейтинг.')
                break
    

    @commands.command()
    async def money(self, ctx):
        '''Количество монет'''
        author = ctx.message.author.name

        for user in session.all_users:
            if user.name == author:
                money = int(user.money * 100) / 100
                await ctx.send(f'Всего {money} монет')
                print(f'{author} запросил кол-во своих монет.')
                break


    @commands.command()
    async def days(self, ctx):
        '''Количество дней на сервере'''
        author = ctx.message.author.name

        for user in session.all_users:
            if user.name == author:
                d = user.live_server.split('-')
                dd = DT.date(int(d[0]), int(d[1]), int(d[2]))
                cur_date = (DT.date.today() - dd)
                day = int(cur_date.days)

                await ctx.send(f'{author} с нами {day} {user.get_days(day)}')
                print(f'{author} запросил количество дней на сервере.')
                break


    @commands.command()
    async def info(self, ctx):
        '''Вся информация о себе'''
        author = ctx.message.author.name

        for user in session.all_users:
            if user.name == author:
                await ctx.send(f'{user.user_info()}')
                print(f'{author} запросил инфо о себе.')
                break


def setup(client):
    client.add_cog(Info(client))