from random import randint
import datetime as DT


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
        money_win *= 1.1
    
    return to_two_digits(money_win)

# +1 win and +1 game
def update_duel_stat(stat, game):
    pass
    all_games = int(stat[0]) + 1

    if game:
        win_games = int(stat[1]) + 1
    else:
        win_games = int(stat[1])

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

# Количество дней от даты до текущего дня
def date_to_days(user_date):
    date = user_date.split('-')
    date = DT.date(int(date[0]), int(date[1]), int(date[2]))
    days = abs(int((DT.date.today() - date).days))

    return days

# окончания для даты (дня, дней)
def get_days(day):
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

# на вход подаётся число (х или хх) -> xx
def time_format(time):
    if len(time) == 1:
        time = '0' + time
    
    return time

# who = Dina/hero/
def some_phrases(who):
    match(who):
        case 'Dina':
            pass
            #sentences = []'')
        case 'hero':
            pass

# title, description, color
def ege_24_text_1():
    title_msg = 'Видео-курс 24 Задание ЕГЭ Информатика'

    description_msg = 'Хочешь понять строки и уметь решать все 24ые номера?\n'
    description_msg += 'Тогда это то, что тебе нужно!\n\n'
    description_msg += 'Что входит в курс:\n'
    description_msg += '• Основы строк\n'
    description_msg += '• Срезы\n'
    description_msg += '• Разбор множества заданий(всё что только может попасться)\n'
    description_msg += '  + задания с последних лет из реальных ЕГЭ\n\n'
    description_msg += 'Общая длительность курса: ~2 часа.\n\n'
    description_msg += 'Источники задач:\n'
    description_msg += '1) Реальные задания с ЕГЭ\n'
    description_msg += '2) КПоляков\n'
    description_msg += '3) Мои тренировочные задания\n\n'
    description_msg += 'Самая основная теория + большое количество практических разборов и советов от меня.\n\n'
    description_msg += '💻Как это проходит:\n'
    description_msg += 'Это закрытый видеокурс, находящийся на YouTube.'
    color_msg = 0x5ACFF5

    return (title_msg, description_msg, color_msg)

def ege_24_text_2(owner):
    text = 'Чтобы получить доступ к Курсу нужно:\n'
    text += '1. Перевести на карту сбербанка 290р. с текстом сообщения: "Инфа24"\n'
    text += 'на карту: 4276 0800 1585 5878\n'
    text += '2. Сделать скрин успешного перевода или скрин на последние 4 цифры карты\n'
    text += '3. Email на YouTube, чтобы был доступ :)\n\n'
    text += f'Скрин и эмэйл отправь мне ({owner.mention}) в личные сообщения'

    return text

# title, description, color
def ege_25_text_1():
    title_msg = 'Видео-курс 25 Задание ЕГЭ Информатика'

    description_msg = 'Всё самое необходимое для решения 25ого номера в ЕГЭ.\n\n'
    description_msg += 'Что входит в курс:\n'
    description_msg += '• Нахождение делителей\n'
    description_msg += '• Оптимизация\n'
    description_msg += '• Разбор множества заданий(всё что только может попасться)\n'
    description_msg += '  + задания с последних лет из реальных ЕГЭ\n\n'
    description_msg += 'Общая длительность курса: ~2 часа.\n\n'
    description_msg += 'Источники задач:\n'
    description_msg += '1) Реальные задания с ЕГЭ\n'
    description_msg += '2) КПоляков\n'
    description_msg += '3) Мои тренировочные задания\n\n'
    description_msg += 'Самая основная теория + большое количество практических разборов и советов от меня.\n\n'
    description_msg += '💻Как это проходит:\n'
    description_msg += 'Это закрытый видеокурс, находящийся на YouTube.'
    color_msg = 0x5ACFF5

    return (title_msg, description_msg, color_msg)

def ege_25_text_2(owner):
    text = 'Чтобы получить доступ к Курсу нужно:\n'
    text += '1. Перевести на карту сбербанка 360р. с текстом сообщения: "Инфа25"\n'
    text += 'на карту: 4276 0800 1585 5878\n'
    text += '2. Сделать скрин успешного перевода или скрин на последние 4 цифры карты\n'
    text += '3. Email на YouTube, чтобы был доступ :)\n\n'
    text += f'Скрин и эмэйл отправь мне ({owner.mention}) в личные сообщения'

    return text

