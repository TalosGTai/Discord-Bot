import datetime as DT
from ..db.db_functions import get_question_from_db
import disnake


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
def time_format(time: str) -> str:
    if len(time) == 1: return '0' + time
    return time


# delete \
def delete_reverse_slash(s: str) -> str:
    if s.find('\\') == -1:
        return s
    return s[:s.find('\\'):] + s[s.find('\\') + 1::]


def ege_24_text_1() -> tuple[str, str, int]:
    title_msg = 'Видео-курс 24 Задание ЕГЭ Информатика'

    description_msg = 'Хочешь понять строки и уметь решать все 24ые номера?\n'
    description_msg += 'Тогда это то, что тебе нужно!\n\n'
    description_msg += 'Что входит в курс:\n'
    description_msg += '• Основы строк\n'
    description_msg += '• Срезы\n'
    description_msg += '• Разбор множества заданий(всё что только может попасться)\n'
    description_msg += '• Курс постоянно обновляется и дополняется\n'
    description_msg += '  + задания с последних лет из реальных ЕГЭ\n\n'
    description_msg += 'Общая длительность курса: 2.5 часа.\n\n'
    description_msg += 'Источники задач:\n'
    description_msg += '1) Реальные задания с ЕГЭ\n'
    description_msg += '2) КПоляков\n'
    description_msg += '3) Мои тренировочные задания\n\n'
    description_msg += 'Самая основная теория + большое количество практических разборов и советов от меня.\n\n'
    description_msg += '💻Как это проходит:\n'
    description_msg += 'Это закрытый видеокурс, находящийся на YouTube.'
    color_msg = 0x5ACFF5

    return (title_msg, description_msg, color_msg)


def ege_24_text_2(owner) -> str:
    text = 'Чтобы получить доступ к Курсу нужно:\n'
    text += '1. Перевести на карту сбербанка 350р. с текстом сообщения: "Инфа24"\n'
    text += 'на карту: 4276 0800 1585 5878\n'
    text += '2. Сделать скрин успешного перевода или скрин на последние 4 цифры карты\n'
    text += '3. Email на YouTube, чтобы был доступ :)\n\n'
    text += f'Скрин и эмэйл отправь мне ({owner.mention}) в личные сообщения'

    return text


def ege_25_text_1() -> dict[str, str, int]:
    title_msg = 'Видео-курс 25 Задание ЕГЭ Информатика'

    description_msg = 'Всё самое необходимое для решения 25ого номера в ЕГЭ.\n\n'
    description_msg += 'Что входит в курс:\n'
    description_msg += '• Нахождение делителей\n'
    description_msg += '• Оптимизация\n'
    description_msg += '• Разбор множества заданий(всё что только может попасться)\n'
    description_msg += '• Курс постоянно обновляется и дополняется\n'
    description_msg += '  + задания с последних лет из реальных ЕГЭ\n\n'
    description_msg += 'Общая длительность курса: 2.5 часа.\n\n'
    description_msg += 'Источники задач:\n'
    description_msg += '1) Реальные задания с ЕГЭ\n'
    description_msg += '2) КПоляков\n'
    description_msg += '3) Мои тренировочные задания\n\n'
    description_msg += 'Самая основная теория + большое количество практических разборов и советов от меня.\n\n'
    description_msg += '💻Как это проходит:\n'
    description_msg += 'Это закрытый видеокурс, находящийся на YouTube.'
    color_msg = 0x5ACFF5

    return (title_msg, description_msg, color_msg)


def ege_25_text_2(owner) -> str:
    text = 'Чтобы получить доступ к Курсу нужно:\n'
    text += '1. Перевести на карту сбербанка 360р. с текстом сообщения: "Инфа25"\n'
    text += 'на карту: 4276 0800 1585 5878\n'
    text += '2. Сделать скрин успешного перевода или скрин на последние 4 цифры карты\n'
    text += '3. Email на YouTube, чтобы был доступ :)\n\n'
    text += f'Скрин и эмэйл отправь мне ({owner.mention}) в личные сообщения'

    return text


def ege_26_text_1() -> tuple[str, str, int]:
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


def ege_26_text_2(owner) -> str:
    text = 'Чтобы получить доступ к Курсу нужно:\n'
    text += '1. Перевести на карту сбербанка 572р. с текстом сообщения: "Инфа26"\n'
    text += 'на карту: 4276 0800 1585 5878\n'
    text += '2. Сделать скрин успешного перевода или скрин на последние 4 цифры карты\n'
    text += '3. Email на YouTube, чтобы был доступ :)\n\n'
    text += f'Скрин и эмэйл отправь мне ({owner.mention}) в личные сообщения'

    return text


def ege_27_text_1() -> tuple[str, str, int]:
    title_msg = 'Видео-курс 27 Задание ЕГЭ Информатика'

    description_msg = 'Всё самое необходимое по строкам для решения 27ого номера в ЕГЭ.\n\n'
    description_msg += 'Что входит в курс:\n'
    description_msg += '• Нахождение делителей\n'
    description_msg += '• Последовательности\n'
    description_msg += '• Динамическое программирование\n'
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


