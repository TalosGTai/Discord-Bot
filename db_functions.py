from connect_db import mydb
import session

def select_user(db, name):
    cursor = db.cursor()

    sql = "SELECT idUser \
    FROM users \
    WHERE name=\"" + name + "\""

    cursor.execute(sql)
    result = cursor.fetchone()

    return result[0]


def get_last_insert_id(db):
    cursor = db.cursor()
    sql = 'SELECT LAST_INSERT_ID() from users'
    cursor.execute(sql)
    cur_id = cursor.lastrowid
    cursor.close()

    return cur_id


def get_last_user_id(db):
    cursor = db.cursor()
    sql = 'SELECT MAX(idUser) from users'
    cursor.execute(sql)
    cur_id = cursor.fetchone()
    cursor.close()

    return cur_id[0]


def insert_users(db, values, new_id):
    cursor = db.cursor()
    
    sql = "INSERT INTO users \
    (name, money, idStat, date_registr) \
    VALUES (%s, %s, %s, %s)"
    #val = (1, GTai, 12040, 1, 2021-10-10)
    val = (values[0], values[1], new_id, values[2])
    cursor.execute(sql, val)

    db.commit()
    cursor.close()
    print('Success insert user.')


def insert_stats(db, values, new_id):
    cursor = db.cursor()

    sql = "INSERT INTO stats \
    (count_msg, req_help, done_help, count_proj, bonus_rate, rate, idDuel) \
    VALUES ( %s, %s, %s, %s, %s, %s, %s)"
    #val = (1557, 0, 2, 0, 0, 47.91, id)

    values.append(new_id)
    cursor.execute(sql, values)
    db.commit()
    cursor.close()
    print('Success insert stats.')


def insert_duel(db, values, new_id):
    cursor = db.cursor()

    sql = "INSERT INTO duel \
    (idStats, all_games, win_games) \
    VALUES ( %s, %s, %s)"
    #val = (1, 100, 60)

    val = (new_id, values[0], values[1])
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    print('Success insert duel.')


def update_users(db, name, values):
    idStat = select_user(db, name)
    val = [values[1], idStat]
    cursor = db.cursor()

    sql = "UPDATE users \
    SET money = %s \
    WHERE idUser = %s"

    cursor.execute(sql, val)
    db.commit()


def update_stats(db, name, values):
    idStat = select_user(db, name)
    values.append(idStat)
    cursor = db.cursor()

    sql = "UPDATE stats \
    SET count_msg = %s, req_help = %s, done_help = %s, count_proj = %s, \
         bonus_rate = %s, rate = %s \
    WHERE idStat = %s"

    cursor.execute(sql, values)
    db.commit()


def update_duel(db, name, values):
    idStat = select_user(db, name)
    values.append(idStat)
    cursor = db.cursor()

    sql = "UPDATE duel \
    SET all_games = %s, win_games = %s \
    WHERE idDuel = %s"

    cursor.execute(sql, values)
    db.commit()


def values_to_users(i, values):
    t = []

    if i == -1:
        t.append(values.name)
        t.append(values.money)
        t.append(values.live_server)
    else:
        t.append(values[i].name)
        t.append(values[i].money)
        t.append(values[i].live_server)
    
    return t


def values_to_stats(i, values):
    t = []

    if i == -1:
        t.append(values.count_messages)
        t.append(values.count_req_help)
        t.append(values.count_done_help)
        t.append(values.count_projects)
        t.append(values.bonus_rate)
        t.append(values.rate)
    else:
        t.append(values[i].count_messages)
        t.append(values[i].count_req_help)
        t.append(values[i].count_done_help)
        t.append(values[i].count_projects)
        t.append(values[i].bonus_rate)
        t.append(values[i].rate)

    return t


def values_to_duel(i, values):
    t = []

    if i == -1:
        t.append(values.duel_all_games)
        t.append(values.duel_win_games)
    else:
        t.append(values[i].duel_all_games)
        t.append(values[i].duel_win_games)

    return t


def divide_values(values, count):
    users = []
    stats = []
    duels = []

    if count > 1:
        for i in range(count):
            t1 = values_to_users(i, values)
            t2 = values_to_stats(i, values)
            t3 = values_to_duel(i, values)

            users.append(t1)
            stats.append(t2)
            duels.append(t3)
    else:
        t1 = values_to_users(-1, values)
        t2 = values_to_stats(-1, values)
        t3 = values_to_duel(-1, values)

        users.append(t1)
        stats.append(t2)
        duels.append(t3)

    return (users, stats, duels)


def update_algo(values):
    db = mydb()
    db.open_connect()
    users, stats, duel = divide_values(values, len(values))

    for i in range(len(users)):
        name = users[i][0]
        # add try
        update_users(db.db, name, users[i])
        update_stats(db.db, name, stats[i])
        update_duel(db.db, name, duel[i])
    
    db.close_connect()


def create_user(user):
    db = mydb()
    db.open_connect()

    users, stats, duel = divide_values(user, 1)
    new_id = get_last_user_id(db.db) + 1

    print(users, new_id)

    insert_stats(db.db, stats[0], new_id)
    insert_users(db.db, users[0], new_id)
    insert_duel(db.db, duel[0], new_id)

    db.close_connect()


# index - stat_index
# value - fill the value all users
def add_stat(index):
    pass