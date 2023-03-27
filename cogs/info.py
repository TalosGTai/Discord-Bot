import session, functions
from disnake.ext import commands
import disnake


class Info(commands.Cog):
    '''Информация о пользователе'''

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @commands.slash_command(name='рейтинг')
    async def rate(self, inter: disnake.ApplicationCommandInteraction):
        '''Рейтинг'''
        author = inter.author

        user = functions.find_user(author.name, session.all_users)
        user.count_messages -= 1

        await inter.send(f'Рейтинг {user.name} = {user.rate}')
    

    @commands.slash_command(name='монеты')
    async def money(self, inter: disnake.ApplicationCommandInteraction):
        '''Количество монет'''
        author = author = inter.author

        user = functions.find_user(author.name, session.all_users)
        user.count_messages -= 1
        user.money = functions.to_two_digits(user.money)
        
        await inter.send(f'У {user.name} {user.money} монет')


    @commands.slash_command(name='дней_на_сервере')
    async def days(self, inter: disnake.ApplicationCommandInteraction):
        '''Количество дней на сервере'''
        author = inter.author

        user = functions.find_user(author.name, session.all_users)
        user.count_messages -= 1
        day = functions.date_to_days(user.live_server)

        await inter.send(f'{author} с нами {day} {functions.get_days(day)}')


    @commands.slash_command(name='инфо')
    async def info(self, inter: disnake.ApplicationCommandInteraction):
        '''Вся информация о себе'''
        author = inter.author

        user = functions.find_user(author.name, session.all_users)
        user.count_messages -= 1

        await inter.send(f'{user.user_info()}')


def setup(bot: commands.Bot):
    bot.add_cog(Info(bot))
