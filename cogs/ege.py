import disnake
from disnake.ext import commands
from db_functions import get_task
from functions import date_to_days, get_days, embed_task_msg, embed_days_to_ege


class Ege(commands.Cog):
    '''ЕГЭ'''

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @commands.slash_command(name='дней_до_егэ')
    async def ege_days(self, ctx):
        '''Дней до начала ЕГЭ'''

        inf = '2023-06-19'
        math = '2023-06-01'
        rus = '2023-05-29'

        days_inf = date_to_days(inf)
        days_math = date_to_days(math)
        days_rus = date_to_days(rus)
        # окончания
        str_inf = get_days(days_inf + 1)
        str_math = get_days(days_math)
        str_rus = get_days(days_rus)

        t_ege = ((days_inf, str_inf), (days_math, str_math),
         (days_rus, str_rus))

        title, description, color = embed_days_to_ege(t_ege)
        embed = disnake.Embed(
            title=title, description=description, color=color)

        #if int(days_rus) == 1:
        #    msg = 'Всем удачки на русском!\n Будьте котиками и затащите ^_^\n'
        #    msg += 'GTai с вами — сотка в кармане!'
        
        await ctx.send(embed=embed)
    

    @commands.has_permissions(kick_members=True)
    @commands.slash_command(name='задачи_егэ_инф')
    async def tasks(self, inter: disnake.ApplicationCommandInteraction,
     number_task: int = 8, complexity: str = 'Средняя'):
        '''Реши задачу из любого номера ЕГЭ по Информатике'''
        
        lst_tasks = [2, 8]
        types_complexity = ['Лёгкая', 'Средняя', 'Сложная']
        complexity = complexity[0].upper() + complexity.lower()[1::]

        if number_task in lst_tasks and complexity in types_complexity:
            row = get_task(number_task, complexity)
            title, description, color = embed_task_msg(number_task, row)
            embed = disnake.Embed(
                title=title, description=description, color=color)

            await inter.send(embed=embed)
        else:
            msg = f'Выбери номер из {lst_tasks} и сложность из {types_complexity}'
            await inter.send(msg)


    @commands.has_permissions(kick_members=True)
    @commands.slash_command(name='тест', options=[name])
    async def test(self, inter: disnake.GuildCommandInteraction):
        owner = await self.bot.fetch_user(172383544201445376)
        role = owner.mutual_guilds[0].get_role(1075208457633935470)
        boy = disnake.utils.get(self.bot.get_all_members(), id=owner.id)
        
        await boy.add_roles(role)


def setup(bot: commands.Bot):
    bot.add_cog(Ege(bot))