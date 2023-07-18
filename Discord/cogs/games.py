import Discord.session as session
from Discord.functions.main_func import find_user, load_phrases, embed_by_phrase, \
find_channel_by_name, embed_wrong_channel
from Discord.functions.duel_func import duel_algo, calculate_money_win
from disnake.ext import commands
import disnake
from random import randint


class Games(commands.Cog):
    '''Игры'''

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @commands.slash_command(name='дуэль')
    async def duel(self, inter: disnake.ApplicationCommandInteraction,
        противник: str):
        '''Вызов на дуэль другого игрока'''

        channels = ['игровой', 'чатимся']

        if str(inter.guild.get_channel(inter.channel.id)) in channels or \
                inter.author.display_name == 'gtai':
            hero = противник
            author = inter.author.name
            user1 = find_user(author, session.all_users)
            user1.count_messages -= 1
            user2 = find_user(hero, session.all_users)
            
            if user2 == False:
                msg = load_phrases('none')
                embed = embed_by_phrase(phrase)
                await inter.send(embed=embed)
            else:
                if user1.money == 0:
                    phrase = load_phrases('money-self')
                    embed = embed_by_phrase(phrase)
                    await inter.send(embed=embed)
                elif user2.money == 0:
                    msg = load_phrases('money-enemy')
                    embed = embed_by_phrase(phrase)
                    await inter.send(embed=embed)
                else:
                    # Проверка дуэли с ботом или самим собой
                    if user2.name == 'dina':
                        msg = load_phrases('bot')
                        embed = embed_by_phrase(phrase)
                        await inter.send(embed=embed)
                    elif user1.name == user2.name:
                        msg = load_phrases('self')
                        embed = embed_by_phrase(phrase)
                        await inter.send(embed=embed)
                    else:
                        res = duel_algo(user1, user2)
                        user_win = res['winner']
                        user_lose = res['loser']
                        wr1 = res['wr_w']
                        wr2 = res['wr_l']

                        user_win.duel_all_games += 1
                        user_win.duel_win_games += 1
                        user_lose.duel_all_games += 1
                        user_lose.duel_win_games -= 1
                        
                        money_win = calculate_money_win(
                            wr1, wr2, user_win.money, user_lose.money)
                        
                        user_win.money += money_win
                        user_lose.money -= money_win

                        # embed
                        msg = 'Дуэль между {} {}% и {} {}%\n'.format(
                            user_win.name, wr1, user_lose.name, wr2)
                        msg += '{} одержал победу в дуэли над {}\n'.format(
                            user_win.name, user_lose.name)
                        msg += 'И выиграл {} монет'.format(money_win)
                        
                        await inter.send(msg)
        else:
            channel = find_channel_by_name(self.bot, 'игровой')
            embed = embed_wrong_channel(channel.mention, 'duel')

            await inter.send(embed=embed)


    @commands.slash_command(name='угадай_число')
    async def lucky_number(self, inter: disnake.ApplicationCommandInteraction):
        '''Угадай число'''
        
        '''Правила игры очень просты:
            • загадано целое число от 1 до 100 (включительно)
            • у тебя 6 попыток
            • при каждой попытке ты будешь знать больше/меньше
            исходного числа ты находишься

        P.S. в строке должно находится только число (без посторонних символов)
        '''
        channels = ['игровой', 'чатимся']

        if str(inter.guild.get_channel(inter.channel.id)) in channels or \
                inter.author.display_name == 'gtai':
            user = find_user(inter.author.name, session.all_users)
            game = user.lucky_current_game
            money_win = 60
            msg_win = 'Поздравляю тебя user! Ты угадал число number! \n'
            msg_win += f'Твой выигрыш составил {money_win}.'
            msg_more = 'Я загадала число больше твоего'
            msg_less = 'Я загадала число меньше твоего'
            msg_lose = 'К сожалению, ты проиграл. Загаданное число: number'

            # проверка на начало игры
            if game == -1:
                game = randint(1, 100)
                msg = 'Напиши число от 1 до 100 (включительно) и угадай моё число!\n'
                msg += 'На ответ даётся 10 секунд.\n'
                msg += 'Твоя 1ая попытка, удачи!'
                await inter.send(msg)
                
                def check(m):
                    print(game)
                    return m.author == inter.author
                
                try:
                    answer = await self.bot.wait_for("message", check=check, timeout=10)
                    answer = answer.content
                except TimeoutError:
                    return await inter.send(f'{inter.author.name} время вышло. Игра окончена.')
                
                if str(answer).isdigit():
                    # первый ход
                    if game == int(answer):
                        msg = msg_win.replace('user', str(
                            inter.author.name)).replace('number', str(game))
                        user.set_lucky_start_game()
                        user.money += 60
                        return await inter.send(msg)
                    elif game > int(answer):
                        msg = msg_more
                    else:
                        msg = msg_less
                    
                    msg += '\n' + 'Твоя 2ая попытка'
                    await inter.send(msg)

                    # 2ой ход
                    try:
                        answer = await self.bot.wait_for("message", check=check, timeout=10)
                        answer = answer.content
                    except TimeoutError:
                        return await inter.send(f'{inter.author.name} время вышло. Игра окончена.')
                    
                    if str(answer).isdigit():
                        if game == int(answer):
                            msg = msg_win.replace('user', str(inter.author.name)).replace(
                                'number', str(game))
                            user.money += 60
                            user.set_lucky_start_game()
                            return await inter.send(msg)
                        elif game > int(answer):
                            msg = msg_more
                        else:
                            msg = msg_less

                        msg += '\n' + 'Твоя 3яя попытка'
                        await inter.send(msg)

                        # 3ий ход
                        try:
                            answer = await self.bot.wait_for("message", check=check, timeout=10)
                            answer = answer.content
                        except TimeoutError:
                            return await inter.send(f'{inter.author.name} время вышло. Игра окончена.')

                        if str(answer).isdigit():
                            if game == int(answer):
                                msg = msg_win.replace('user', str(inter.author.name)).replace(
                                    'number', str(game))
                                user.set_lucky_start_game()
                                user.money += 60
                                return await inter.send(msg)
                            elif game > int(answer):
                                msg = msg_more
                            else:
                                msg = msg_less

                            msg += '\n' + 'Твоя 4ая попытка'
                            await inter.send(msg)

                            # 4ый ход
                            try:
                                answer = await self.bot.wait_for("message", check=check, timeout=10)
                                answer = answer.content
                            except TimeoutError:
                                return await inter.send(f'{inter.author.name} время вышло. Игра окончена.')

                            if str(answer).isdigit():
                                if game == int(answer):
                                    msg = msg_win.replace('user', str(inter.author.name)).replace(
                                        'number', str(game))
                                    user.set_lucky_start_game()
                                    user.money += 60
                                    return await inter.send(msg)
                                elif game > int(answer):
                                    msg = msg_more
                                else:
                                    msg = msg_less

                                msg += '\n' + 'Твоя 5ая попытка. Ты сможешь!'
                                await inter.send(msg)

                                # 5ый ход
                                try:
                                    answer = await self.bot.wait_for("message", check=check, timeout=10)
                                    answer = answer.content
                                except TimeoutError:
                                    return await inter.send(f'{inter.author.name} время вышло. Игра окончена.')

                                if str(answer).isdigit():
                                    if game == int(answer):
                                        msg = msg_win.replace('user', str(
                                            inter.author.name)).replace('number', str(game))
                                        user.set_lucky_start_game()
                                        user.money += 60
                                        return await inter.send(msg)
                                    elif game > int(answer):
                                        msg = msg_more
                                    else:
                                        msg = msg_less
                                    
                                    msg += '\n' + 'Твоя последняя попытка. Пробуди свою силу!'
                                    await inter.send(msg)

                                    # 6ой ход
                                    try:
                                        answer = await self.bot.wait_for("message", check=check, timeout=10)
                                        answer = answer.content
                                    except TimeoutError:
                                        return await inter.send(f'{inter.author.name} время вышло. Игра окончена.')

                                    if str(answer).isdigit():
                                        if game == int(answer):
                                            msg = msg_win.replace('user', str(
                                                inter.author.name)).replace('number', str(game))
                                            user.money += 60
                                        elif game > int(answer):
                                            msg = msg_lose
                                        else:
                                            msg = msg_lose
                                        user.set_lucky_start_game()
                                        return await inter.send(msg)
                                    else:
                                        msg = 'Нужно указать число от 1 до 100 (включительно).\n'
                                        msg += 'Начни игру заново.'
                                        user.set_lucky_start_game()
                                        return await inter.send(msg)
                                else:
                                    msg = 'Нужно указать число от 1 до 100 (включительно).\n'
                                    msg += 'Начни игру заново.'
                                    user.set_lucky_start_game()
                                    return await inter.send(msg)
                            else:
                                msg = 'Нужно указать число от 1 до 100 (включительно).\n'
                                msg += 'Начни игру заново.'
                                user.set_lucky_start_game()
                                return await inter.send(msg)
                        else:
                            msg = 'Нужно указать число от 1 до 100 (включительно).\n'
                            msg += 'Начни игру заново.'
                            user.set_lucky_start_game()
                            return await inter.send(msg)
                    else:
                        msg = 'Нужно указать число от 1 до 100 (включительно).\n'
                        msg += 'Начни игру заново.'
                        user.set_lucky_start_game()
                        return await inter.send(msg)
                else:
                    msg = 'Нужно указать число от 1 до 100 (включительно).\n'
                    msg += 'Начни игру заново.'
                    user.set_lucky_start_game()
                    return await inter.send(msg)
        else:
            channel = find_channel_by_name(self.bot, 'игровой')
            embed = embed_wrong_channel(channel.mention, 'lucky_number')

            await inter.send(embed=embed)


    # @commands.slash_command(name='ограбить')
    async def crime(self, inter: disnake.ApplicationCommandInteraction,
        hero: str):
        '''Ограбить игрока'''
        
        '''Ты можешь напасть попытаться ограбить игрока,
        но есть шанс быть пойманным. 

        Вероятность успеха зависит от твоих навыков '''
        pass


    async def calculate_expressions(self, inter: disnake.ApplicationCommandInteraction):
        '''Вычислить выражения'''
        pass


def setup(bot: commands.Bot):
    bot.add_cog(Games(bot))
