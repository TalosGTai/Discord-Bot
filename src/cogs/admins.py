from disnake.ext import commands
from src.functions.discord import find_user, set_user_date_registr, \
    add_user_bonus_rate, add_user_count_proj, add_user_done_help, \
    add_user_money, add_user_req_help, set_user_done_help


class Admins(commands.Cog):
    '''Админка на сервере'''

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def all_add_money(self, ctx, money: str):
        '''Добавить всем участникам денег
        
        Пример: .all_add_money 100
        '''

        author = ctx.message.author.name
        
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

        # добавить речь
        await ctx.send(f'Начало сезона! ')
        print(f'{author} начал новый сезон {money} монет')
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
        user = find_user(hero)

        if user:
            set_user_date_registr(hero, date)
            msg = f'{author} изменил стартовую дату для {hero}'
        else:
            msg = 'Выбери существующего человека.'

        print(msg)
        await ctx.send(msg)
        await ctx.message.delete()


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
        user = find_user(hero)

        if author == hero and author != 'GTai'.lower():
            await ctx.send(f'В свой карман класть нельзя! Не шали ;)')
        else:
            if user:
                add_user_money(hero, int(money))

                if int(money) > 0:
                    msg = f'{author} добавил {money} монет пользователю {hero}.'
                else:
                    msg = f'{author} отнял {money} монет у пользователя {hero}.'
            else:
                msg = 'Выбери существующего человека.'
        
        print(msg)
        await ctx.send(msg)
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
        user = find_user(hero)

        if author == hero and author != 'GTai'.lower():
            await ctx.send(f'Себе нельзя изменять! Не шали ;_)')
        else:
            if user:
                add_user_bonus_rate(hero, float(count))

                if float(count) > 0:
                    msg = f'{author} добавил {count} рейтинга пользователю {hero}'
                else:
                    msg = f'{author} отнял {count} рейтинга у пользователя {hero}'
            else:
                msg = 'Выбери существующего человека.'

        print(msg)
        await ctx.send(msg)
        await ctx.message.delete()


    @commands.has_permissions(kick_members=True)
    async def add_req_help(self, ctx, hero: str, count: str):
        '''Увеличение/уменьшние характеристики запросы помощи

        Шаблон: .add_done_help name count
        Пример: .add_done_help GTai 1

        Увеличение характеристики на 1
        '''

        author = ctx.message.author.name
        user = find_user(hero)

        if user:
            add_user_req_help(hero, int(count))
            msg = f'{author} изменил количество запросов помощи у {hero} на {count}'
        else:
            msg = 'Выбери существующего человека.'

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
        user = find_user(hero)

        if user:
            set_user_done_help(hero, int(count))
            msg = f'{author} установил значение количество запросов помощи у {hero} равным {count}'
        else:
            msg = 'Выбери существующего человека.'

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
        user = find_user(hero)

        if user:
            add_user_done_help(hero, int(count))
            msg = f'{author} изменил количество помощи у {hero} на {count}'
        else:
            msg = 'Выбери существующего человека.'

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
        user = find_user(hero)

        if user:
            set_user_done_help(hero, int(count))
            msg = f'{author} установил значение количество помощи у {hero} равным {count}'
        else:
            msg = 'Выбери существующего человека.'

        print(msg)
        await ctx.send(msg)
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def add_count_projects(self, ctx, hero: str):
        '''Увеличение количества проектов

        Шаблон: .add_count_projects
        Пример: .add_count_projects GTai

        Увеличение характеристики на 1
        '''
        
        author = ctx.message.author.name
        user = find_user(hero)

        if user:
            add_user_count_proj(hero, 1)
            msg = f'{author} увеличил количество проектов у {hero} на 1'
        else:
            msg = 'Выбери существующего человека.'

        print(msg)
        await ctx.send(msg)
        await ctx.message.delete()


def setup(bot: commands.Bot):
    bot.add_cog(Admins(bot))
