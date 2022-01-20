import session
from discord.ext import commands


class Info(commands.Cog):
    '''Информация о пользователе'''
    def __init__(self, client) -> None:
        self.client = client


    @commands.command()
    async def rate(self, ctx):
        '''Рейтинг'''
        author = ctx.message.author.name

        user = session.find_user(author, session.all_users)
        await ctx.send(f'Рейтинг {user.name} = {user.rate}')
        print(f'{author} запросил свой рейтинг.')
    

    @commands.command()
    async def money(self, ctx):
        '''Количество монет'''
        author = ctx.message.author.name

        user = session.find_user(author, session.all_users)
        user.money_two_digits()
        await ctx.send(f'У {user.name} {user.money} монет')
        print(f'{author} запросил кол-во своих монет.')


    @commands.command()
    async def days(self, ctx):
        '''Количество дней на сервере'''
        author = ctx.message.author.name

        user = session.find_user(author, session.all_users)
        day = user.date_to_days()

        await ctx.send(f'{author} с нами {day} {user.get_days(day)}')
        print(f'{author} запросил количество дней на сервере.')


    @commands.command()
    async def info(self, ctx):
        '''Вся информация о себе'''
        author = ctx.message.author.name

        user = session.find_user(author, session.all_users)
        await ctx.send(f'{user.user_info()}')
        print(f'{author} запросил инфо о себе.')


def setup(client):
    client.add_cog(Info(client))
