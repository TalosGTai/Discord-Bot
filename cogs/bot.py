from discord.ext import commands
from discord.utils import get


class Dina(commands.Cog):
    '''Управление Диной'''

    def __init__(self, client) -> None:
        self.client = client

    @commands.command(name='смс', aliases=['send', 'send_msg'])
    @commands.has_permissions(administrator=True)
    async def send_msg(self, ctx, msg, msg_channel):
        '''Отправить сообщение в чат
        
        Шаблон: command channel msg
        Пример: .send_msg "егэ-чат" "Привет, красавчик ^_^"
        '''

        for guild in self.client.guilds:
            for channel in guild.channels:
                if channel.name == msg_channel:
                    await channel.send(msg)
        await ctx.message.delete()


    @commands.command(name='clear', aliases=['очистить', 'удалить'])
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, count):
        '''Удаление сообщений'''

        await ctx.channel.purge(limit=int(count))
        await ctx.message.delete()
        

def setup(client):
    client.add_cog(Dina(client))