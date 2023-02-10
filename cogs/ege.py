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

        inf = '2023-06-19'
        math = '2023-06-01'
        rus = '2023-05-29'

        days_inf = functions.date_to_days(inf)
        days_math = functions.date_to_days(math)
        days_rus = functions.date_to_days(rus)
        # окончания
        str_inf = functions.get_days(days_inf + 1)
        str_math = functions.get_days(days_math)
        str_rus = functions.get_days(days_rus)

        new_line = '\n'
        msg = f'до ЕГЭ по русичу {days_rus} {str_inf}' + new_line
        msg += f'до ЕГЭ по матеше {days_math} {str_math}' + new_line
        msg += f'до ЕГЭ по инфе {days_inf}/{days_inf + 1} {str_rus}'

        #if int(days_rus) == 1:
        #    msg = 'Всем удачки на русском!\n Будьте котиками и затащите ^_^\n'
        #    msg += 'GTai с вами — сотка в кармане!'
        
        await ctx.send(msg)
        await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def math_days(self, ctx):
        '''Дней до начала ЕГЭ'''

        math = '2022-06-01'

        days_math = functions.date_to_days(math)

        new_line = '\n'
        msg = f'до ЕГЭ по матеше {days_math} дней' + new_line

        #if int(days_rus) == 1:
        #    msg = 'Всем удачки на русском!\n Будьте котиками и затащите ^_^\n'
        #    msg += 'Ведьмачка с вами — сотка в кармане!'

        await ctx.send(msg)
        await ctx.message.delete()
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def rus_days(self, ctx):
        '''Дней до начала ЕГЭ'''

        rus = '2022-05-29'

        days_rus = functions.date_to_days(rus)

        new_line = '\n'
        msg = f'до ЕГЭ по русичу {days_rus} дней' + new_line

        #if int(days_rus) == 1:
        #    msg = 'Всем удачки на русском!\n Будьте котиками и затащите ^_^\n'
        #    msg += 'Ведьмачка с вами — сотка в кармане!'

        await ctx.send(msg)
        await ctx.message.delete()


def setup(client):
    client.add_cog(EGE(client))