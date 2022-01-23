import session, functions
from discord.ext import commands
from discord.utils import get


class Games(commands.Cog):
    '''Игры'''
    def __init__(self, client) -> None:
        self.client = client


    @commands.cooldown(rate=1, per=1, type=commands.BucketType.user)
    @commands.command()
    async def duel(self, ctx, hero):
        '''Вызов на дуэль другого игрока
        
        Старайся вызывать более сильных противников, Геральт бы одобрил!

        Пример: .duel GTai 
        '''
        author = ctx.message.author.name
        user1 = functions.find_user(author, session.all_users)
        user2 = functions.find_user(hero, session.all_users)

        if int(user1.money) == 0:
            msg = 'Монет нет, дуэли не будет\n'
            msg += 'Нужно работать, бездельник'

            await ctx.send(msg)
        elif int(user2.money) == 0:
            await ctx.send(f'У {hero} нет монет :(')
        else:
            # Проверка дуэли с ботом или самим собой
            if user2 and user2.name == 'Dina':
                await ctx.send(f'Рано тебе ещё с ведьмачкой тягаться, смерд')
            elif user2 and user1.name == user2.name:
                await ctx.send(f'С собой сражаться бессмысленно')
            else:
                res = functions.duel_algo(user1, user2)
                user_win = res['winner']
                user_lose = res['loser']
                wr1 = res['wr_w']
                wr2 = res['wr_l']

                user_win.duel = functions.update_duel_stat(user_win.duel, True)
                user_lose.duel = functions.update_duel_stat(
                    user_lose.duel, False)
                money_win = functions.calculate_money_win(
                    wr1, wr2, user_win.money, user_lose.money)
                
                user_win.money += money_win
                user_lose.money -= money_win

                msg = 'Дуэль между {} {}% и {} {}%\n'.format(
                    user_win.name, wr1, user_lose.name, wr2)
                msg += '{} одержал победу в дуэли над {}\n'.format(
                    user_win.name, user_lose.name)
                msg += 'И выиграл {} монет'.format(money_win)
                
                await ctx.send(msg)


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def duel_top(self, ctx):
        '''Топ 5 дуэлянтов этой эпохи
        
        Сюда попадают лучшие из лучших
        Участвуй в дуэлях, выигрывай и станешь одним из них!
        
        Попасть можно только от 30 дуэлей
        '''
        author = ctx.message.author.name
        duel_stat = []
        for user in session.all_users:
            temp_stats = list(user.duel.split('-'))
            all_games = int(temp_stats[0])
            win_games = int(temp_stats[1])
            if win_games != 0:
                percent_win = int((win_games/all_games) * 100)
            else:
                percent_win = 0

            duel_stat.append((user.name, user.duel, percent_win))

        duel_stat = sorted(duel_stat, key=lambda user: user[2])
        
        j = len(duel_stat) - 1
        res = [duel_stat[i] for i in range(j, j - 5, -1)]
        
        rate_duel = 'Топ 5 лучших дуэлянтов этой эпохи:\n'
        rate_duel += '{} - {} {}'.format(1, res[0][0], res[0][1])

        for i in range(1, len(res)):
            wr = int(100 * res[i][1]/res[i][0])
            rate_duel += '\n{} - {} {}  {}%'.format(i + 1, res[i][0], res[i][1], wr)

        await ctx.send(rate_duel)
       

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def duel_info(self, ctx, hero):
        '''Статистика в дуэлях
        
        Шаблон: .duel_info name
        Пример: .duel_info GTai
        '''
        author = ctx.message.author.name

        user = functions.find_user(hero, session.all_users)
        temp_stat = list(user.duel.split('-'))
        all_games = int(temp_stat[0])
        win_games = int(temp_stat[1])
        wr = int((win_games/all_games) * 100)

        await ctx.send(f'Статы {user.name}\n{user.duel_stats()}, {wr}%')


def setup(client):
    client.add_cog(Games(client))