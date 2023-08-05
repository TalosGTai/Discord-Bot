from disnake.ext import commands
import disnake
from src.functions.discord import find_user, get_user_rate, \
    get_user_money, get_user_date, get_user_duel_all_games, \
    get_user_duel_win_games
from src.functions.main_func import load_phrases, date_to_days, \
    get_days
from src.functions.embeds import embed_stats_duel


class Stats(commands.Cog):
    '''Изменение/просмотр статистики участников'''

    def __init__(self,  bot: commands.Bot) -> None:
        self.bot = bot


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def get_info(self, ctx, hero):
        '''Посмотреть информацию об участнике
        
        Пример: .get_info GTai
        '''
        user = find_user(hero)

        if user:
            msg = 'None msg in info'
        else:
            msg = 'Выбери существующего человека.'

        await ctx.send(msg)
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def duel_top(self, ctx):
        '''Топ 5 дуэлянтов этой эпохи
        
        Сюда попадают лучшие из лучших
        Участвуй в дуэлях, выигрывай и станешь одним из них!
        
        Попасть можно только от 30 дуэлей
        '''
        '''
        duel_stat = []
        for user in session.all_users:
            all_games = user.duel_all_games
            win_games = user.duel_win_games
            if win_games != 0:
                percent_win = int((win_games/all_games) * 100)
            else:
                percent_win = 0

            duel_stat.append((user.name, user.duel_all_games,
                             user.duel_win_games, percent_win))

        duel_stat = sorted(duel_stat, key=lambda user: user[3])

        j = len(duel_stat) - 1
        res = [duel_stat[i] for i in range(j, j - 5, -1)]

        rate_duel = 'Топ 5 лучших дуэлянтов этой эпохи:\n'

        for i in range(len(res)):
            wr = int(100 * res[i][2]/res[i][1])
            rate_duel += '{} - {} {}-{} {}%\n'.format(
                i + 1, res[i][0], res[i][1], res[i][2], wr)

        await ctx.send(rate_duel)
        '''
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def duel_info(self, ctx, hero: str):
        '''Статистика в дуэлях
        
        Шаблон: .duel_info name
        Пример: .duel_info GTai
        '''

        user = find_user(hero)

        if user:
            all_games = get_user_duel_all_games(hero)
            win_games = get_user_duel_win_games(hero)
            wr = int((win_games/all_games) * 100)
            values = dict()
            values['all_games'] = all_games 
            values['win_games'] = win_games 
            values['wr'] = wr
            embed = embed_stats_duel(hero, values)
            
            await ctx.send(embed=embed)
        else:
            msg = load_phrases('social', 'not_exist')
            await ctx.send(msg)

        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def top_rate(self, ctx):
        '''Топ 10 пользователей по рейтингу'''
        pass


    @commands.slash_command(name='рейтинг')
    async def rate(self, inter: disnake.ApplicationCommandInteraction):
        '''Рейтинг'''

        author = inter.author.name
        user = find_user(author)

        if user:
            msg = f'Рейтинг {author} = {get_user_rate(author)}'
        else:
            msg = load_phrases('social', 'not_exist')
            
        await inter.send(msg)


    @commands.slash_command(name='монеты')
    async def money(self, inter: disnake.ApplicationCommandInteraction):
        '''Количество монет'''

        author = inter.author.name
        user = find_user(author)

        if user:
            msg = f'У {author} {get_user_money(author)} монет'
        else:
            msg = load_phrases('social', 'not_exist')

        await inter.send(msg)


    @commands.slash_command(name='дней_на_сервере')
    async def days(self, inter: disnake.ApplicationCommandInteraction):
        '''Количество дней на сервере'''

        author = inter.author.name
        user = find_user(author)
        msg = 'Something gone wronge. [days]'

        if user:
            user_date = date_to_days(get_user_date(author))
            msg = f'{author} с нами {user_date} {get_days(user_date)}'
        else:
            msg = load_phrases('social', 'not_exist')

        await inter.send(msg)


    @commands.slash_command(name='инфо')
    async def info(self, inter: disnake.ApplicationCommandInteraction):
        '''Вся информация о себе'''

        author = inter.author
        user = find_user(author)

        if user:
            msg = ''
        else:
            msg = load_phrases('social', 'not_exist')

        await inter.send(msg)   


def setup(bot: commands.Bot):
    bot.add_cog(Stats(bot))
