from disnake.ext import commands
import functions
import disnake


class Events(commands.Cog):
    '''События'''

    def __init__(self, client) -> None:
        self.client = client


    @commands.slash_command(name='дней_до_нг')
    async def ny_days(self, ctx):
        '''Дней до начала Нового Года'''

        ny = '2023-12-31'

        days_ny = functions.date_to_days(ny)

        new_line = '\n'
        msg = f'{days_ny} дней до Нового Года!'

        await ctx.send(msg)


def setup(client):
    client.add_cog(Events(client))