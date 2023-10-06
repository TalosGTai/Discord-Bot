from src.functions.discord import find_role_by_name


def roles_main() -> dict[str, int, dict]:
    '''Формирование ролей и сообщения Общего'''

    reactions = {'gtai': '<:GTai:1158357831058206801>',
                 'code': '<:plus1:1158356291866087478>',
                 'ege': '<:ege:849327226645250058>'}
    roles = {'<:GTai:1158357831058206801>': 'YouTube Уведомления',
             '<:plus1:1158356291866087478>': 'Programming Уведомления',
             '<:ege:849327226645250058>': 'ЕГЭшник'}

    description = f"Реакция  {reactions['gtai']}, чтобы не"
    description += 'пропустить новые видео на канале.\n'
    description += f"Реакция  {reactions['code']}, чтобы получать "
    description += 'уведомления о новых задачах и челленджах по программированию.\n'
    description += f"Реакция  {reactions['ege']}, чтобы получать "
    description += 'уведомления, связанные с ЕГЭ.\n'
    color = 0xff8c00

    return {'description': description, 'color': color, 'roles': roles}


def roles_it(bot) -> dict[str, int]:
    '''Формирование ролей и сообщения, связанного с IT'''

    reactions = {'python': '<:python:847868360985542656>',
                 'c#': '<:cs:847868360943337502>', 
                 'java': '<:java:847868360938487808>',
                 'c++': '<:cpp:847868361051209758>', 
                 'js': '<:js:848668818385010708>'}
    roles = {'<:python:847868360985542656>': 'Python',
             '<:cs:847868360943337502>': 'C#',
             '<:java:847868360938487808>': 'Java',
             '<:cpp:847868361051209758>': 'C++',
             '<:js:848668818385010708>': 'JavaScript'}
    python = find_role_by_name(bot, 'Python')
    cs = find_role_by_name(bot, 'C#')
    java = find_role_by_name(bot, 'Java')
    cpp = find_role_by_name(bot, 'C++')
    js = find_role_by_name(bot, 'JavaScript')
    title = 'Используй соответствующие реакции для получения ролей'
    description = f"{reactions['python']} для {python.mention} роли\n"
    description += f"{reactions['c#']}  для {cs.mention} роли\n"
    description += f"{reactions['java']}  для {java.mention} роли\n"
    description += f"{reactions['c++']}  для {cpp.mention} роли\n"
    description += f"{reactions['js']}  для {js.mention} роли\n"
    color = 0xff8c00
    
    return {'title': title, 'description': description, 'color': color, 'roles': roles}


def roles_games() -> dict[str, int]:
    '''Формирование ролей и сообщения, связанного с играми'''

    reactions = {'chess': '<:chesspawn:1158364628720550008>'}
    roles = {'<:chesspawn:1158364628720550008>': 'Chess'}
    description = f"Реакция  {reactions['chess']} чтобы получать "
    description += 'уведомления о турнирах по шахматам и всем с этим связанным.\n'
    color = 0xff8c00
    
    return {'description': description, 'color': color, 'roles': roles}


def add_key_to_dict(cur_dict: dict, new_dict: dict) -> dict:
    ''' Для функции get_all_roles. 
        cur_dict - общий словарь со всеми ключами (сюда добавляем). 
        new_dict - отсюда берём.
    '''
    
    for key in new_dict:
        cur_dict[key] = new_dict[key]

    return cur_dict


def get_all_roles(bot) -> dict:
    '''Все словари с ролями объединяем в 1 словарь'''

    d_main = roles_main()
    d_it = roles_it(bot)
    d_games = roles_games()
    roles = dict()

    roles = add_key_to_dict(roles, d_main['roles'])
    roles = add_key_to_dict(roles, d_it['roles'])
    roles = add_key_to_dict(roles, d_games['roles'])

    return roles


def get_all_msg_roles() -> list[int]:
    '''Список со всеми id-сообщениями, в которых
        можно менять роли.
    '''

    l_msg_id = [1158402595686199387,
                1158408970160050287,
                1158409058680852570]
    return l_msg_id