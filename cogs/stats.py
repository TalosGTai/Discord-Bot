import session
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

        for user in session.all_users:
            if user.name == hero:
                hero = user
                break
        
        if author == hero.name and author != 'GTai':
            await ctx.send(f'Себе в свой карман класть нельзя! Не шали ;_)')
        else:
            if float(money) > 0:
                hero.money += float(money)
                print(f'{author} добавил {money} монет пользователю {hero.name}')
                await ctx.send(f'{author} добавил {money} монет пользователю {hero.name}')
            else:
                hero.money += float(money)
                print(f'{author} отнял {money} монет у пользователя {hero.name}')
                await ctx.send(f'{author} отнял {money} монет у пользователя {hero.name}')


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def add_req_help(self, ctx, hero):
        '''Увеличение характеристики запросы помощи

        Шаблон: .add_done_help name
        
        Пример: .add_done_help GTai
        Увеличение характеристики на 1
        '''
        author = ctx.message.author.name

        for user in session.all_users:
            if user.name == hero:
                hero = user
                break

        hero.count_done_help += 1
        print(
            f'{author} увеличил количество запросов помощи у {hero.name} на 1')
        await ctx.send(f'{author} увеличил количество запросов помощи у {hero.name} на 1')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def set_req_help(self, ctx, hero, count):
        '''Изменение характеристики запросы помощи

        Шаблон: .add_done_help name count
        
        Пример: .add_done_help GTai 5
        Установил значение равным 5
        '''
        author = ctx.message.author.name

        for user in session.all_users:
            if user.name == hero:
                hero = user
                break

        hero.count_done_help = int(count)
        print(
            f'{author} установил значение количество запросов помощи у {hero.name} равным {count}')
        await ctx.send(f'{author} установил значение количество запросов помощи у {hero.name} равным {count}')


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def add_done_help(self, ctx, hero):
        '''Увеличение характеристики помощь

        Шаблон: .add_done_help name
        
        Пример: .add_done_help GTai
        Увеличение характеристики на 1
        '''
        author = ctx.message.author.name

        for user in session.all_users:
            if user.name == hero:
                hero = user
                break

        hero.count_done_help += 1
        print(f'{author} увеличил количество помощи у {hero.name} на 1')
        await ctx.send(f'{author} увеличил количество помощи у {hero.name} на 1')


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def set_req_help(self, ctx, hero, count):
        '''Изменение характеристики запросы помощи

        Шаблон: .add_done_help name count
        
        Пример: .add_done_help GTai 5
        Установил значение равным 5
        '''
        author = ctx.message.author.name

        for user in session.all_users:
            if user.name == hero:
                hero = user
                break

        hero.count_done_help = int(count)
        print(
            f'{author} установил значение количество запросов помощи у {hero.name} равным {count}')
        await ctx.send(f'{author} установил значение количество запросов помощи у {hero.name} равным {count}')


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def add_count_projects(self, ctx, hero):
        '''Увеличение характеристики количество проектов

        Шаблон: .add_count_projects name count
        
        Пример: .add_count_projects GTai
        Увеличение характеристики на 1
        '''
        author = ctx.message.author.name

        for user in session.all_users:
            if user.name == hero:
                hero = user
                break

        hero.count_projects += 1
        print(f'{author} увеличил количество проектов у {hero.name} на 1')
        await ctx.send(f'{author} увеличил количество проектов у {hero.name} на 1')


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def set_user_date(self, ctx, hero, date):
        '''Установка начало даты пребывания на сервере
        
        Шаблон: .set_user_date name date 
        date: год-месяц-день  | 0000-00-00
        Пример: .set_user_date GTai 2021-04-04
        '''
        author = ctx.message.author.name

        for user in session.all_users:
            if user.name == hero:
                hero = user
        
        hero.live_server = date
        print(f'{author} изменил стартовую дату для {hero.name}')
        await ctx.send(f'{author} изменил стартовую дату для {hero.name}')


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def get_info(self, ctx, hero):
        '''Посмотреть информацию об участнике
        
        Пример: .get_info GTai
        '''
        author = ctx.message.author.name

        for user in session.all_users:
            if user.name == hero:
                await ctx.send(f'{user.user_info()}')
                print(f'{author} запросил информацию {hero}')
                break


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def top_rate(self, ctx):
        '''Топ 10 пользователей по рейтингу'''
        pass


def setup(client):
    client.add_cog(Stats(client))