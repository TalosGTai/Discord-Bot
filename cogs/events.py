from discord.ext import commands
import functions


class Events(commands.Cog):
    '''События'''

    def __init__(self, client) -> None:
        self.client = client

    @commands.command()
    async def ny_days(self, ctx):
        '''Дней до начала Нового Года'''

        ny = '2023-12-31'

        days_ny = functions.date_to_days(ny)

        new_line = '\n'
        msg = f'{days_ny} дней до Нового Года!'

        #if int(days_rus) == 1:
        #    msg = 'Всем удачки на русском!\n Будьте котиками и затащите ^_^\n'
        #    msg += 'Ведьмачка с вами — сотка в кармане!'

        await ctx.send(msg)
        await ctx.message.delete()


def setup(client):
    client.add_cog(Events(client))