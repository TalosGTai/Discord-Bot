from random import randint

# +1 win and +1 game
def duel_update_stat(stat, game):
    s = list(stat.split('-'))
    all_games = int(s[0]) + 1

    if game:
        win_games = int(s[1]) + 1
    else:
        win_games = int(s[1])

    res = str(all_games) + '-' + str(win_games)

    return res


def duel_algo(user1, user2):
    all_rate = user1.rate + user2.rate
    w1 = int(user1.rate / all_rate * 100)

    # чтобы не было дуэлей 100-0
    if w1 == 0:
        w1 = 1
    elif w1 == 100:
        w1 = 99

    w = randint(1, 100)
    m1 = w1
    res = dict()

    if w <= m1:
        res['winner'] = user1
        res['wr_w'] = w1
        res['loser'] = user2
        res['wr_l'] = 100 - w1
    else:
        res['winner'] = user2
        res['wr_w'] = 100 - w1
        res['loser'] = user1
        res['wr_l'] = w1

    return res


# Формула расчёт денег на победу
def calculate_money_win(wr1, wr2, money1, money2):
    money_win = min(wr1, wr2) * min(money1 / 100, money2 / 100)
    
    if wr1 < wr2:
        money_win *= (wr2/wr1)
    
    return to_two_digits(money_win)


def update_duel_stat(stat, game):
    s = list(stat.split('-'))
    all_games = int(s[0]) + 1

    if game:
        win_games = int(s[1]) + 1
    else:
        win_games = int(s[1])

    res = str(all_games) + '-' + str(win_games)

    return res


# check < 0 and to view: xxx.xx
def update_money(user_money, money_win):
    # проверка на отрицательное количество монет
    if user_money - money_win < 0:
        money_win = user_money

    money_win = to_two_digits(money_win)

    return money_win


# convert number to two digits
def to_two_digits(num):
    return int(num * 100) / 100


def find_user(name, all_users):
    for user in all_users:
        if user.name == name:
            return user

    return False