import session, functions
from discord.ext import commands
from discord.utils import get

class Stats(commands.Cog):
    '''Изменение/просмотр статистики участников'''

    def __init__(self, client) -> None:
        self.client = client


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def add_money(self, ctx, hero, money):
        '''Добавить/отнять монет участнику
        
        Шаблон: .add_money name money

        Пример1: .add_money GTai 200
        Добавление GTai 200 монет

        Пример2: .add_money GTai -100
        Отнятие у GTai 100 монет
        '''
        author = ctx.message.author.name
        user = functions.find_user(hero, session.all_users)
        
        if author == user.name and author != 'GTai':
            await ctx.send(f'В свой карман класть нельзя! Не шали ;_)')
        else:
            user.money += float(money)

            if float(money) > 0:
                print(f'{author} добавил {money} монет пользователю {user.name}')
                await ctx.send(f'{author} добавил {money} монет пользователю {user.name}')
            else:
                print(f'{author} отнял {money} монет у пользователя {user.name}')
                await ctx.send(f'{author} отнял {money} монет у пользователя {user.name}')


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def add_req_help(self, ctx, hero):
        '''Увеличение характеристики запросы помощи

        Шаблон: .add_done_help name
        
        Пример: .add_done_help GTai
        Увеличение характеристики на 1
        '''
        author = ctx.message.author.name
        user = functions.find_user(hero, session.all_users)

        user.count_req_help += 1
        print(
            f'{author} увеличил количество запросов помощи у {user.name} на 1')
        await ctx.send(f'{author} увеличил количество запросов помощи у {user.name} на 1')


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def set_req_help(self, ctx, hero, count):
        '''Изменение характеристики запросы помощи

        Шаблон: .add_done_help name count
        
        Пример: .add_done_help GTai 5
        Установил значение равным 5
        '''
        author = ctx.message.author.name
        user = functions.find_user(hero, session.all_users)

        user.count_req_help = int(count)
        print(
            f'{author} установил значение количество запросов помощи у {user.name} равным {count}')
        await ctx.send(f'{author} установил значение количество запросов помощи у {user.name} равным {count}')


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def add_done_help(self, ctx, hero):
        '''Увеличение характеристики помощь

        Шаблон: .add_done_help name
        
        Пример: .add_done_help GTai
        Увеличение характеристики на 1
        '''
        author = ctx.message.author.name
        user = functions.find_user(hero, session.all_users)

        user.count_done_help += 1
        print(f'{author} увеличил количество помощи у {user.name} на 1')
        await ctx.send(f'{author} увеличил количество помощи у {user.name} на 1')


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def set_done_help(self, ctx, hero, count):
        '''Изменение характеристики запросы помощи

        Шаблон: .add_done_help name count
        
        Пример: .add_done_help GTai 5
        Установил значение равным 5
        '''
        author = ctx.message.author.name
        user = functions.find_user(hero, session.all_users)

        user.count_done_help = int(count)
        print(
            f'{author} установил значение количество помощи у {user.name} равным {count}')
        await ctx.send(f'{author} установил значение количество помощи у {user.name} равным {count}')


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def add_count_projects(self, ctx, hero):
        '''Увеличение количества проектов

        Шаблон: .add_count_projects name count
        
        Пример: .add_count_projects GTai
        Увеличение характеристики на 1
        '''
        author = ctx.message.author.name
        user = functions.find_user(hero, session.all_users)

        user.count_projects += 1
        print(f'{author} увеличил количество проектов у {user.name} на 1')
        await ctx.send(f'{author} увеличил количество проектов у {user.name} на 1')


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def set_user_date(self, ctx, hero, date):
        '''Установка начало даты пребывания на сервере
        
        Шаблон: .set_user_date name date 
        date: год-месяц-день  | 0000-00-00
        Пример: .set_user_date GTai 2021-04-04
        '''
        author = ctx.message.author.name
        user = functions.find_user(hero, session.all_users)
        
        user.live_server = date
        print(f'{author} изменил стартовую дату для {user.name}')
        await ctx.send(f'{author} изменил стартовую дату для {user.name}')


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def get_info(self, ctx, hero):
        '''Посмотреть информацию об участнике
        
        Пример: .get_info GTai
        '''
        author = ctx.message.author.name
        user = functions.find_user(hero, session.all_users)
        await ctx.send(f'{user.user_info()}')
        print(f'{author} запросил информацию {hero}')


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def all_add_money(self, ctx, money):
        '''Добавить всем участникам денег
        
        Пример: .all_add_money 100
        '''
        author = ctx.message.author.name

        for user in session.all_users:
            user.money += float(money)
        
        await ctx.send(f'Монетки подъехали')
        print(f'{author} дал всем {money} монет')


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def all_set_money(self, ctx, money):
        '''Установить количество монет для всех
        
        Пример: .all_set_money 100
        '''
        author = ctx.message.author.name

        for user in session.all_users:
            user.money = float(money)

        await ctx.send(f'Начало сезона! У всех {money} монет')
        print(f'{author} начал новый сезон {money} монет')


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def top_rate(self, ctx):
        '''Топ 10 пользователей по рейтингу'''
        pass


def setup(client):
    client.add_cog(Stats(client))
