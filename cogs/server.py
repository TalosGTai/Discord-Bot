from email.mime import application
from http import client
import session
from discord.ext import commands, tasks
from discord.utils import get
import datetime as DT


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

        # session.all_users
        session.save_db(session.all_users)
        print(f'{DT.datetime.now().hour}:{DT.datetime.now().minute}: Все данные сохранены.')


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def dina_save(self, ctx):
        '''Принудительное сохранение'''

        for user in session.all_users:
            user.update_rate()

        session.save_db(session.all_users)

        print('Обновлены все рейтинги.')
        print(f'{DT.datetime.now().hour}:{DT.datetime.now().minute}: Все данные сохранены.')


def setup(client):
    client.add_cog(Server(client))