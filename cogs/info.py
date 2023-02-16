import session, functions
from disnake.ext import commands


class Info(commands.Cog):
    '''Информация о пользователе'''
    def __init__(self, client) -> None:
        self.client = client


    @commands.command(name='rate', aliases=['рейт', 'рэйт', 'рейтинг'])
    async def rate(self, ctx):
        '''Рейтинг'''
        author = ctx.message.author.name

        user = functions.find_user(author, session.all_users)
        user.count_messages -= 1

        await ctx.send(f'Рейтинг {user.name} = {user.rate}')
        await ctx.message.delete()
    

    @commands.command(name='money', \
        aliases=['мани', 'деньги', 'бабки', 'бабосы', 'бабло', 'монеты', 'монет'])
    async def money(self, ctx):
        '''Количество монет'''
        author = ctx.message.author.name

        user = functions.find_user(author, session.all_users)
        user.count_messages -= 1
        user.money = functions.to_two_digits(user.money)
        
        await ctx.send(f'У {user.name} {user.money} монет')
        await ctx.message.delete()


    @commands.command()
    async def days(self, ctx):
        '''Количество дней на сервере'''
        author = ctx.message.author.name

        user = functions.find_user(author, session.all_users)
        user.count_messages -= 1
        day = functions.date_to_days(user.live_server)

        await ctx.send(f'{author} с нами {day} {functions.get_days(day)}')
        await ctx.message.delete()


    @commands.command(name='info', aliases=['инфо', 'себе', 'я', 'me'])
    async def info(self, ctx):
        '''Вся информация о себе'''
        author = ctx.message.author.name

        user = functions.find_user(author, session.all_users)
        user.count_messages -= 1

        await ctx.send(f'{user.user_info()}')
        await ctx.message.delete()


def setup(client):
    client.add_cog(Info(client))
