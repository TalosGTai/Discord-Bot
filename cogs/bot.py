from disnake.ext import commands
import disnake


class Dina(commands.Cog):
    '''Управление Диной'''

    def __init__(self, client) -> None:
        self.client = client

    @commands.command(name='send_msg', aliases=['send', 'смс'])
    @commands.has_permissions(administrator=True)
    async def send_msg(self, ctx, msg_channel, msg):
        '''Отправить сообщение в чат
        
        Шаблон: command channel msg
        Пример: .send_msg "егэ-чат" "Привет, красавчик ^_^"
        '''

        for guild in self.client.guilds:
            for channel in guild.channels:
                if channel.name == msg_channel:
                    await channel.send(msg)


    @commands.command(name='send_embed', aliases=['embed'])
    @commands.has_permissions(administrator=True)
    async def send_embed(self, ctx, msg_channel: str, title: str,
    description: str, color: str):
        '''Отправить сообщение в чат
        
        Шаблон: command channel msg
        Пример: .send_embed "егэ-чат" "Заголовок" "текст" "0x0004eb"
        '''
        color = int(color, 16)
        embed = disnake.Embed(title=title,
                              description=description, color=color)

        for guild in self.client.guilds:
            for channel in guild.channels:
                if channel.name == msg_channel:
                    await channel.send(embed=embed)


    @commands.command(name='clear', aliases=['очистить', 'удалить'])
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, count):
        '''Удаление сообщений'''

        await ctx.channel.purge(limit=int(count))
        await ctx.message.delete()
        

def setup(client):
    client.add_cog(Dina(client))