# title, description, color
def ege_26_text_1():
    title_msg = 'Видео-курс 26 Задание ЕГЭ Информатика'

    description_msg = 'Всё самое необходимое для решения 26ого номера в ЕГЭ.\n\n'
    description_msg += 'Что входит в курс:\n'
    description_msg += '• Объяснение логики заданий всех типов\n'
    description_msg += '• Решение кодом и через Excel (большинство кодом)\n'
    description_msg += '• Разбор множества заданий(всё что только может попасться)\n'
    description_msg += '  + задания с последних лет из реальных ЕГЭ\n\n'
    description_msg += 'Общая длительность курса: ~2 часа.\n\n'
    description_msg += 'Источники задач:\n'
    description_msg += '1) Реальные задания с ЕГЭ\n'
    description_msg += '2) КПоляков\n'
    description_msg += '3) Мои тренировочные задания\n\n'
    description_msg += 'Самая основная теория + большое количество практических разборов и советов от меня.\n\n'
    description_msg += '💻Как это проходит:\n'
    description_msg += 'Это закрытый видеокурс, находящийся на YouTube.'
    color_msg = 0x5ACFF5

    return (title_msg, description_msg, color_msg)


def ege_26_text_2(owner):
    text = 'Чтобы получить доступ к Курсу нужно:\n'
    text += '1. Перевести на карту сбербанка 572р. с текстом сообщения: "Инфа26"\n'
    text += 'на карту: 4276 0800 1585 5878\n'
    text += '2. Сделать скрин успешного перевода или скрин на последние 4 цифры карты\n'
    text += '3. Email на YouTube, чтобы был доступ :)\n\n'
    text += f'Скрин и эмэйл отправь мне ({owner.mention}) в личные сообщения'

    return text

# title, description, color
def ege_27_text_1():
    title_msg = 'Видео-курс 27 Задание ЕГЭ Информатика'

    description_msg = 'Всё самое необходимое по строкам для решения 27ого номера в ЕГЭ.\n\n'
    description_msg += 'Что входит в курс:\n'
    description_msg += '• Нахождение делителей\n'
    description_msg += '• Оптимизация\n'
    description_msg += '• Разбор множества заданий(всё что только может попасться)\n'
    description_msg += '  + задания с последних лет из реальных ЕГЭ\n\n'
    description_msg += 'Общая длительность курса: ~2 часа.\n\n'
    description_msg += 'Источники задач:\n'
    description_msg += '1) Реальные задания с ЕГЭ\n'
    description_msg += '2) КПоляков\n'
    description_msg += '3) Мои тренировочные задания\n\n'
    description_msg += 'Самая основная теория + большое количество практических разборов и советов от меня.\n\n'
    description_msg += '💻Как это проходит:\n'
    description_msg += 'Это закрытый видеокурс, находящийся на YouTube.'
    color_msg = 0x5ACFF5

    return (title_msg, description_msg, color_msg)


def ege_27_text_2(owner):
    text = 'Чтобы получить доступ к Курсу нужно:\n'
    text += '1. Перевести на карту сбербанка 750р. с текстом сообщения: "Инфа26"\n'
    text += 'на карту: 4276 0800 1585 5878\n'
    text += '2. Сделать скрин успешного перевода или скрин на последние 4 цифры карты\n'
    text += '3. Email на YouTube, чтобы был доступ :)\n\n'
    text += f'Скрин и эмэйл отправь мне ({owner.mention}) в личные сообщения'

    return text

# title, description, color
def krugosvetka_pro_text_1():
    title_msg = 'Мастер-группа Кругосветка PRO ЕГЭ Информатика'

    description_msg = 'Хочешь высокие баллы? Тогда это то, что тебе нужно!\n'
    discription_msg += '80+, 90+ или 100 баллов станут реальностью 😉\n\n'
    description_msg += 'Кругосветка — это отличная возможность подготовиться к ЕГЭ!\n'
    description_msg += 'Совместно с ребятами, которые как и ты заинтересованы в успешной \n'
    description_msg += 'подготовке к экзамену, в приятной и комфортной атмосфере время \n'
    description_msg += 'пролетит быстро и ты получишь огромнейший ап скилла и уверенность в себе!\n\n'
    description_msg += 'Что входит в курс:\n\n'
    description_msg += '• 2 занятия в неделю. Все занятия записываются и у тебя \n'
    description_msg += '  будет возможность пересмотреть их в любой момент.\n'
    description_msg += '  Длительность занятий ~90 минут.\n'
    description_msg += '• много практики. Много задач на занятии, много задач\n'
    description_msg += '  после занятия, которые идут тебе в дз.\n'
    description_msg += '• Регулярные пробники для наглядности твоего прогресса \n'
    description_msg += '  и обретении уверенности в своих силах.\n'
    description_msg += '• общий чат со мной и всеми ребятами. А это постоянная мотивация,\n'
    description_msg += '  обсуждение задач, помощь друг другу и немного фана позволит тебе\n'
    description_msg += '  всегда оставаться в тонусе.\n'
    description_msg += '• возможность личного общения со мной, чтобы справиться с волнениями,\n'
    description_msg += '  нервами, трудностями и всем остальным ;)\n'
    description_msg += '• бонусные занятия, созвоны для дополнительной практики и ответов на вопросы.\n'
    description_msg += '• индивидуальная помощь при выборе ВУЗа и направлений.\n\n'
    description_msg += '💻Как это проходит:\n'
    description_msg += 'Все занятия проходят на YouTube в виде закрытых стримов\n'
    description_msg += 'с использованием онлайн-доски (для хранения всех записей)\n\n'
    #description_msg += '' на 5 месяцев
    color_msg = 0x5ACFF5

    return (title_msg, description_msg, color_msg)


