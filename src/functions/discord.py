from src.data.data_base import DB
import datetime as DT


def find_channel_by_name(bot, source_channel: str):
    '''Поиск канала по названию канала'''

    for guild in bot.guilds:
        for channel in guild.channels:
            if channel.name == source_channel:
                return channel
    return False


def find_user_by_name_discord(bot, user_name: str):
    '''Поиск пользователя по имени в дискорд-сервере'''
    
    for guild in bot.guilds:
        for member in guild.members:
            if member.name == user_name:
                return member
    return False


def find_user(user_name: str) -> bool:
    '''Поиск пользователя по имени в БД'''

    db = DB()

    if db.select_user(user_name) is None:
        return False
    return True


def get_user_money(user_name: str) -> int | None:
    '''Получаем количество монет пользователя'''

    db = DB()
    user_id = db.select_user(user_name)

    if user_id is not None:
        return db.get_user_money(user_id)
    return None


def get_user_rate(user_name: str) -> int | None:
    '''Получаем рейтинг пользователя'''

    db = DB()
    user_id = db.select_user(user_name)

    if user_id is not None:
        return db.get_user_rate(user_id)
    return None


def get_user_bonus_rate(user_name: str) -> int | None:
    '''Получаем бонусный рейтинг пользователя'''

    db = DB()
    user_id = db.select_user(user_name)

    if user_id is not None:
        return db.get_user_bonus_rate(user_id)
    return None


def get_user_duel_all_games(user_name: str) -> int | None:
    '''Получаем бонусный рейтинг пользователя'''

    db = DB()
    user_id = db.select_user(user_name)

    if user_id is not None:
        return db.get_duel_all_games(user_id)
    return None


def get_user_duel_win_games(user_name: str) -> int | None:
    '''Получаем бонусный рейтинг пользователя'''

    db = DB()
    user_id = db.select_user(user_name)

    if user_id is not None:
        return db.get_duel_win_games(user_id)
    return None


def get_user_date(user_name: str) -> DT.datetime | None:
    '''Получаем дату регистрации пользователя'''

    db = DB()
    user_id = db.select_user(user_name)

    if user_id is not None:
        return db.get_user_date(user_id)
    return None


def add_user_bonus_rate(user_name: str, rate: int):
    '''Добавляем пользователю бонусный рейтинг'''

    db = DB()
    user_id = db.select_user(user_name)

    if user_id is not None:
        db.add_user_bonus_rate(user_id, rate)


def add_user_rate(user_name: str, rate: int):
    '''Добавляем пользователю рейтинг'''

    db = DB()
    user_id = db.select_user(user_name)

    if user_id is not None:
        db.add_user_rate(user_id, rate)


def add_user_count_msg(user_name: str, count: int):
    '''Добавляем пользователю количество сообщений'''

    db = DB()
    user_id = db.select_user(user_name)

    if user_id is not None:
        db.add_user_count_msg(user_id, count)


def add_user_money(user_name: str, money: int):
    '''Добавляем/вычитаем у пользователя монеты'''

    db = DB()
    user_id = db.select_user(user_name)

    if user_id is not None:
        db.add_user_money(user_id, money)


def add_user_req_help(user_name: str, count: int):
    '''Добавляем/вычитаем у пользователя количество запросов помощи'''

    db = DB()
    user_id = db.select_user(user_name)

    if user_id is not None:
        db.add_user_req_help(user_id, count)


def add_user_done_help(user_name: str, count: int):
    '''Добавляем/вычитаем у пользователя количество выполненной помощи'''

    db = DB()
    user_id = db.select_user(user_name)

    if user_id is not None:
        db.add_user_done_help(user_id, count)


def add_user_count_proj(user_name: str, count: int):
    '''Добавляем/вычитаем у пользователя количество проектов'''

    db = DB()
    user_id = db.select_user(user_name)

    if user_id is not None:
        db.add_user_count_proj(user_id, count)


def set_user_req_help(user_name: str, count: int):
    '''Задаём у пользователя количество запросов помощи'''

    db = DB()
    user_id = db.select_user(user_name)

    if user_id is not None:
        db.set_user_req_help(user_id, count)


def set_user_done_help(user_name: str, count: int):
    '''Задаём у пользователя количество выполненной помощи'''

    db = DB()
    user_id = db.select_user(user_name)

    if user_id is not None:
        db.set_user_done_help(user_id, count)


def set_user_date_registr(user_name: str, date: str):
    '''Изменяем у пользователя дату регистрации на сервере'''

    db = DB()
    user_id = db.select_user(user_name)

    if user_id is not None:
        db.set_user_date(user_id, date)


def update_duel_stats(user_win: str, user_lose: str):
    '''Обновление статистики после дуэли'''

    db = DB()

    db.update_duel_stats(user_win, 1)
    db.update_duel_stats(user_lose, -1)