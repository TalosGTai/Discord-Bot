import disnake
from src.functions.discord import find_channel_by_name
from src.data.data_base import DB
from src.functions.describe import lucky_number_describe


def embed_reason(member: str) -> disnake.Embed:
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
    '''Создание embed для выбора подходящего канала.
    Когда пользователь выбрал не тот канал.'''

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


def embed_stats_duel(user_name: str, value: dict[str, int]) -> disnake.Embed:
    all_games, win_games = value['all_games'], value['win_games']
    wr = value['wr']
    
    title = f'Статы {user_name} в игре Дуэль'
    descr = f'Всего игр: {all_games}\n'
    descr += f'Побед: {win_games}\n'
    descr += f'Процент побед: {wr}'
    color = 0x187CFC

    embed = disnake.Embed(title=title, description=descr, color=color)

    return embed


def embed_user_info(user_name: str, value: dict[str, int]) -> disnake.Embed:
    title = f''
    descr = f''
    
    color = 0x187CFC

    embed = disnake.Embed(title=title, description=descr, color=color)

    return embed


def embed_task_msg(number_task: int, row: dict) -> list:
    '''Создание embed для таска'''

    title = f'Задача из {number_task}ого номера ЕГЭ по Информатике'
    description = f"Тип: {row['theme']}\n"
    description += f"Сложность: {row['complexity']}\n"
    description += f"Автор: {row['author']}\n"
    color = 0x53377A
    embeds = []

    if 'img' in row.keys():
        if len(row['img']) > 1:
            for i in range(len(row['img'])):
                description += row['condition'][i]
                embed_i = disnake.Embed(color=color, description=description)
                embed_i.set_image(file=row['img'][i])
                embeds.append(embed_i)
                description = ''
        else:
            description += 'Условие:\n'
            description += f"{row['condition'][1]}"
            embed = disnake.Embed(
                title=title, description=description, color=color)
            embed.set_image(file=row['img'][0])
            embeds.append(embed)
    else:
        description += 'Условие:\n'
        description += f"{row['condition']}"
        embed = disnake.Embed(
            title=title, description=description, color=color)
        embeds.append(embed)

    return embeds


def embed_days_to_ege(t_ege: tuple[tuple[int, str], tuple[int, str],
                                   tuple[int, str]]) -> tuple[str, str, int]:
    '''Создание embed для отображения дней до ЕГЭ'''

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
    db = DB()
    description = db.get_question_from_db()
    color = 0x003d03

    return (description, color)


def embed_rules_lucky_game(timeout: int) -> disnake.Embed:
    d_rules = lucky_number_describe(timeout)
    color = 0x187CFC

    embed = disnake.Embed(title=d_rules['title'],
                          description=d_rules['description'], color=color)

    return embed


def embed_moderator_panel(d_embed: dict[str, str]) -> disnake.Embed:
    color = 0x38016b
    embed = disnake.Embed(
        title=d_embed['title'], description=d_embed['description'],
        color=color)

    return embed


def embed_games_panel(d_embed: dict[str, str]) -> disnake.Embed:
    color = 0x0073ff
    embed = disnake.Embed(
        title=d_embed['title'], description=d_embed['description'],
        color=color)

    return embed


def embed_user_panel(d_embed: dict[str, str]) -> disnake.Embed:
    color = 0x0e5c00
    embed = disnake.Embed(
        title=d_embed['title'], description=d_embed['description'],
        color=color)

    return embed
