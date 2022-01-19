from discord.ext import commands
from discord.utils import get


class Dina(commands.Cog):
    '''Управление Диной'''

    def __init__(self, client) -> None:
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def send_msg(self, ctx, channel, msg):
        '''Отправить сообщение в чат
        
        Пример: .send_msg "егэ-чат" "Привет, красавчик ^_^"
        '''
        author = ctx.message.author.name

        #await ctx.send(f'{author} добавил {money} участнику {hero}')


def setup(client):
    client.add_cog(Dina(client))