def ege_27_text_2(owner) -> str:
    text = 'Чтобы получить доступ к Курсу нужно:\n'
    text += '1. Перевести на карту сбербанка 750р. с текстом сообщения: "Инфа26"\n'
    text += 'на карту: 4276 0800 1585 5878\n'
    text += '2. Сделать скрин успешного перевода или скрин на последние 4 цифры карты\n'
    text += '3. Email на YouTube, чтобы был доступ :)\n\n'
    text += f'Скрин и эмэйл отправь мне ({owner.mention}) в личные сообщения'

    return text


def krugosvetka_pro_text_1() -> tuple[str, str, int]:
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


def krugosvetka_pro_text_2(owner) -> str:
    text = 'Чтобы получить доступ к Мастер-группе нужно:\n'
    text += '1. Перевести на карту сбербанка 2164р.  с текстом сообщения: "КругосветкаPRO"\n'
    text += 'номер карты: 4276 0800 1585 5878\n'
    text += '2. Сделать скрин успешного перевода или скрин на последние 4 цифры карты\n'
    text += '3. Email на YouTube, чтобы был доступ :)\n'
    text += '4. Скинь мне свой ник в Discord, чтобы я дал роль на сервере\n\n'
    text += f'Скрин и эмэйл отправь мне ({owner.mention}) в личные сообщения'

    return text


def c_university_text_1() -> tuple[str, str, int]:
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


def c_university_text_2(owner) -> str:
    text = 'Чтобы получить доступ к Мастер-группе нужно:\n'
    text += '1. Перевести на карту сбербанка 2164р.  с текстом сообщения: "КругосветкаPRO"\n'
    text += 'номер карты: 4276 0800 1585 5878\n'
    text += '2. Сделать скрин успешного перевода или скрин на последние 4 цифры карты\n'
    text += '3. Email на YouTube, чтобы был доступ :)\n'
    text += '4. Скинь мне свой ник в Discord, чтобы я дал роль на сервере\n\n'
    text += f'Скрин и эмэйл отправь мне ({owner.mention}) в личные сообщения'

    return text


def trainer_2_text() -> tuple[str, str, int]:
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


def trainer_7_text() -> tuple[str, str, int]:
    title_msg = 'Курс-тренажёр по 7ому заданию ЕГЭ Информатика'

    description_msg = 'Отличная возможность по подготовке и тренировке 8ого задания из ЕГЭ.\n\n'
    description_msg += '• Научу с 0 делать этот номер;\n'
    description_msg += '• Разбор всех типов задания;\n'
    description_msg += '• 50+ заданий для практики;\n'
    description_msg += '• Задания из реальных ЕГЭ прошлых лет;\n'
    description_msg += '• Видео-разборы заданий;\n\n'
    description_msg += '• Ответы на все возникающие вопросы;\n\n'
    description_msg += 'Всего лишь за 350р. ты получишь всё это!\n'
    description_msg += 'Для приобретения курса перейди по ссылке -> https://stepik.org/a/131347'
    color_msg = 0x5ACFF5

    return (title_msg, description_msg, color_msg)


def trainer_8_text() -> tuple[str, str, int]:
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


def trainer_15_text() -> tuple[str, str, int]:
    title_msg = 'Курс-тренажёр по 15ому заданию ЕГЭ Информатика'

    description_msg = 'Отличная возможность по подготовке и тренировке 15ого задания из ЕГЭ.\n\n'
    description_msg += '• Научу с 0 делать этот номер;\n'
    description_msg += '• 50+ заданий для практики;\n'
    description_msg += '• Задания из реальных ЕГЭ прошлых лет;\n'
    description_msg += '• Видео-разборы заданий;\n\n'
    description_msg += '• Ответы на все возникающие вопросы;\n\n'
    description_msg += 'Всего лишь за 350р. ты получишь всё это!\n'
    description_msg += 'Для приобретения курса перейди по ссылке -> https://stepik.org/149687'
    color_msg = 0x5ACFF5

    return (title_msg, description_msg, color_msg)


def embed_task_msg(number_task: int, row: dict) -> list:
    title = f'Задача из {number_task}ого номера ЕГЭ по Информатике'
    description = f"Тип задания: {row['type']}\n"
    description += f"Сложность задания: {row['complexity']}\n"
    color= 0x53377A
    embeds = []

    if 'img' in row.keys():
        for i in range(len(row['img'])):
            description += row['condition'][i]
            embed_i = disnake.Embed(color=color, description=description)
            embed_i.set_image(file=row['img'][i])
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


def load_phrases(action: str) -> str:
    match (action):
        case 'bot':
            f = open('../phrases/games/duel/fight_bot.txt')
        case 'self':
            f = open('../phrases/games/duel/fight_self.txt')
        case 'none':
            f = open('../phrases/games/duel/fight_none.txt')
        case 'money-self':
            f = open('../phrases/games/duel/money_self.txt')
        case 'money-enemy':
            f = open('../phrases/games/duel/money_enemy.txt')
    
    id_string: int = randint(0, count_strings_in_file(f) - 1)
    phrase: str = get_string_by_id(f, id_string)

    return phrase


