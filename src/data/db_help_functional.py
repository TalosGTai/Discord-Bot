import random
import disnake
import src.data.data_base as db
from src.config import paths
import datetime as DT


def create_user(user):
    '''Создание пользователя в БД'''
    
    data_base = db.DB()
    users, stats, duel = divide_values(user)
    new_id = data_base.get_last_user_id() + 1

    print(users, new_id)

    data_base.insert_stats(stats, new_id)
    data_base.insert_users(users, new_id)
    data_base.insert_duel(duel, new_id)


def divide_values(values: list) -> tuple:
    '''Разделение значений для записи в БД'''

    users = [values.name, values.money, values.live_server]
    stats = [values.count_messages, values.count_req_help,
             values.count_done_help, values.count_projects,
             values.bonus_rate, values.rate]
    duels = [values.duel_all_games, values.duel_win_games]

    return (users, stats, duels)


def get_number_random_question(table: str) -> int | None:
    '''Получаем номер(id) рандомного вопроса для bot question'''

    data_base = db.DB()
    count_questions = data_base.get_count_records_in_table(table)

    if count_questions is not None:
        rnd = random.Random()
        return rnd.randint(1, count_questions)
    return None


def get_sql_query_question(id_question: int, table: str) -> str:
    '''Запрос на получение вопроса из таблицы [question]'''

    sql = f"SELECT question FROM discord.{table} " + \
        f"WHERE id_{table} = {id_question}"

    return sql


def get_id_random_task_complexity(number_task: int, complexity: str) -> int | None:
    '''Получаем номер рандомного таска определённой сложности'''

    data_base = db.DB()
    count_task = data_base.get_count_task_complexity(number_task, complexity)

    if count_task is not None and count_task != 0:
        rnd = random.Random()
        return rnd.randint(1, count_task)
    return None


def get_sql_query_rnd_task_complexity(number_task: int, complexity: str) -> str:
    '''Запрос на нахождение таска определённой сложности'''

    sql = f"SELECT id_ege_{number_task}, ege_{number_task}.theme, " + \
        f"ege_{number_task}.complexity, " + f'ege_{number_task}.type, ' + \
        f"ege_{number_task}.condition, " + f"ege_{number_task}.answer, " + \
        f'ege_{number_task}.author ' + \
        f"FROM courses.ege_{number_task} " + \
        f"WHERE complexity = \"{complexity}\""

    return sql


def get_dict_from_task(result: list) -> dict:
    '''Создаём словарь из списка значений таска
    
    keys: id_task, theme, complexity, type, codition, answer, author
    '''

    row = {'id_task': result[0], 'theme': result[1], 'complexity': result[2],
           'type': result[3], 'condition': result[4], 'answer': result[5],
           'author': result[6]}

    return row


def check_pic_condition(row: dict) -> bool:
    '''Проверяем есть ли картинка в нашем таске'''

    if 'pic' in row['condition']: return True
    return False


def check_txt_condition(row: dict) -> bool:
    '''Проверяем есть ли текстовые файлы в нашем таске'''

    if '.txt' in row['condition']: return True
    return False


def get_txt_from_task(number_task: int, row_task: dict) -> dict:
    '''Подружаем текстовые файлы для таска'''

    path_hook = paths['txt_path']
    id_task = row_task['id_task']
    path = f'{path_hook}{number_task}/{number_task}_{id_task}.txt'
    file = disnake.File(fp=path)
    row_task['txt'] = file

    return row_task


def get_pic_from_task(number_task: int, row_task: dict) -> dict:
    '''Подгружаем картинку из таска'''

    files = []
    rows = row_task['condition'].split('\n')
    id_task = row_task['id_task']
    condition = ''
    condition_lst = []
    count_rows = 1

    for row in rows:
        if 'pic' in row:
            path_hook = paths['img_path']
            path = f'{path_hook}{number_task}/{id_task}.{count_rows}.png'
            file = disnake.File(fp=path)
            files.append(file)
            count_rows += 1
            condition_lst.append(condition)
            condition = ''
        else:
            condition += row + '\n'

    if len(condition) > 0:
        condition_lst.append(condition)
        
    row_task['condition'] = condition_lst
    row_task['img'] = files
    
    return row_task


def get_task(number_task: int, complexity: str) -> dict | str:
    '''Получаем задачу по номеру и сложности
    
    При успешном получении возвращаем словарь (таск)
    Иначе, строку с ошибкой
    '''

    id_random_task = get_id_random_task_complexity(
        number_task, complexity)
    query = get_sql_query_rnd_task_complexity(
        number_task, complexity)
    
    if id_random_task is not None:
        data_base = db.DB()
        result = data_base.get_task_from_db(query)
        
        if result is not None:
            row = get_dict_from_task(result[id_random_task - 1])

            if check_pic_condition(row):
                row = get_pic_from_task(number_task, row)
            if check_txt_condition(row):
                row = get_txt_from_task(number_task, row)

            return row
        else:
            return f'Не удалось найти задачу по заданным параметрам: task = {number_task}'
    return f'Не удалось найти номер задачи заданной сложности: task = {number_task}, complexity = {complexity}'


def add_warn_to_user(user_name: str, type: str, description: str = '', time: int = 0) -> None:
    '''Добавить новое нарушение.
    Параметры БД: 
    • user_name: str;
    • type: str;
    • description: str;
    • date_start: date;
    • date_end: date;
    '''
    date_start = DT.date.today()
    date_end = date_start + DT.timedelta(minutes=time)

    data_base = db.DB()
    id_user = data_base.select_user(user_name)
    values = [id_user, type, description, date_start, date_end]

    data_base.insert_table_warns(values)