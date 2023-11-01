from src.functions.main_func import load_phrases
from src.functions.embeds import embed_by_phrase, \
    embed_wrong_channel, embed_rules_lucky_game, embed_stats_lucky, embed_stats_duel, embed_games_panel
from src.functions.discord import find_user, find_channel_by_name,\
    get_user_money, update_duel_stats, add_user_money, update_lucky_stats, \
    form_lucky_stats_dict, form_duel_stats_dict
from src.functions.duel_func import duel_algo, calculate_money_win
from disnake.ext import commands
import disnake
from random import randint
from asyncio.exceptions import TimeoutError
from src.functions.describe import duel_describe


class Games(commands.Cog):
    '''Игры'''

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.slash_command(name='дуэль')
    async def duel(self, inter: disnake.ApplicationCommandInteraction,
                   противник: str):
        '''Вызов на дуэль другого игрока'''
        #
        # channels = ['игры']
        #
        # if str(inter.guild.get_channel(inter.channel.id)) in channels or \
        #         inter.author.name == 'gtai':
        await inter.send(embeds=[embed_games_panel(duel_describe()), embed_stats_duel(inter.author.name,
                                                         form_duel_stats_dict(inter.author.name))])
        hero = противник
        author = inter.author.name
        user2 = find_user(hero)

        if not user2:
            phrase = load_phrases('games', 'duel', 'none')
            embed = embed_by_phrase(phrase)
            await inter.send(embed=embed)
        else:
            if get_user_money(author) == 0:
                phrase = load_phrases('games', 'duel', 'money_self')
                embed = embed_by_phrase(phrase)
                await inter.send(embed=embed)
            elif get_user_money(hero) == 0:
                phrase = load_phrases('games', 'duel', 'money_enemy')
                embed = embed_by_phrase(phrase)
                await inter.send(embed=embed)
            else:
                if hero.lower() == 'кристи':
                    phrase = load_phrases('games', 'duel', 'bot')
                    embed = embed_by_phrase(phrase)
                    await inter.send(embed=embed)
                elif author == hero:
                    phrase = load_phrases('games', 'duel', 'self')
                    embed = embed_by_phrase(phrase)
                    await inter.send(embed=embed)
                else:
                    res = duel_algo(author, hero)
                    user_win = res['winner']
                    user_lose = res['loser']
                    wr1 = res['wr_w']
                    wr2 = res['wr_l']

                    update_duel_stats(user_win, user_lose)

                    money_win = calculate_money_win(
                        wr1, wr2, get_user_money(user_win),
                        get_user_money(user_lose))

                    add_user_money(user_win, money_win)
                    add_user_money(user_lose, -money_win)

                    msg = 'Дуэль между {} {}% и {} {}%\n'.format(
                        user_win, wr1, user_lose, wr2)
                    msg += '{} одержал победу в дуэли над {}\n'.format(
                        user_win, user_lose)
                    msg += 'И выиграл {} монет'.format(money_win)

                    await inter.send(msg)
        # else:
        #     channel = find_channel_by_name(self.bot, 'игры')
        #     embed = embed_wrong_channel(channel.mention, 'duel')
        #
        #     await inter.send(embed=embed)

    @commands.slash_command(name='угадай_число')
    async def lucky_number(self, inter: disnake.ApplicationCommandInteraction):
        '''Угадай число'''
        #
        # channels = ['игры']
        #
        # if str(inter.guild.get_channel(inter.channel.id)) in channels or \
        #         inter.author.name == 'gtai':

        game = -1
        money_win = 60
        time_timeout = 30
        msg_win = 'Поздравляю тебя user! Ты угадал число number! \n'
        msg_win += f'Твой выигрыш составил {money_win} монет.'
        msg_more = 'Я загадала число больше твоего.'
        msg_less = 'Я загадала число меньше твоего.'
        msg_lose = 'К сожалению, ты проиграл. Загаданное число: number.'

        await inter.send(embeds=[embed_rules_lucky_game(time_timeout), embed_stats_lucky(inter.author.name,
                                                         form_lucky_stats_dict(inter.author.name))])
        # проверка на начало игры
        if game == -1:
            game = randint(1, 100)
            msg = f'На ответ даётся {time_timeout} секунд.\n'
            msg += 'Твоя 1ая попытка, удачи!'
            await inter.send(msg)

            def check(m):
                return m.author == inter.author

            try:
                answer = await self.bot.wait_for("message", check=check,
                                                 timeout=time_timeout)
                answer = answer.content
            except TimeoutError:
                update_lucky_stats(inter.author.name, 0)
                return await inter.send(f'{inter.author.name} время вышло. Игра окончена.')

            if str(answer).isdigit():
                # первый ход
                if game == int(answer):
                    msg = msg_win.replace('user', str(
                        inter.author.name)).replace('number', str(game))
                    update_lucky_stats(inter.author.name, 1)
                    add_user_money(inter.author.name, money_win)
                    return await inter.send(msg)
                elif game > int(answer):
                    msg = msg_more
                else:
                    msg = msg_less

                msg += '\n' + 'Твоя 2ая попытка'
                await inter.send(msg)

                # 2ой ход
                try:
                    answer = await self.bot.wait_for("message",
                                                     check=check, timeout=time_timeout)
                    answer = answer.content
                except TimeoutError:
                    update_lucky_stats(inter.author.name, 0)
                    return await inter.send(f'{inter.author.name} время вышло. Игра окончена.')

                if str(answer).isdigit():
                    if game == int(answer):
                        msg = msg_win.replace('user', str(inter.author.name)).replace(
                            'number', str(game))
                        add_user_money(inter.author.name, money_win)
                        update_lucky_stats(inter.author.name, 1)
                        return await inter.send(msg)
                    elif game > int(answer):
                        msg = msg_more
                    else:
                        msg = msg_less

                    msg += '\n' + 'Твоя 3яя попытка'
                    await inter.send(msg)

                    # 3ий ход
                    try:
                        answer = await self.bot.wait_for("message", check=check, timeout=time_timeout)
                        answer = answer.content
                    except TimeoutError:
                        update_lucky_stats(inter.author.name, 0)
                        return await inter.send(f'{inter.author.name} время вышло. Игра окончена.')

                    if str(answer).isdigit():
                        if game == int(answer):
                            msg = msg_win.replace('user', str(inter.author.name)).replace(
                                'number', str(game))
                            add_user_money(inter.author.name, money_win)
                            update_lucky_stats(inter.author.name, 1)
                            return await inter.send(msg)
                        elif game > int(answer):
                            msg = msg_more
                        else:
                            msg = msg_less

                        msg += '\n' + 'Твоя 4ая попытка'
                        await inter.send(msg)

                        # 4ый ход
                        try:
                            answer = await self.bot.wait_for("message",
                                                             check=check, timeout=time_timeout)
                            answer = answer.content
                        except TimeoutError:
                            update_lucky_stats(inter.author.name, 0)
                            return await inter.send(f'{inter.author.name} время вышло. Игра окончена.')

                        if str(answer).isdigit():
                            if game == int(answer):
                                msg = msg_win.replace('user', str(inter.author.name)).replace(
                                    'number', str(game))
                                add_user_money(inter.author.name, money_win)
                                update_lucky_stats(inter.author.name, 1)
                                return await inter.send(msg)
                            elif game > int(answer):
                                msg = msg_more
                            else:
                                msg = msg_less

                            msg += '\n' + 'Твоя 5ая попытка. Ты сможешь!'
                            await inter.send(msg)

                            # 5ый ход
                            try:
                                answer = await self.bot.wait_for("message",
                                                                 check=check, timeout=time_timeout)
                                answer = answer.content
                            except TimeoutError:
                                update_lucky_stats(inter.author.name, 0)
                                return await inter.send(f'{inter.author.name} время вышло. Игра окончена.')

                            if str(answer).isdigit():
                                if game == int(answer):
                                    msg = msg_win.replace('user', str(
                                        inter.author.name)).replace('number', str(game))
                                    add_user_money(inter.author.name, money_win)
                                    update_lucky_stats(inter.author.name, 1)
                                    return await inter.send(msg)
                                elif game > int(answer):
                                    msg = msg_more
                                else:
                                    msg = msg_less

                                msg += '\n' + 'Твоя последняя попытка. Пробуди свою силу!'
                                await inter.send(msg)

                                # 6ой ход
                                try:
                                    answer = await self.bot.wait_for("message",
                                                                     check=check, timeout=time_timeout)
                                    answer = answer.content
                                except TimeoutError:
                                    update_lucky_stats(inter.author.name, 0)
                                    return await inter.send(f'{inter.author.name} время вышло. Игра окончена.')

                                if str(answer).isdigit():
                                    if game == int(answer):
                                        msg = msg_win.replace('user', str(
                                            inter.author.name)).replace('number', str(game))
                                        add_user_money(inter.author.name, money_win)
                                        update_lucky_stats(inter.author.name, 1)
                                    else:
                                        msg = msg_lose.replace('number', str(game))
                                        update_lucky_stats(inter.author.name, 0)
                                    return await inter.send(msg)
                                else:
                                    msg = 'Нужно указать число от 1 до 100 (включительно).\n'
                                    msg += 'Начни игру заново.'
                                    return await inter.send(msg)
                            else:
                                msg = 'Нужно указать число от 1 до 100 (включительно).\n'
                                msg += 'Начни игру заново.'
                                return await inter.send(msg)
                        else:
                            msg = 'Нужно указать число от 1 до 100 (включительно).\n'
                            msg += 'Начни игру заново.'
                            return await inter.send(msg)
                    else:
                        msg = 'Нужно указать число от 1 до 100 (включительно).\n'
                        msg += 'Начни игру заново.'
                        return await inter.send(msg)
                else:
                    msg = 'Нужно указать число от 1 до 100 (включительно).\n'
                    msg += 'Начни игру заново.'
                    return await inter.send(msg)
            else:
                msg = 'Нужно указать число от 1 до 100 (включительно).\n'
                msg += 'Начни игру заново.'
                return await inter.send(msg)
        # else:
        #     channel = find_channel_by_name(self.bot, 'игры')
        #     embed = embed_wrong_channel(channel.mention, 'lucky_number')
        #
        #     await inter.send(embed=embed)

    # @commands.slash_command(name='ограбить')
    async def crime(self, inter: disnake.ApplicationCommandInteraction,
                    hero: str):
        '''Ограбить игрока.
        Ты можешь напасть попытаться ограбить игрока,
        но есть шанс быть пойманным. Вероятность успеха зависит от твоих навыков '''

        pass


def setup(bot: commands.Bot):
    bot.add_cog(Games(bot))
