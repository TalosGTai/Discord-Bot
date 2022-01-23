COGS:

1. Games

def update_stat(self, stat, game):
    изменение статы дуэлей
    winner - True/False (победа/поражение)

def update_money(self, user_money, money_win):
    # проверка условий с выигрышем монет
    # user_money - монеты пользователя
    # money_win - выигрышное количество монет


Rating:
Формула подсчёт рейтинга:
rate = msg + req_help + done_help + proj + duel + win_duel + day + bonus_rate

1msg = 0.01
1req_help = 0.05
1done_help = 0.5
1proj = 1.00
1duel = 0.03
1win_duel = 0.05
1day = 0.01
bonus_rate