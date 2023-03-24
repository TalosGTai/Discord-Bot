import session
from functions import find_user, load_phrases, duel_algo
from functions import calculate_money_win, embed_by_phrase
from disnake.ext import commands
import disnake


class Games(commands.Cog):
    '''Игры'''

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @commands.slash_command(name='дуэль')
    async def duel(self, inter: disnake.ApplicationCommandInteraction,
        противник: str):
        '''Вызов на дуэль другого игрока'''

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
                if user2.name == 'Dina':
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


    # @commands.slash_command(name='угадай_число')
    async def lucky_number(self, inter: disnake.ApplicationCommandInteraction):
        '''Угадай число'''
        
        '''Правила игры очень просты:
            • загадано целое число от 1 до 100 (включительно)
            • у тебя 6 попыток
            • при каждой попытке ты будешь знать больше/меньше
            исходного числа ты находишься

        P.S. в строке должно находится только число (без посторонних символов)
        '''
        pass


    # @commands.slash_command(name='ограбить')
    async def crime(self, inter: disnake.ApplicationCommandInteraction,
        hero: str):
        '''Ограбить игрока'''
        
        '''Ты можешь напасть попытаться ограбить игрока,
        но есть шанс быть пойманным. 

        Вероятность успеха зависит от твоих навыков '''
        pass


def setup(bot: commands.Bot):
    bot.add_cog(Games(bot))