def count_strings_in_file(file) -> int:
    count_strings: int = 0

    for s in file:
        count_strings += 1

    return count_strings
    

def get_string_by_id(file, id_string: int) -> str:
    cur_id: int = 0

    for s in file:
        if cur_id == id_string: return s
        cur_id += 1


def embed_reason(member:str) -> disnake.Embed:
    title = 'Сервер GTai'
    msg = f'Привет {member}' + '\n'
    msg += 'Ты от нас уходишь? Мне бы этого совсем не хотелось...' + '\n'
    msg += 'Если тебе не хватило неформального общения и ежедвных задач, то' + '\n'
    msg += 'они есть в нашем телеграм-канале https://t.me/gtai_ege' + '\n'
    msg += 'Кстати, задачки и здесь можно решать ежедневные.' + '\n'
    msg += 'Для этого нужно написать /задачи_егэ_инф и выбрать нужную' + '\m\n'
    msg += 'Если всё же у меня не получилось тебя уговорить остаться, то напиши причину, пожалуйста.'
    color = 0x003d03
    embed = disnake.Embed(title=title, description=msg, color=color)

    return embed


def embed_wrong_channel(channel, type: str) -> disnake.Embed:
    match (type):
        case 'question':
            description = f'Вопросы от меня ты можешь получить на канале {channel.mention}'
        case 'ege':
            description = f'Задачи от меня ты можешь получить на канале {channel.mention}' + '\n'
            description += 'просто напиши там эту же комманду ;)'
        case 'duel':
            description = f'Сразиться в дуэли ты можешь на канале {channel.mention}'
        case 'lucky_number':
            description = f'Сыграть в эту игру ты можешь на канале {channel.mention}'

    color = 0x5c2e01
    embed = disnake.Embed(description=description, color=color)

    return embed


def embeds_welcome(bot, member: disnake.Member) -> list[disnake.Embed]:
    title = 'Добро пожаловать на сервер'
    descr = f'{member.mention}, очень рада приветствовать тебя на нашем сервере!' + '\n'
    descr += 'Здесь ты сможешь полезно и кайфово провести время.' + '\n'
    descr += 'Новые знакомства и знания ждут тебя впереди!' + '\n'
    descr += 'Наслаждайся :smiling_imp: '
    color = 0x33081d
    
    embed = disnake.Embed(title=title, description=descr, color=color)

    return [embed, embed_welcome_ege(bot, member), embed_welcome_it(bot, member)]


def embed_welcome_ege(bot, member: disnake.Member) -> disnake.Embed:
    channel_inf_tasks = find_channel_by_name(bot, 'инфа-задачи')
    channel_inf_courses = find_channel_by_name(bot, 'о-курсах-егэ')
    channel_inf_links = find_channel_by_name(bot, 'полезные-ссылки-егэ')

    title = 'ЕГЭ по информатике'
    descr = 'Самые интересные и топовые каналы по этой теме:' + '\n\n'
    descr += f'{channel_inf_tasks.mention} — если возникают трудности при решении каких-то задач, то '
    descr += 'присылай свои задачи и мы поможем или же помоги другим ;)' + '\n\n'
    descr += f'{channel_inf_courses.mention} - очень крутые и полезные курсы от ВСЕОТЦА '
    descr += 'помогут тебе увеличить свой балл на экзамене и обрести уверенность' + '\n\n'
    descr += f'{channel_inf_links.mention} - здесь все самые необходимые ссылки для подготовки к ЕГЭ по информатике'
    color = 0x103303

    embed = disnake.Embed(title=title, description=descr, color=color)

    return embed


def embed_welcome_it(bot, member: disnake.Member) -> disnake.Embed:
    channel_it_tasks = find_channel_by_name(bot, 'общий')
    channel_it_courses = find_channel_by_name(bot, 'о-курсах-it')
    channel_it_links = find_channel_by_name(bot, 'полезные-ссылки-it')

    title = 'Программирование | IT'
    descr = 'Интересен мир IT? Ознакомься с этими каналами:' + '\n\n'
    descr += f'{channel_it_tasks.mention} — здесь можешь обсудить все интересующие тебя вопросы из мира IT' + '\n\n'
    descr += f'{channel_it_courses.mention} - очень крутые и полезные курсы от ВСЕОТЦА '
    descr += 'их мало, но там так всё чётко разложено, будто ты всегда это знал, стоящая вещь!' + '\n\n'
    descr += f'{channel_it_links.mention} - множества полезнейших ресурсов для кодинга, разработки, '
    descr += 'дизайна и анализа разного уровня сложности.'
    color = 0x330319

    embed = disnake.Embed(title=title, description=descr, color=color)

    return embed


def embed_by_phrase(phrase: str) -> disnake.Embed:
    embed = disnake.Embed(description=phrase)

    return embed


def write_to_file(file_name: str, msg: str):
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


def find_channel_by_name(bot, source_channel: str):
    for guild in bot.guilds:
        for channel in guild.channels:
            if channel.name == source_channel:
                return channel
    return False


def find_user(name: str, all_users):
    for user in all_users:
        if user.name.lower() == name.lower():
            return user
    return False