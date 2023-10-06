import datetime as DT
from random import randint
from src.data.data_base import DB


def to_two_digits(num: float) -> float:
    '''Преобразовываем к 2ум знакам после запятой'''

    return int(num * 100) / 100

def date_to_days(user_date: str) -> int:
    '''Количество дней от даты до текущего дня'''

    # datetime.date
    date = str(user_date).split('-')
    date = DT.date(int(date[0]), int(date[1]), int(date[2]))
    days = abs(int((date - DT.date.today()).days))

    return days

def get_days(day: int) -> dict[int, str]:
    '''Окончания для даты (дня, дней)'''

    days = {
        0: 'дней',
        1: 'день',
        2: 'дня',
        3: 'дня',
        4: 'дня',
        5: 'дней',
        6: 'дней',
        7: 'дней',
        8: 'дней',
        9: 'дней',
        10: 'дней',
        11: 'дней',
        12: 'дней',
        13: 'дней',
        14: 'дней',
        15: 'дней',
        16: 'дней',
        17: 'дней',
        18: 'дней',
        19: 'дней',
        20: 'дней',
    }

    day = day % 100

    if day in days.keys():
        return days[day]
    else:
        day = day % 10
        return days[day]

def time_format(time: str) -> str:
    ''' На вход подаётся строка формата: х или хх.
    Дописываем 0, если нужно.
    '''
    
    if len(time) == 1: return '0' + time
    return time

def delete_reverse_slash(s: str) -> str:
    if s.find('\\') == -1:
        return s
    return s[:s.find('\\'):] + s[s.find('\\') + 1::]

def create_password(complexity: str, length: int) -> str:
    '''Генерация пароля по заданной сложности и длине'''

    alphabet = [chr(c) for c in range(ord('a'), ord('z') + 1)]
    alphabet += [chr(c) for c in range(ord('A'), ord('Z') + 1)]
    digits = [chr(c) for c in range(ord('0'), ord('9') + 1)]
    special = ['`', '!', '@', ',', '.', '#', '$', '%', '^', '&', '*', '?', ':', '/', '\\', '_', '~']
    password = ''
    
    match complexity:
        case 'easy':
            for i in range(length):
                x = randint(0,  len(alphabet) - 1)
                password += alphabet[x]
        case 'medium':
            alphabet += digits
            for i in range(length):
                x = randint(0,  len(alphabet) - 1)
                password += alphabet[x]
        case 'hard':
            count_special = max(1, length // 3)
            for i in range(length):
                choice_symb = randint(1, 2)
                if choice_symb == 2 and count_special > 0:
                    x = randint(0, len(special) - 1)
                    password += special[x]
                    count_special -= 1
                else:
                    x = randint(0,  len(alphabet) - 1)
                    password += alphabet[x]

    return password

def get_complexity() -> dict[str, list[str]]:
    '''Словарь для понимания выбора сложности'''

    complexity = {
        'easy': ['лёгкая', 'легкая', 'easy', 'изи', 'лёгкий', 'начальный'], 
        'medium': ['средняя', 'meduim', 'середина', 'норм', 'норма', 'средний', 'обычный'],
        'hard': ['тяжёлая', 'тяжёлый', 'hard', 'хард', 'трудно', 'сильно',
                'сложная', 'сложный', 'сложно', 'жёсткий']
        }
    return complexity

def get_key_by_value(value: str, categories_dict: dict[str, list[str]]) -> str | bool:
    '''Проверка значения на нахождения в словаре
    возвращаем ключ от этого значения
    '''

    for key in categories_dict.keys():
        if value in categories_dict[key]:
            return key
    return False

def load_phrases(type='social', game='', action='not_exist') -> str:
    '''Подгрузка фраз для общения
    
    type: games, social
    game: duel
    '''

    path = f'./data/phrases/{type}/'

    match (type):
        case 'games':
            match (game):
                case 'duel':
                    match (action):
                        case 'bot':
                            f = open(f'{path}{game}/{action}.txt',
                                     encoding='UTF-8')
                        case 'self':
                            f = open(f'{path}{game}/{action}.txt',
                                     encoding='UTF-8')
                        case 'none':
                            f = open(f'{path}{game}/{action}.txt',
                                     encoding='UTF-8')
                        case 'money_self':
                            f = open(f'{path}{game}/{action}.txt',
                                     encoding='UTF-8')
                        case 'money_enemy':
                            f = open(f'{path}{game}/{action}.txt',
                                     encoding='UTF-8')
        case 'social':
            match (action):
                case 'not_exist':
                    f = open(f'{path}/{action}.txt', encoding='UTF-8')
                case 'transfer_money_hero':
                    f = open(f'{path}/{action}.txt', encoding='UTF-8')
                case 'transfer_money_self':
                    f = open(f'{path}/{action}.txt', encoding='UTF-8')

    strings_actions = f.readlines()
    num_string = randint(0, len(strings_actions) - 1)
    f.close()

    return strings_actions[num_string]

def write_to_file(file_name: str, msg: str) -> None:
    file_strings = get_strings_from_file(file_name, msg)
    file_strings += [msg]
    f = open(f'logs/{file_name}.txt')
    f.readlines(file_strings)
    f.close()

def get_strings_from_file(file_name: str) -> list[str]:
    f = open(f'logs/{file_name}.txt')
    file_strings = f.readlines()
    file_strings[-1] += '\n'
    f.close()

    return file_strings