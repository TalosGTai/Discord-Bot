import datetime as DT
from src.functions.main_func import date_to_days, to_two_digits


class User:
    def __init__(self, name: str, money: int=100, live_server: DT.date=DT.date.today(), \
        count_msg: int=0, count_req_help: int=0, count_done_help: int=0, count_projects: int=0, \
        bonus_rate: float=0, rate: float=0, duel_all_games: int=0, duel_win_games: int=0) -> None:
        self.name = name
        self.money = int(money)
        self.live_server = str(live_server)
        self.count_messages = int(count_msg)
        self.count_req_help = int(count_req_help)
        self.count_done_help = int(count_done_help)
        self.count_projects = int(count_projects)
        self.bonus_rate = float(bonus_rate)
        self.rate = float(rate)
        self.duel_all_games = int(duel_all_games)
        self.duel_win_games = int(duel_win_games)
        self.lucky_current_game = -1
        self.rate = self.calc_rate()


    def set_lucky_start_game(self):
        ''' Значение по умолчанию для "угадай число" '''

        self.lucky_current_game = -1


    def days_on_server(self) -> int:
        return date_to_days(self.live_server)
    
    
    def calc_rate(self) -> int:
        '''Формула рассчёта рейтинга пользователя'''
        
        self.rate = self.count_messages * 0.01 + self.count_req_help * \
            0.15 + self.count_done_help * 0.8 + self.count_projects * 3.0 + \
            self.duel_all_games * 0.01 + self.duel_win_games * 0.03 + \
            self.days_on_server() * 0.01 + self.bonus_rate
        self.rate = to_two_digits(self.rate)

        return self.rate


    def user_info(self) -> dict[str, int]:
        dict_user: dict = {}
        dict_user['count_msg'] = self.count_messages
        dict_user['count_req_help'] = self.count_req_help
        dict_user['count_done_help'] = self.count_done_help
        dict_user['count_count_proj'] = self.count_projects
        dict_user['rate'] = self.rate
        dict_user['money'] = self.money
        dict_user['date'] = self.days_on_server

        return dict_user


    def duel_stats(self) -> str:
        msg = f'Всего игр/побед: {self.duel_all_games}/{self.duel_win_games}'

        return msg
    

    def lucky_stats(self) -> str:
        msg = f'Всего игр/побед: {self.lucky_all_games}/{self.lucky_win_games}'

        return msg