def krugosvetka_pro_text_2(owner):
    text = 'Чтобы получить доступ к Мастер-группе нужно:\n'
    text += '1. Перевести на карту сбербанка 2164р.  с текстом сообщения: "КругосветкаPRO"\n'
    text += 'номер карты: 4276 0800 1585 5878\n'
    text += '2. Сделать скрин успешного перевода или скрин на последние 4 цифры карты\n'
    text += '3. Email на YouTube, чтобы был доступ :)\n'
    text += '4. Скинь мне свой ник в Discord, чтобы я дал роль на сервере\n\n'
    text += f'Скрин и эмэйл отправь мне ({owner.mention}) в личные сообщения'

    return text


# title, description, color
def c_university_text_1():
    title_msg = 'Видео-курс Си для ВУЗа'

    description_msg = 'Хочешь шарить в ВУЗе?\n'
    discription_msg += '80+, 90+ или 100 баллов станут реальностью 😉\n\n'
    description_msg += 'Кругосветка — это отличная возможность подготовиться к ЕГЭ!\n'
    description_msg += 'Что входит в курс:\n\n'
    description_msg += '• 2 занятия в неделю. Все занятия записываются и у тебя \n'
    description_msg += '  будет возможность пересмотреть их в любой момент.\n'
    description_msg += '  Длительность занятий ~90 минут.\n'
    description_msg += '• много практики. Много задач на занятии, много задач\n'
    description_msg += '  после занятия, которые идут тебе в дз.\n'
    description_msg += '• Регулярные пробники для наглядности твоего прогресса \n'
    description_msg += '  и обретении уверенности в своих силах.\n'
    description_msg += '• общий чат со мной и всеми ребятами. А это постоянная мотивация,\n'
    description_msg += '  обсуждение задач, помощь друг другу и немного фана позволит тебе\n'
    description_msg += '  всегда оставаться в тонусе.\n'
    description_msg += '• возможность личного общения со мной, чтобы справиться с волнениями,\n'
    description_msg += '  нервами, трудностями и всем остальным ;)\n'
    description_msg += '• бонусные занятия, созвоны для дополнительной практики и ответов на вопросы.\n'
    description_msg += '• индивидуальная помощь при выборе ВУЗа и направлений.\n\n'
    description_msg += '💻Как это проходит:\n'
    description_msg += 'Все занятия проходят на YouTube в виде закрытых стримов\n'
    description_msg += 'с использованием онлайн-доски (для хранения всех записей)\n\n'
    #description_msg += '' на 5 месяцев
    color_msg = 0x5ACFF5

    return (title_msg, description_msg, color_msg)


def c_university_text_2(owner):
    text = 'Чтобы получить доступ к Мастер-группе нужно:\n'
    text += '1. Перевести на карту сбербанка 2164р.  с текстом сообщения: "КругосветкаPRO"\n'
    text += 'номер карты: 4276 0800 1585 5878\n'
    text += '2. Сделать скрин успешного перевода или скрин на последние 4 цифры карты\n'
    text += '3. Email на YouTube, чтобы был доступ :)\n'
    text += '4. Скинь мне свой ник в Discord, чтобы я дал роль на сервере\n\n'
    text += f'Скрин и эмэйл отправь мне ({owner.mention}) в личные сообщения'

    return text


def find_user(name, all_users):
    for user in all_users:
        if user.name.lower() == name.lower():
            return user

    return False