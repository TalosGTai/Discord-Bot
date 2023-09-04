import mysql.connector
from src.config import data_base
from src.data.db_help_functional import get_number_random_question, \
    get_sql_query_question
import datetime as DT


class DB:
    def __init__(self) -> None:
        self.__db_discord: mysql.connector.connection = None
        self.__db_course: mysql.connector.connection = None
        self.open_connect_courses()
        self.open_connect_discord()
        self.__cursor_discord = self.__db_discord.cursor()
        self.__cursor_course = self.__db_course.cursor()


    def open_connect_discord(self):
        try:
            self.__db_discord = mysql.connector.connect(
                host=data_base['host'],
                user=data_base['user'],
                password=data_base['password'],
                database=data_base['discord']
            )
        except mysql.connector.DatabaseError as db_error:
            print(f'Try to connect DB discord, error: {db_error}')
        except mysql.connector.Error as error:
            print(f'Something gone wrong, error: {error}')
        except Exception as ex:
            print(f'Something gone wrong, ex: {ex}')


    def open_connect_courses(self):
        try:
            self.__db_course = mysql.connector.connect(
                host=data_base['host'],
                user=data_base['user'],
                password=data_base['password'],
                database=data_base['courses']
            )
        except mysql.connector.DatabaseError as db_error:
            print(f'Try to connect DB courses, error: {db_error}')
        except mysql.connector.Error as error:
            print(
                f'Something gone wrong with connect DBcourses, error: {error}')
        except Exception as ex:
            print(f'Something gone wrong, ex: {ex}')
            

    def select_user(self, user_name: str) -> int | None:
        '''Ищем пользователя в БД по имени
        возвращаем id
        '''
        
        query = f"SELECT idUser \
        FROM users \
        WHERE name=\"{user_name}\""

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            result = self.__cursor_discord.fetchone()
            self.__cursor_discord.close()

            return result[0]
        except mysql.connector.InternalError as internal_error:
            print(f'Error with cursor in functions [select_user], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [select_user], error: {programming_error}')
        except mysql.connector.Error as error:
            print(f'Some error in functions [select_user], error: {error}')
        except Exception as ex:
            print(f'Something gone wrong in functions [select_user], ex: {ex}, txt: {user_name}')

        return None
    

    def get_user_money(self, user_id: int) -> int | None:
        '''Ищем количество монет полоьзователя по id'''

        query = f"SELECT money \
        FROM users \
        WHERE idUser=\"{user_id}\""

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            result = self.__cursor_discord.fetchone()
            self.__cursor_discord.close()

            return result[0]
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [get_user_money], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [get_user_money], error: {programming_error}')
        except mysql.connector.Error as error:
            print(f'Some error in functions [get_user_money], error: {error}')

        return None


    def get_user_bonus_rate(self, user_id: int) -> int | None:
        '''Ищем бонусный рейтинг пользователя в БД по id'''

        query = f"SELECT bonus_rate \
        FROM stats \
        WHERE idStat=\"{user_id}\""

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            result = self.__cursor_discord.fetchone()
            self.__cursor_discord.close()

            return result[0]
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [get_user_bonus_rate], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [get_user_bonus_rate], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [get_user_bonus_rate], error: {error}')

        return None
    

    def get_user_rate(self, user_id: int) -> int | None:
        '''Ищем рейтинг пользователя в БД по id'''

        query = f"SELECT rate \
        FROM stats \
        WHERE idStat=\"{user_id}\""

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            result = self.__cursor_discord.fetchone()
            self.__cursor_discord.close()

            return result[0]
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [get_user_rate], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [get_user_rate], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [get_user_rate], error: {error}')

        return None
    

    def get_user_count_msg(self, user_id: int) -> int | None:
        '''Ищем количество сообщений пользователя по id'''

        query = f"SELECT count_msg \
            FROM stats \
            WHERE idStat=\"{user_id}\""

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            result = self.__cursor_discord.fetchone()
            self.__cursor_discord.close()

            return result[0]
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [get_user_count_msg], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [get_user_count_msg], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [get_user_count_msg], error: {error}')

        return None


    def get_user_req_help(self, user_id: int) -> int | None:
        '''Ищем количество запросов помощи пользователя по id'''

        query = f"SELECT req_help \
            FROM stats \
            WHERE idStat=\"{user_id}\""

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            result = self.__cursor_discord.fetchone()
            self.__cursor_discord.close()

            return result[0]
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [get_user_req_help], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [get_user_req_help], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [get_user_req_help], error: {error}')

        return None


    def get_user_done_help(self, user_id: int) -> int | None:
        '''Ищем количество запросов помощи пользователя по id'''

        query = f"SELECT done_help \
            FROM stats \
            WHERE idStat=\"{user_id}\""

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            result = self.__cursor_discord.fetchone()
            self.__cursor_discord.close()

            return result[0]
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [get_user_done_help], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [get_user_done_help], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [get_user_done_help], error: {error}')

        return None


    def get_user_date(self, user_id: int) -> DT.datetime | None:
        '''Ищем дату регистрации пользователя по id'''

        query = f"SELECT date_registr \
            FROM users \
            WHERE idUser=\"{user_id}\""

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            result = self.__cursor_discord.fetchone()
            self.__cursor_discord.close()

            return result[0]
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [get_user_done_help], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [get_user_done_help], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [get_user_done_help], error: {error}')

        return None


    def get_duel_all_games(self, user_id: int) -> int | None:
        '''Ищем количество всех дуэлей пользователя по id'''

        query = f"SELECT all_games \
            FROM duel \
            WHERE idStats=\"{user_id}\""

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            result = self.__cursor_discord.fetchone()
            self.__cursor_discord.close()

            return result[0]
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [get_user_done_help], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [get_user_done_help], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [get_user_done_help], error: {error}')

        return None


    def get_duel_win_games(self, user_id: int) -> int | None:
        '''Ищем количество всех дуэлей пользователя по id'''

        query = f"SELECT win_games \
            FROM duel \
            WHERE idStats=\"{user_id}\""

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            result = self.__cursor_discord.fetchone()
            self.__cursor_discord.close()

            return result[0]
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [get_user_done_help], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [get_user_done_help], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [get_user_done_help], error: {error}')

        return None


    def add_user_count_msg(self, user_id: int, count_msg: int):
        '''Увеличиваем количество сообщений для пользователя по id'''

        query = f"UPDATE stats \
            SET count_msg = count_msg + {count_msg} \
            WHERE idStat = {user_id}"

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            self.__db_discord.commit()
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [add_user_count_msg], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [add_user_count_msg], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [add_user_count_msg], error: {error}')


    def add_user_bonus_rate(self, user_id: int, rate: int):
        '''Увеличиваем бонусный рейтинг пользователя по id'''

        query = f"UPDATE stats \
            SET bonus_rate = bonus_rate + {rate} \
            WHERE idStat = {user_id}"

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            self.__db_discord.commit()
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [add_user_bonus_rate], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [add_user_bonus_rate], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [add_user_bonus_rate], error: {error}')


    def add_user_rate(self, user_id: int, rate: int):
        '''Увеличиваем бонусный рейтинг пользователя по id'''

        query = f"UPDATE stats \
            SET rate = rate + {rate} \
            WHERE idStat = {user_id}"

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            self.__db_discord.commit()
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [add_user_rate], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [add_user_rate], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [add_user_rate], error: {error}')


    def add_user_money(self, user_id: int, money: int):
        '''Увеличиваем монеты пользователя по id'''

        query = f'UPDATE users \
            SET money = money + {money} \
            WHERE idUser = {user_id}'

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            self.__db_discord.commit()
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [add_user_money], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [add_user_money], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [add_user_money], error: {error}')


    def add_user_req_help(self, user_id: int, count: int):
        '''Увеличиваем/уменьшаем количество запросов помощи пользователя по id'''

        query = f"UPDATE stats \
                SET req_help = req_help + ({count}) \
                WHERE idStat = {user_id}"

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            self.__db_discord.commit()
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [add_user_req_help], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [add_user_req_help], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [add_user_req_help], error: {error}')


    def add_user_done_help(self, user_id: int, count: int):
        '''Увеличиваем/уменьшаем количество выполненной помощи пользователя по id'''

        query = f"UPDATE stats \
                SET done_help = done_help + ({count}) \
                WHERE idStat = {user_id}"

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            self.__db_discord.commit()
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [add_user_done_help], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [add_user_done_help], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [add_user_done_help], error: {error}')


    def add_user_count_proj(self, user_id: int, count: int):
        '''Увеличиваем/уменьшаем количество проектов пользователя по id'''

        query = f"UPDATE stats \
                SET count_proj = count_proj + ({count}) \
                WHERE idStat = {user_id}"

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            self.__db_discord.commit()
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [add_user_count_proj], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [add_user_count_proj], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [add_user_count_proj], error: {error}')


    def get_last_insert_id(self) -> int | None:
        '''Получаем индекс последнего добавленного пользователя'''

        query = 'SELECT LAST_INSERT_ID() from users'

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            cur_id = self.__cursor_discord.lastrowid
            self.__cursor_discord.close()

            return cur_id
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [get_last_insert_id], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [get_last_insert_id], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [get_last_insert_id], error: {error}')

        return None
    

    def get_last_user_id(self) -> int | None:
        '''Получаем индекс последнего добавленного пользователя'''
        
        query = 'SELECT MAX(idUser) from users'
        
        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            cur_id = self.__cursor_discord.fetchone()
            self.__cursor_discord.close()

            return cur_id[0]
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [get_last_insert_id], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [get_last_insert_id], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [get_last_insert_id], error: {error}')

        return None


    def get_count_task_complexity(self, number_task: int, complexity: str) -> int | None:
        '''Количество задач в номере определённой сложности'''

        query = f"SELECT count(type) FROM ege_{number_task} " + \
            "WHERE complexity = " + "\"" + complexity + "\""

        try:
            self.__cursor_course = self.__db_course.cursor()
            self.__cursor_course.execute(query)
            result = self.__cursor_course.fetchone()

            return int(result[0])
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [get_count_task_complexity], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [get_count_task_complexity], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [get_count_task_complexity], error: {error}')

        return None


    def get_task_from_db(self, query) -> list | None:
        '''По запросу возвращаем таск из таблицы [course]'''

        try:
            self.__cursor_course = self.__db_course.cursor()
            self.__cursor_course.execute(query)
            return self.__cursor_course.fetchall()
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [get_task_from_db], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [get_task_from_db], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [get_task_from_db], error: {error}')

        return None


    def get_question_from_db(self) -> str:
        '''Запрос в БД на получение вопроса из таблицы [questions]'''

        table = 'questions'
        id_random_question = get_number_random_question(table)

        if id_random_question is not None:
            query = get_sql_query_question(id_random_question, table)

            try:
                self.__cursor_course = self.__db_course.cursor()
                self.__cursor_discord.execute(query)
                result = self.__cursor_discord.fetchone()

                return result[0]
            except mysql.connector.InternalError as internal_error:
                print(
                    f'Error with cursor in functions [get_question_from_db], error: {internal_error}')
            except mysql.connector.ProgrammingError as programming_error:
                print(
                    f'Error with code, probably with syntax in functions [get_question_from_db], error: {programming_error}')
            except mysql.connector.Error as error:
                print(
                    f'Some error in functions [get_question_from_db], error: {error}')
        return None


    def set_user_money(self, user_id: int, money: int):
        '''Задаём монеты для пользователя по id'''

        query = f"UPDATE users \
            SET money = {money} \
            WHERE idUser = {user_id}"

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            self.__db_discord.commit()
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [set_user_money], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [set_user_money], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [set_user_money], error: {error}')


    def set_user_req_help(self, user_id: int, count: int):
        '''Задаём количество запросов помощи для пользователя по id'''

        query = f"UPDATE stats \
            SET req_help = {count} \
            WHERE idUser = {user_id}"

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            self.__db_discord.commit()
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [set_user_req_help], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [set_user_req_help], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [set_user_req_help], error: {error}')


    def set_user_done_help(self, user_id: int, count: int):
        '''Задаём количество выполненной помощи для пользователя по id'''

        query = f"UPDATE stats \
            SET req_done = {count} \
            WHERE idUser = {user_id}"

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            self.__db_discord.commit()
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [set_user_done_help], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [set_user_done_help], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [set_user_done_help], error: {error}')


    def set_user_rate(self, user_id: int, rate: int):
        '''Задаём рейтинг пользователя по id'''

        query = f"UPDATE stats \
            SET rate = {rate} \
            WHERE idUser = {user_id}"

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            self.__db_discord.commit()
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [set_user_money], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [set_user_money], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [set_user_money], error: {error}')


    def set_user_bonus_rate(self, user_id: int, rate: int):
        '''Задаём бонусный рейтинг пользователя по id'''

        query = f"UPDATE stats \
            SET bonus_rate = {rate} \
            WHERE idUser = {user_id}"

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            self.__db_discord.commit()
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [set_user_bonus_rate], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [set_user_bonus_rate], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [set_user_bonus_rate], error: {error}')


    def set_user_count_msg(self, user_id: int, count_msg: int):
        '''Задаём количество сообщений для пользователя по id'''

        query = f"UPDATE stats \
            SET count_msg = {count_msg} \
            WHERE idUser = {user_id}"

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            self.__db_discord.commit()
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [set_user_count_msg], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [set_user_count_msg], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [set_user_count_msg], error: {error}')


    def set_user_date(self, user_id: int, date: int):
        '''Задаём количество сообщений для пользователя по id'''

        query = f"UPDATE users \
            SET date_registr = {date} \
            WHERE idUser = {user_id}"

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            self.__db_discord.commit()
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [set_user_date], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [set_user_date], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [set_user_date], error: {error}')


    def insert_users(self, values: list, new_id: int):
        '''Вставка нового пользователя в БД [users]'''

        query = "INSERT INTO users \
        (name, money, idStat, date_registr) \
        VALUES (%s, %s, %s, %s)"

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            val = (values[0], values[1], new_id, values[2])
            self.__cursor_discord.execute(query, val)

            self.__db_discord.commit()
            self.__cursor_discord.close()

            print('Success insert user.')
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [insert_users], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [insert_users], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [insert_users], error: {error}')


    def insert_stats(self, values: list, new_id: int):
        '''Добавление статистики пользователя в таблицу [stats] БД'''

        query = "INSERT INTO stats \
        (count_msg, req_help, done_help, count_proj, bonus_rate, rate, idDuel) \
        VALUES ( %s, %s, %s, %s, %s, %s, %s)"

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            values.append(new_id)
            self.__cursor_discord.execute(query, values)
            self.__db_discord.commit()
            self.__cursor_discord.close()

            print('Success insert stats.')
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [insert_stats], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [insert_stats], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [insert_stats], error: {error}')
            

    def insert_duel(self, values: list, new_id: int):
        '''Добавление статистики для дуэлей пользователя в таблицу [duels] БД'''

        query = "INSERT INTO duel \
        (idStats, all_games, win_games) \
        VALUES ( %s, %s, %s)"

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            val = (new_id, values[0], values[1])
            self.__cursor_discord.execute(query, val)
            self.__db_discord.commit()
            self.__cursor_discord.close()

            print('Success insert duel.')
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [insert_duel], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [insert_duel], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [insert_duel], error: {error}')


    def update_duel_stats(self, user_name: str, result_duel: int):
        '''Обновление в таблице дуэль'''

        idStat = self.select_user(user_name)

        query = f'UPDATE duel \
        SET all_games = all_games + 1, win_games = win_games + {result_duel} \
        WHERE idDuel = {idStat}'
        
        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            self.__db_discord.commit()
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [update_duel_stats], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [update_duel_stats], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [update_duel_stats], error: {error}')


    def get_count_records_in_table(self, table: str) -> int | None:
        '''Количество записей в таблице'''

        query = f"SELECT count({'id_'+table}) \
        FROM {table}"

        try:
            self.__cursor_discord = self.__db_discord.cursor()
            self.__cursor_discord.execute(query)
            result = self.__cursor_discord.fetchone()

            return int(result[0])
        except mysql.connector.InternalError as internal_error:
            print(
                f'Error with cursor in functions [get_count_records_in_table], error: {internal_error}')
        except mysql.connector.ProgrammingError as programming_error:
            print(
                f'Error with code, probably with syntax in functions [get_count_records_in_table], error: {programming_error}')
        except mysql.connector.Error as error:
            print(
                f'Some error in functions [get_count_records_in_table], error: {error}')


    def update_table_stats(self, name: str, values: list):
        '''Обновление таблицы [stats] пользователя'''

        idStat = self.select_user(name)

        if idStat is not None:
            values.append(idStat)

            query = "UPDATE stats \
            SET count_msg = %s, req_help = %s, done_help = %s, count_proj = %s, \
                bonus_rate = %s, rate = %s \
            WHERE idStat = %s"

            try:
                self.__cursor_discord = self.__db_discord.cursor()
                self.__cursor_discord.execute(query, values)
                self.__db_discord.commit()
            except mysql.connector.InternalError as internal_error:
                print(
                    f'Error with cursor in functions [update_table_stats], error: {internal_error}')
            except mysql.connector.ProgrammingError as programming_error:
                print(
                    f'Error with code, probably with syntax in functions [update_table_stats], error: {programming_error}')
            except mysql.connector.Error as error:
                print(
                    f'Some error in functions [update_table_stats], error: {error}')


    def update_table_users(self, name: str, values: list):
        '''Обновление таблицы [users] пользователя'''
        idStat = self.select_user(name)

        if idStat is not None:
            val = [values[1], idStat]

            query = "UPDATE users \
            SET money = %s \
            WHERE idUser = %s"

            try:
                self.__cursor_discord = self.__db_discord.cursor()
                self.__cursor_discord.execute(query, val)
                self.__db_discord.commit()
            except mysql.connector.InternalError as internal_error:
                print(
                    f'Error with cursor in functions [update_table_users], error: {internal_error}')
            except mysql.connector.ProgrammingError as programming_error:
                print(
                    f'Error with code, probably with syntax in functions [update_table_users], error: {programming_error}')
            except mysql.connector.Error as error:
                print(
                    f'Some error in functions [update_table_users], error: {error}')
    