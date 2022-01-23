import session, functions
from discord.ext import commands


class Info(commands.Cog):
    '''Информация о пользователе'''
    def __init__(self, client) -> None:
        self.client = client


    @commands.command()
    async def rate(self, ctx):
        '''Рейтинг'''
        author = ctx.message.author.name

        user = functions.find_user(author, session.all_users)
        await ctx.send(f'Рейтинг {user.name} = {user.rate}')
    

    @commands.command()
    async def money(self, ctx):
        '''Количество монет'''
        author = ctx.message.author.name

        user = functions.find_user(author, session.all_users)
        user.money = functions.to_two_digits(user.money)
        await ctx.send(f'У {user.name} {user.money} монет')


    @commands.command()
    async def days(self, ctx):
        '''Количество дней на сервере'''
        author = ctx.message.author.name

        user = functions.find_user(author, session.all_users)
        day = user.date_to_days()

        await ctx.send(f'{author} с нами {day} {user.get_days(day)}')


    @commands.command()
    async def info(self, ctx):
        '''Вся информация о себе'''
        author = ctx.message.author.name

        user = functions.find_user(author, session.all_users)
        await ctx.send(f'{user.user_info()}')


def setup(client):
    client.add_cog(Info(client))