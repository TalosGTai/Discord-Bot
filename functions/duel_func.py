from random import randint
from main_func import to_two_digits

def duel_algo(user1, user2) -> dict:
    all_rate = user1.rate + user2.rate
    winrate_user_1 = int(user1.rate / all_rate * 100)

    # чтобы не было дуэлей 100-0
    if winrate_user_1 == 0:
        winrate_user_1 = 1
    elif winrate_user_1 == 100:
        winrate_user_1 = 99

    winrate_rnd: int = randint(1, 99)
    res = dict()

    if winrate_rnd <= winrate_user_1:
        res['winner'] = user1
        res['wr_w'] = winrate_user_1
        res['loser'] = user2
        res['wr_l'] = 100 - winrate_user_1
    else:
        res['winner'] = user2
        res['wr_w'] = 100 - winrate_user_1
        res['loser'] = user1
        res['wr_l'] = winrate_user_1

    return res


# Формула расчёт денег на победу
def calculate_money_win(winrate_user_1: int, winrate_user_2: int, money_1: float, money_2: float) -> float:
    money_win = min(winrate_user_1, winrate_user_2) * \
        min(money_1 / 100, money_2 / 100)

    if winrate_user_1 < winrate_user_2:
        money_win *= 1.1

    return to_two_digits(money_win)


# +1 win and +1 game
def update_duel_stat(stat, game: bool) -> str:
    all_games = int(stat[0]) + 1

    if game:
        win_games = int(stat[1]) + 1
    else:
        win_games = int(stat[1])

    return f'{all_games}-{win_games}'


# check < 0 and to view: xxx.xx
def update_money(user_money: float, money_win: float) -> float:
    # проверка на отрицательное количество монет
    if user_money - money_win < 0:
        money_win = user_money

    money_win = to_two_digits(money_win)

    return money_win
