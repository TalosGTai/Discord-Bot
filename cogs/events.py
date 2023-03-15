from disnake.ext import commands
import functions
import disnake


class Events(commands.Cog):
    '''События'''

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @commands.slash_command(name='дней_до_нг')
    async def days_ny(self, inter: disnake.ApplicationCommandInteraction):
        '''Дней до Нового Года'''

        ny = '2023-12-31'

        days_ny = functions.date_to_days(ny)

        new_line = '\n'
        msg = f'{days_ny} дней до Нового Года!'

        await inter.send(msg)
    
    
    @commands.slash_command(name='дней_до_хэллоуина')
    async def days_helloween(self, inter: disnake.ApplicationCommandInteraction):
        '''Дней до Хэллоуина'''

        ny = '2023-10-31'

        days_ny = functions.date_to_days(ny)

        new_line = '\n'
        msg = f'{days_ny} дней до Хэллоуина!'

        await inter.send(msg)


def setup(bot: commands.Bot):
    bot.add_cog(Events(bot))