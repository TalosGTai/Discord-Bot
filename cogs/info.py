import session, functions
from disnake.ext import commands
import disnake


class Info(commands.Cog):
    '''Информация о пользователе'''

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @commands.slash_command(name='рейтинг')
    async def rate(self, ctx):
        '''Рейтинг'''
        author = ctx.message.author.name

        user = functions.find_user(author, session.all_users)
        user.count_messages -= 1

        await ctx.send(f'Рейтинг {user.name} = {user.rate}')
    

    @commands.slash_command(name='монеты')
    async def money(self, ctx):
        '''Количество монет'''
        author = ctx.message.author.name

        user = functions.find_user(author, session.all_users)
        user.count_messages -= 1
        user.money = functions.to_two_digits(user.money)
        
        await ctx.send(f'У {user.name} {user.money} монет')


    @commands.slash_command(name='дней_на_сервере')
    async def days(self, ctx):
        '''Количество дней на сервере'''
        author = ctx.message.author.name

        user = functions.find_user(author, session.all_users)
        user.count_messages -= 1
        day = functions.date_to_days(user.live_server)

        await ctx.send(f'{author} с нами {day} {functions.get_days(day)}')


    @commands.slash_command(name='инфо')
    async def info(self, ctx):
        '''Вся информация о себе'''
        author = ctx.message.author.name

        user = functions.find_user(author, session.all_users)
        user.count_messages -= 1

        await ctx.send(f'{user.user_info()}')


def setup(bot: commands.Bot):
    bot.add_cog(Info(bot))
