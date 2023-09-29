import disnake
from disnake.ext import commands
from disnake.enums import ButtonStyle
from src.data.db_help_functional import get_task
from src.functions.main_func import date_to_days, get_days
from src.functions.embeds import embed_task_msg, embed_days_to_ege,\
    embed_wrong_channel
from src.functions.discord import find_channel_by_name
from src.modules.row_buttons import RowButtons


class Ege(commands.Cog):
    '''ЕГЭ'''

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @commands.slash_command(name='дней_до_егэ')
    async def ege_days(self, inter: disnake.ApplicationCommandInteraction):
        '''Дней до начала ЕГЭ'''

        inf = '2024-06-19'
        math = '2024-06-01'
        rus = '2024-05-29'
        physics = '2024-06-05'
        social = '2024-06-05'
        history = '2024-06-29'

        days_inf = date_to_days(inf)
        days_math = date_to_days(math)
        days_rus = date_to_days(rus)
        days_physics = date_to_days(physics)
        days_social = date_to_days(social)
        days_history = date_to_days(history)
        # окончания
        str_inf = get_days(days_inf + 1)
        str_math = get_days(days_math)
        str_rus = get_days(days_rus)
        str_physics = get_days(days_physics)
        str_social = get_days(days_social)
        str_history = get_days(days_history)

        t_ege = ((days_inf, str_inf), (days_math, str_math),
                 (days_rus, str_rus), (days_physics, str_physics),
                 (days_social, str_social), (days_history, str_history))

        title, description, color = embed_days_to_ege(t_ege)
        embed = disnake.Embed(
            title=title, description=description, color=color)
        
        await inter.send(embed=embed)
    

    @commands.slash_command(name='задачи_егэ_инф')
    async def tasks(self, 
     inter: disnake.ApplicationCommandInteraction,
        номер: int = 8, сложность: str = 'Средняя'):
        number_task, complexity = номер, сложность
        '''Реши задачу из любого номера ЕГЭ по Информатике'''
        
        channels = ['инфа-задачи', 'группа-орлы', 'группа-убийцы', 'кругосветка-pro']
        
        if str(inter.guild.get_channel(inter.channel.id)) in channels or \
                inter.author.name == 'GTai'.lower():
            lst_tasks = [1, 2, 8, 13, 15, 23, 24]
            types_complexity = ['Лёгкая', 'Средняя', 'Сложная']
            complexity = complexity[0].upper() + complexity.lower()[1::]

            if number_task in lst_tasks and complexity in types_complexity:
                row = get_task(number_task, complexity)
                
                if type(row) != str:
                    embed = embed_task_msg(number_task, row)

                    await inter.send(embeds=embed, view=RowButtons(row['answer']))

                    if 'txt' in row.keys():
                        await inter.send(file=row['txt'])
                else:
                    msg = row
                    await inter.send(msg)
            else:
                msg = f'Выбери номер из {lst_tasks} и сложность из {types_complexity}'
                await inter.send(msg)
        else:
            channel = find_channel_by_name(self.bot, 'инфа-задачи')
            embed = embed_wrong_channel(channel.mention, 'ege')
            
            await inter.send(embed=embed)


    @commands.has_permissions(administrator=True)
    @commands.slash_command(name='тест')
    async def test(self, inter: disnake.GuildCommandInteraction):
        #file = disnake.File(fp='S:/Programming/DB/ege_2/1.1.png')
        #embed = disnake.Embed(title='Test img',
        #    description='some text here')
        #embed.set_image(file=file)
        for guild in self.bot.guilds:
            for channel in guild.channels:
                if channel.name == 'вопросы-от-ведьмачки':
                    await inter.send(channel.mention)
        await inter.send(inter.author.display_name)


def setup(bot: commands.Bot):
    bot.add_cog(Ege(bot))