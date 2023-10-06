from disnake.ext import commands
import disnake
from src.functions.discord import find_user, set_user_date_registr, \
    add_user_bonus_rate, add_user_count_proj, add_user_done_help, \
    add_user_money, add_user_req_help, set_user_done_help, \
    find_user_by_name_discord
from src.data.db_help_functional import add_warn_to_user
from asyncio import sleep
from src.modules.panel_main_buttons import MainPanelButtons


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
            msg = 'Пользователь не найден.'

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
                msg = 'Пользователь не найден.'
        
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
                msg = 'Пользователь не найден.'

        print(msg)
        await ctx.send(msg)
        await ctx.message.delete()


    @commands.command()
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
            msg = 'Пользователь не найден.'

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
            msg = 'Пользователь не найден.'

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
            msg = 'Пользователь не найден.'

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
            msg = 'Пользователь не найден.'

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

        if find_user(hero) or (hero[0] == '@' and find_user(hero[1::])):
            add_user_count_proj(hero, 1)
            msg = f'{author} увеличил количество проектов у {hero} на 1'
        else:
            msg = 'Пользователь не найден.'

        print(msg)
        await ctx.send(msg)
        await ctx.message.delete()


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
    async def kick_user(self, ctx, hero: str, reason: str):
        '''Кик пользователя'''

        author = ctx.message.author.name

        if find_user(hero) or (hero[0] == '@' and find_user(hero[1::])):
            user = find_user_by_name_discord(self.bot, hero)
            await user.kick(reason=reason)
            msg = f'{author} кикнул участника {hero} по причине {reason}'
            add_warn_to_user(hero, 'kick', reason)
        else:
            msg = 'Пользователь не найден.'

        print(msg)
        await ctx.send(msg)
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute_user(self, ctx, hero: str, time: str, reason: str):
        '''Мут пользователя'''

        author = ctx.message.author.name
        condition_time = time.isdigit()
        condition_user = find_user(hero) or (
            hero[0] == '@' and find_user(hero[1::]))

        if condition_time:
            if condition_user:
                time = int(time)
                user = find_user_by_name_discord(self.bot, hero)
                role = user.mutual_guilds[0].get_role(1155196925923045506)
                msg = f'{author} дал мут {hero} по причине {reason} на {time} минут.'
                add_warn_to_user(hero, 'mute', reason, time)
                await user.add_roles(role)
            else:
                msg = 'Пользователь не найден.'
        else:
            msg = 'Ошибка формата времени. Время должно быть целым числом.'

        print(msg)
        await ctx.send(msg)
        await ctx.message.delete()
        
        if condition_time and condition_user:
            await sleep(60 * time)
            await user.remove_roles(role)
    

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute_user(self, ctx, hero: str):
        '''Размут пользователя'''

        author = ctx.message.author.name

        if find_user(hero) or (hero[0] == '@' and find_user(hero[1::])):
            user = find_user_by_name_discord(self.bot, hero)
            role = user.mutual_guilds[0].get_role(1155196925923045506)
            msg = f'{author} убрал мут у {hero}'
            await user.remove_roles
        else:
            msg = 'Пользователь не найден.'

        print(msg)
        await ctx.send(msg)
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn_user(self, ctx, hero: str, reason: str):
        '''Предупреждение пользователю'''

        author = ctx.message.author.name

        if find_user(hero) or (hero[0] == '@' and find_user(hero[1::])):
            msg = f'{author} дал предупреждение {hero} по причине {reason}'
            add_warn_to_user(hero, 'warn', reason)
        else:
            msg = 'Пользователь не найден.'

        print(msg)
        await ctx.send(msg)
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban_user(self, ctx, hero: str, reason: str):
        '''Бан пользователя'''

        author = ctx.message.author.name
        user = find_user(hero)

        if user:
            user = find_user_by_name_discord(self.bot, hero)
            await user.ban(reason=reason)
            msg = f'{author} забанил участника {hero} по причине {reason}'
            add_warn_to_user(hero, 'ban', reason)
        else:
            msg = 'Пользователь не найден.'

        print(msg)
        await ctx.send(msg)
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban_user(self, ctx, hero: str, reason: str):
        '''Разбан пользователя'''

        author = ctx.message.author.name
        user = find_user(hero)

        if user:
            user = find_user_by_name_discord(self.bot, hero)
            await user.unban(reason=reason)
            msg = f'{author} разбанил участника {hero} по причине {reason}'
        else:
            msg = 'Пользователь не найден.'

        print(msg)
        await ctx.send(msg)
        await ctx.message.delete()


    @commands.slash_command(name='панель_модератора')
    @commands.has_permissions(kick_members=True)
    async def moder_panel(self, inter: disnake.GuildCommandInteraction):
        '''Описание всех возможностей модератора'''

        await inter.send(view=MainPanelButtons())
  

def setup(bot: commands.Bot):
    bot.add_cog(Admins(bot))
