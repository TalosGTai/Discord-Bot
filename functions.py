from random import randint
import datetime as DT
from db_functions import get_question_from_db
import disnake


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
def calculate_money_win(wr1, wr2, money1: float, money2: float) -> float:
    money_win = min(wr1, wr2) * min(money1 / 100, money2 / 100)

    if wr1 < wr2:
        money_win *= 1.1

    return to_two_digits(money_win)


# +1 win and +1 game
def update_duel_stat(stat, game):
    all_games = int(stat[0]) + 1

    if game:
        win_games = int(stat[1]) + 1
    else:
        win_games = int(stat[1])

    res = str(all_games) + '-' + str(win_games)

    return res


# check < 0 and to view: xxx.xx
def update_money(user_money: float, money_win: float) -> float:
    # проверка на отрицательное количество монет
    if user_money - money_win < 0:
        money_win = user_money

    money_win = to_two_digits(money_win)

    return money_win


# convert number to two digits
def to_two_digits(num: float) -> float:
    return int(num * 100) / 100


# Количество дней от даты до текущего дня
def date_to_days(user_date: str) -> int:
    date = user_date.split('-')
    date = DT.date(int(date[0]), int(date[1]), int(date[2]))
    days = abs(int((date - DT.date.today()).days))

    return days


# окончания для даты (дня, дней)
def get_days(day: int) -> dict:
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
            # sentences = []'')
        case 'hero':
            pass


# delete \
def delete_reverse_slash(s: str) -> str:
    if s.find('\\') == -1:
        return s
    else:
        return s[:s.find('\\'):] + s[s.find('\\') + 1::]


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
    description_msg += '80+, 90+ или 100 баллов станут реальностью 😉\n\n'
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
    description_msg += '80+, 90+ или 100 баллов станут реальностью 😉\n\n'
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


def trainer_2_text():
    title_msg = 'Курс-тренажёр по 2ому заданию ЕГЭ Информатика'

    description_msg = 'Бесплатный курс по подготовке и тренировке 2ого задания из ЕГЭ.\n\n'
    description_msg += '• Научу с 0 делать этот номер;\n'
    description_msg += '• 50+ заданий для практики;\n'
    description_msg += '• Задания из реальных ЕГЭ прошлых лет;\n'
    description_msg += '• Видео-разборы заданий;\n'
    description_msg += '• Ответы на все возникающие вопросы;\n\n'
    description_msg += 'Для прохождения курса перейди по ссылке -> https://stepik.org/course/126074'
    color_msg = 0x5ACFF5

    return (title_msg, description_msg, color_msg)


def trainer_8_text():
    title_msg = 'Курс-тренажёр по 8ому заданию ЕГЭ Информатика'

    description_msg = 'Отличная возможность по подготовке и тренировке 8ого задания из ЕГЭ.\n\n'
    description_msg += '• Научу с 0 делать этот номер;\n'
    description_msg += '• 50+ заданий для практики;\n'
    description_msg += '• Задания из реальных ЕГЭ прошлых лет;\n'
    description_msg += '• Видео-разборы заданий;\n\n'
    description_msg += '• Ответы на все возникающие вопросы;\n\n'
    description_msg += 'Всего лишь за 350р. ты получишь всё это!\n'
    description_msg += 'Для приобретения курса перейди по ссылке -> https://stepik.org/a/131347'
    color_msg = 0x5ACFF5

    return (title_msg, description_msg, color_msg)


def trainer_15_text():
    title_msg = 'Курс-тренажёр по 15ому заданию ЕГЭ Информатика'

    description_msg = 'Отличная возможность по подготовке и тренировке 15ого задания из ЕГЭ.\n\n'
    description_msg += '• Научу с 0 делать этот номер;\n'
    description_msg += '• 50+ заданий для практики;\n'
    description_msg += '• Задания из реальных ЕГЭ прошлых лет;\n'
    description_msg += '• Видео-разборы заданий;\n\n'
    description_msg += '• Ответы на все возникающие вопросы;\n\n'
    description_msg += 'Всего лишь за 350р. ты получишь всё это!\n'
    description_msg += 'Для приобретения курса перейди по ссылке -> https://stepik.org/a/131347'
    color_msg = 0x5ACFF5

    return (title_msg, description_msg, color_msg)


def embed_task_msg(number_task: int, row: dict) -> list:
    title = f'Задача из {number_task}ого номера ЕГЭ по Информатике'
    description = f"Тип задания: {row['type']}\n"
    description += f"Сложность задания: {row['complexity']}\n"
    color= 0x53377A
    embeds = []

    if 'files' in row.keys():
        for i in range(len(row['files'])):
            description += row['condition'][i]
            embed_i = disnake.Embed(color=color, description=description)
            embed_i.set_image(file=row['files'][i])
            embeds.append(embed_i)
            description = ''
    else:
        description += 'Условие:\n'
        description += f"{row['condition']}"
        embed = disnake.Embed(
            title=title, description=description, color=color)
        embeds.append(embed)

    return embeds


def embed_days_to_ege(t_ege: tuple[tuple[int, str], tuple[int, str],
    tuple[int, str]]) -> tuple[str, str, int]:
    new_line = '\n'
    title = "Дней до экзаменов"
    description = f'до ЕГЭ по инфе {t_ege[0][0]}/{t_ege[0][0] + 1} {t_ege[0][1]}' + new_line
    description += f'до ЕГЭ по матеше {t_ege[1][0]} {t_ege[1][1]}' + new_line
    description += f'до ЕГЭ по русичу {t_ege[2][0]} {t_ege[2][1]}' + new_line
    description += f'до ЕГЭ по физике {t_ege[3][0]} {t_ege[3][1]}' + new_line
    description += f'до ЕГЭ по обществу {t_ege[4][0]} {t_ege[4][1]}' + new_line
    description += f'до ЕГЭ по истории {t_ege[5][0]} {t_ege[5][1]}'
    color = 0x00690a

    return (title, description, color)


def embed_question() -> tuple[str, int]:
    description = get_question_from_db()
    color = 0x003d03

    return (description, color)


def find_channel_by_name(bot, source_channel: str):
    for guild in bot.guilds:
        for channel in guild.channels:
            if channel.name == source_channel:
                return channel
    return False


def find_user(name, all_users):
    for user in all_users:
        if user.name.lower() == name.lower():
            return user

    return False