from random import randint
from src.functions.main_func import to_two_digits
from src.functions.discord import get_user_rate


def duel_algo(user_1: str, user_2: str) -> dict:
    all_rate = get_user_rate(user_1) + get_user_rate(user_2)
    winrate_user_1 = int(get_user_rate(user_1) / all_rate * 100)

    # чтобы не было дуэлей 100-0
    if winrate_user_1 == 0:
        winrate_user_1 = 1
    elif winrate_user_1 == 100:
        winrate_user_1 = 99

    winrate_rnd = randint(1, 99)
    res = dict()

    if winrate_rnd <= winrate_user_1:
        res['winner'] = user_1
        res['wr_w'] = winrate_user_1
        res['loser'] = user_2
        res['wr_l'] = 100 - winrate_user_1
    else:
        res['winner'] = user_2
        res['wr_w'] = 100 - winrate_user_1
        res['loser'] = user_1
        res['wr_l'] = winrate_user_1

    return res


def calculate_money_win(winrate_user_1: int, winrate_user_2: int,
                        money_1: int, money_2: int) -> int:
    '''Формула расчёта денег за победу'''

    money_win = min(winrate_user_1, winrate_user_2) * \
        min(money_1 / 100, money_2 / 100)

    if winrate_user_1 < winrate_user_2:
        money_win *= 1.15

    return int(money_win)


def update_money(user_money: int, money_win: int) -> float:
    '''Если у пользователя недостаточно денег,
    то отдаёт всё своё'''

    if user_money - money_win < 0: return user_money
    return money_win
