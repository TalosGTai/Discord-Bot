from email.mime import application
from http import client
import session
from discord.ext import commands, tasks
from discord.utils import get
import datetime as DT
import functions


class Server(commands.Cog):
    '''Команды для управления'''
    def __init__(self, client) -> None:
        self.client = client
        self.update_rate.start()
        self.save.start()


    @tasks.loop(minutes=30.0)
    async def update_rate(self):
        '''Обновление всех рейтингов'''

        for user in session.all_users:
            user.update_rate()

        print('Обновлены все рейтинги.')


    @tasks.loop(minutes=30.0)
    async def save(self):
        '''Сохранение всей статистики'''

        session.save_db(session.all_users)
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

        session.save_db(session.all_users)
        minutes = functions.time_format(str(DT.datetime.now().minute))
        hours = functions.time_format(str(DT.datetime.now().hour))
        msg = 'Обновлены все рейтинги.' + '\n'
        msg += f'{hours}:{minutes}: Все данные сохранены.'

        print(msg)
        await ctx.message.delete()


def setup(client):
    client.add_cog(Server(client))