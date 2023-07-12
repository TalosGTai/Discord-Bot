import session
from disnake.ext import commands
from ..functions.main_func import find_user

class Stats(commands.Cog):
    '''Изменение/просмотр статистики участников'''

    def __init__(self,  bot: commands.Bot) -> None:
        self.bot = bot


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def add_money(self, ctx, hero: str, money: str):
        '''Добавить/отнять монет участнику
        
        Шаблон: .add_money name money

        Пример1: .add_money GTai 200
        Добавление GTai 200 монет

        Пример2: .add_money GTai -100
        Отнятие у GTai 100 монет
        '''
        author = ctx.message.author.name
        user = find_user(hero, session.all_users)
        
        if author == user.name and author != 'GTai':
            await ctx.send(f'В свой карман класть нельзя! Не шали ;_)')
        else:
            user.money += float(money)

            if float(money) > 0:
                msg = f'{author} добавил {money} монет пользователю {user.name}'
                await ctx.send(msg)
            else:
                msg = f'{author} отнял {money} монет у пользователя {user.name}'
                await ctx.send(msg)
        print(msg)
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def add_rate(self, ctx, hero: str, count: str):
        '''Добавить/отнять бонусный рейтинг
        
        Шаблон: .add_rate name count

        Пример1: .add_rate GTai 5
        Добавление GTai 5 рейтинга

        Пример2: .add_rate GTai -10
        Отнятие у GTai 10 рейтинга
        '''
        author = ctx.message.author.name
        user = find_user(hero, session.all_users)

        if author == user.name and author != 'GTai':
            await ctx.send(f'Себе нельзя изменять! Не шали ;_)')
        else:
            user.bonus_rate += float(count)

            if float(count) > 0:
                msg = f'{author} добавил {count} рейтинга пользователю {user.name}'
                await ctx.send(msg)
            else:
                msg = f'{author} отнял {count} рейтинга у пользователя {user.name}'
                await ctx.send(msg)
        print(msg)
        await ctx.message.delete()


    @commands.has_permissions(kick_members=True)
    async def add_req_help(self, ctx, hero: str, count: str):
        '''Увеличение/уменьшние характеристики запросы помощи

        Шаблон: .add_done_help name count
        
        Пример: .add_done_help GTai 1
        Увеличение характеристики на 1
        '''
        author = ctx.message.author.name
        user = find_user(hero, session.all_users)
        user.count_req_help += count
        msg = f'{author} изменил количество запросов помощи у {user.name} на {count}'

        print(msg)
        await ctx.send(msg)
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def set_req_help(self, ctx, hero: str, count: str):
        '''Изменение характеристики запросы помощи

        Шаблон: .add_done_help name count
        
        Пример: .add_done_help GTai 5
        Установил значение равным 5
        '''
        author = ctx.message.author.name
        user = find_user(hero, session.all_users)
        user.count_req_help = int(count)
        msg = f'{author} установил значение количество запросов помощи у {user.name} равным {count}'

        print(msg)
        await ctx.send(msg)
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def add_done_help(self, ctx, hero: str, count: str):
        '''Увеличение/уменьшние характеристики помощь

        Шаблон: .add_done_help name count
        
        Пример: .add_done_help GTai 1
        Увеличение характеристики на 1
        '''
        author = ctx.message.author.name
        user = find_user(hero, session.all_users)
        user.count_done_help += int(count)
        msg = f'{author} изменил количество помощи у {user.name} на {count}'

        print(msg)
        await ctx.send(msg)
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def set_done_help(self, ctx, hero: str, count: str):
        '''Изменение характеристики запросы помощи

        Шаблон: .add_done_help name count
        
        Пример: .add_done_help GTai 5
        Установил значение равным 5
        '''
        author = ctx.message.author.name
        user = find_user(hero, session.all_users)
        user.count_done_help = int(count)
        msg = f'{author} установил значение количество помощи у {user.name} равным {count}'

        print(msg)
        await ctx.send(msg)
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def add_count_projects(self, ctx, hero: str, count: str):
        '''Увеличение количества проектов

        Шаблон: .add_count_projects name count
        
        Пример: .add_count_projects GTai 1
        Увеличение характеристики на 1
        '''
        author = ctx.message.author.name
        user = find_user(hero, session.all_users)
        user.count_projects += 1
        msg = f'{author} увеличил количество проектов у {user.name} на 1'

        print(msg)
        await ctx.send(msg)
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def set_user_date(self, ctx, hero: str, date: str):
        '''Установка начало даты пребывания на сервере
        
        Шаблон: .set_user_date name date 
        date: год-месяц-день  | 0000-00-00
        Пример: .set_user_date GTai 2021-04-04
        '''
        author = ctx.message.author.name
        user = find_user(hero, session.all_users)
        user.live_server = date
        msg = f'{author} изменил стартовую дату для {user.name}'

        print(msg)
        await ctx.send(msg)
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def get_info(self, ctx, hero):
        '''Посмотреть информацию об участнике
        
        Пример: .get_info GTai
        '''
        user = find_user(hero, session.all_users)

        await ctx.send(f'{user.user_info()}')
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def all_add_money(self, ctx, money: str):
        '''Добавить всем участникам денег
        
        Пример: .all_add_money 100
        '''
        author = ctx.message.author.name

        for user in session.all_users:
            user.money += float(money)
        
        # фразы
        await ctx.send(f'Монетки подъехали')
        print(f'{author} дал всем {money} монет')
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def all_set_money(self, ctx, money: str):
        '''Установить количество монет для всех
        
        Пример: .all_set_money 100
        '''
        author = ctx.message.author.name

        for user in session.all_users:
            user.money = float(money)

        # добавить речь
        await ctx.send(f'Начало сезона! ')
        print(f'{author} начал новый сезон {money} монет')
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def duel_top(self, ctx):
        '''Топ 5 дуэлянтов этой эпохи
        
        Сюда попадают лучшие из лучших
        Участвуй в дуэлях, выигрывай и станешь одним из них!
        
        Попасть можно только от 30 дуэлей
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
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def duel_info(self, ctx, hero: str):
        '''Статистика в дуэлях
        
        Шаблон: .duel_info name
        Пример: .duel_info GTai
        '''
        user = find_user(hero, session.all_users)
        all_games = int(user.duel_all_games)
        win_games = int(user.duel_win_games)
        wr = int((win_games/all_games) * 100)
        msg = f'Статы {user.name} в игре Дуэль'
        msg += f'\n{user.duel_stats()}, {wr}%'
        
        await ctx.send(msg)
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def top_rate(self, ctx):
        '''Топ 10 пользователей по рейтингу'''
        pass


def setup(bot: commands.Bot):
    bot.add_cog(Stats(bot))
