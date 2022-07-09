from discord.ext import commands
import functions


class EGE(commands.Cog):
    '''ЕГЭ'''

    def __init__(self, client) -> None:
        self.client = client


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ege_days(self, ctx):
        '''Дней до начала ЕГЭ'''

        inf = '2022-06-20'
        #math = '2022-06-02'
        #rus = '2022-05-30'

        days_inf = functions.date_to_days(inf)
        #days_math = functions.date_to_days(math)
        #days_rus = functions.date_to_days(rus)

        new_line = '\n'
        #msg = f'до ЕГЭ по русичу {days_rus} дней' + new_line
        #msg += f'до ЕГЭ по матеше {days_math} дней' + new_line
        msg = f'до ЕГЭ по инфе {days_inf} дней'

        #if int(days_rus) == 1:
        #    msg = 'Всем удачки на русском!\n Будьте котиками и затащите ^_^\n'
        #    msg += 'Ведьмачка с вами — сотка в кармане!'
        
        await ctx.send(msg)
        await ctx.message.delete()


def setup(client):
    client.add_cog(EGE(client))