from connect_db import mydb

def select_user(db, name):
    cursor = db.cursor()

    sql = "SELECT idUser \
    FROM users \
    WHERE name=\"" + name + "\""

    cursor.execute(sql)
    result = cursor.fetchone()

    return result[0]


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

    t.append(values[i].name)
    t.append(values[i].money)
    t.append(values[i].live_server)
    
    return t


def values_to_stats(i, values):
    t = []

    t.append(values[i].count_messages)
    t.append(values[i].count_req_help)
    t.append(values[i].count_done_help)
    t.append(values[i].count_projects)
    t.append(values[i].bonus_rate)
    t.append(values[i].rate)

    return t


def values_to_duel(i, values):
    t = []

    t.append(values[i].duel_all_games)
    t.append(values[i].duel_win_games)

    return t


def divide_values(values):
    users = []
    stats = []
    duels = []

    for i in range(len(values)):
        t1 = values_to_users(i, values)
        t2 = values_to_stats(i, values)
        t3 = values_to_duel(i, values)

        users.append(t1)
        stats.append(t2)
        duels.append(t3)

    return (users, stats, duels)


def update_algo(values):
    db = mydb()
    db.open_connect()
    users, stats, duel = divide_values(values)

    for i in range(len(users)):
        name = users[i][0]
        update_users(db.db, name, users[i])
        update_stats(db.db, name, stats[i])
        update_duel(db.db, name, duel[i])
    
    db.close_connect()