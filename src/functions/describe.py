from src.functions.discord import find_channel_by_name
from src.modules.config import roles_cost, primary_items


def ask_for_help() -> dict[str, str]:
    '''Сообщение о том как просить о помощь'''

    title = 'Просить о помощи'
    description = 'Когда просишь о помощи, пожалуйста, придерживайся '
    description += 'следующего:\n'
    description += '- Какой результат ты ожидаешь увидеть;\n'
    description += '- Какие ошибки ты получил;\n'
    description += '- Если есть решение, то приложи его;'
    description += '\n\n'
    description += 'Также старайся придерживаться следующего:\n'
    description += '- Никто не ответил на твой вопрос? Возможно, в '
    description += 'вопросе недостаточно информации, плохая формулировка '
    description += 'или слишком узконаправленный вопрос, чтобы кто-то помог.\n'
    description += '- Задавай вопросы сразу. Не спрашивай, чтобы спросить.\n'
    description += '- Запомни, люди, которые тебе помогают - волонтёры, '
    description += 'которые тратят своё свободное время, чтобы помочь тебе '
    description += 'разобраться с твоим вопросом. Пожалуйста, '
    description += 'будь вежлив при общении и терпелив при ожидании ответа.'
    color = 0xff8c00

    return {'title': title, 'description': description, 'color': color}

def help_channels(bot) -> dict[str, str]:
    '''Сообщение о том на каких канала писать'''

    ege = find_channel_by_name(bot, 'помощь-с-егэ')
    code = find_channel_by_name(bot, 'помощь-с-кодом')
    code_forum = find_channel_by_name(bot, 'помощь-с-кодом-форум')
    
    title = 'Каналы для помощи'
    description = 'Задавай вопросы только на соответствующих каналах.'
    description += ' Это повысит шанс того, что тебе помогут ;)'
    description += '\n\n'
    description += f'{ege.mention} для помощь по ЕГЭ\n'
    description += f'{code.mention} для помощь по коду'
    description += '\n\n'
    description += f'Если тебе не ответили на вопрос из-за большой текучки в чате'
    description += f', большого объёма вопроса или на данный момент никто '
    description += f'не может помочь, то задай вопрос на форуме {code_forum.mention}.'
    color = 0xff8c00

    return {'title': title, 'description': description, 'color': color}

def share_code() -> dict[str, str]:
    '''Сообщение о том как постить код'''

    title = 'Как делиться кодом'
    description = 'Когда делишься кодом, то используй блоки кода, чтобы '
    description += 'поделиться небольшим фрагментом кода, который вызывает'
    description += ' проблему.\n\n'
    description += "\`\`\`python\n"
    description += 'код сюда\n'
    description += "\`\`\`"
    description += '\n\n'
    description += 'Замечу, что это символ, расположенный на букве ё, '
    description += 'это не апострофы.\n'
    description += 'Слово python может бьть заменено на любое другое, '
    description += 'соответствующее языку программирования.'
    description += '\n\n'
    description += 'Также ты можешь воспользоваться сторонним сервисом, например, '
    description += 'https://pastebin.com'
    description += '\n'
    description += 'Если в твоём проекте несколько файлов, то залей их на GitHub '
    description += 'и используй ссылку своего проекта.'
    color = 0xff8c00

    return {'title': title, 'description': description, 'color': color}

def moderator_panel() -> dict[str, str]:
    '''Панель с общими действиями модератора'''

    title = 'Панель модератора'
    descr = 'Ниже указаны все действия, необходимые для '
    descr += 'администрирования.'

    return {'title': title, 'description': descr}

def warn_describe() -> dict[str, str]:
    '''Описание команды Предупреждение'''
    
    title = 'Информация о команде Предупреждение'
    descr = 'Используй команду вдумчиво!\n'
    descr = 'Warn — предупреждение давай после, хотя бы, 1ого '
    descr += 'словесного замечания. Для быстрого использования команды '
    descr += 'можешь воспользоваться следующими действиями:\n\n'
    descr += '.warn user \"reason\" — данная команда даёт предупреждение '
    descr += 'участнику по указанной причине.\n'
    descr += 'Например: .warn Test \"оскорбительное поведение\"'

    return {'title': title, 'description': descr}

def mute_describe() -> dict[str, str]:
    '''Описание команды Мут'''

    title = 'Информация об использовании команды Мут'
    descr = 'Используй команду вдумчиво!\n'
    descr += 'Mute — после нескольких warn и словесных замечаний. '
    descr += 'Для быстрого использования команды можешь '
    descr += 'воспользоваться следующими действиями:\n\n'
    descr += '.mute user time \"reason\" — данная команда даёт мут в чате'
    descr += 'участнику по указанной причине, время указывается в минутах.\n'
    descr += 'Например: .mute Test 30 \"не реагировал на предупреждения\".\n\n'

    return {'title': title, 'description': descr}

def unmute_describe() -> dict[str, str]:
    '''Описание команды Размут'''

    title = 'Информация об использовании команды Размут'
    descr = 'Используй команду вдумчиво!\n'
    descr += 'Для быстрого использования команды можешь '
    descr += 'воспользоваться следующими действиями:\n\n'
    descr += '.unmute user — данная команда снимает мут с участника.\n'
    descr += 'Например: .unmute Test\n\n'

    return {'title': title, 'description': descr}

def kick_describe() -> dict[str, str]:
    '''Описание команды Кик'''

    title = 'Информация об использовании команды Кик'
    descr = 'Используй команду вдумчиво!\n'
    descr += 'Kick — если не помогли муты и варны, то остаётся кикнуть. '
    descr += 'Старайся не спешить с этим действием - это одна из крайних мер.\n'
    descr += 'Для быстрого использования команды можешь '
    descr += 'воспользоваться следующими действиями:\n\n'
    descr += '.kick user \"reason\" — данная команда кикает с сервера'
    descr += 'участника по указанной причине.\n'
    descr += 'Например: .kick Test \"после предупреждний и '
    descr += 'мутов нужно было его унять\".\n\n'

    return {'title': title, 'description': descr}

def ban_describe() -> dict[str, str]:
    '''Описание команды Бан'''

    title = 'Информация об использовании команды Бан'
    descr = 'Используй команду вдумчиво!\n'
    descr += 'Ban — если даже после кика человек не начал себя вести как нужно. '
    descr += 'Обязательно посоветуйся с другим модератором или со мной перед баном.\n'
    descr += 'Для быстрого использования команды можешь '
    descr += 'воспользоваться следующими действиями:\n\n'
    descr += '.ban user \"reason\" — данная команда банит навсегда на сервере'
    descr += 'участника по указанной причине.\n'
    descr += 'Например: .ban Test \"полностью неадекватный человек\".\n\n'

    return {'title': title, 'description': descr}

def unban_describe() -> dict[str, str]:
    '''Описание команды Разбан'''

    title = 'Информация об использовании команды Разбан'
    descr = 'Используй команду вдумчиво!\n'
    descr += 'Для быстрого использования команды можешь '
    descr += 'воспользоваться следующими действиями:\n\n'
    descr += '.unban user \"reason\" — данная команда разбанит на сервере '
    descr += 'участника.\n'
    descr += 'Например: .unban Test \"исправился и собирается '
    descr += 'искупить вину\"'

    return {'title': title, 'description': descr}

def games_panel() -> dict[str, str]:
    '''Описание игр с ботом'''

    title = 'Информация о всех играх с ботом'
    descr = 'Играя с ботом и другими участниками '
    descr += 'ты сможешь заработать уважение, получить эмоции '
    descr += 'и монеты, которые впоследствии сможешь потратить в магазине.'
    
    return {'title': title, 'description': descr}

def lucky_number_describe(timeout: int) -> dict[str, str]:
    '''Описание игры угадай число'''

    title = 'Игра Угадай число'
    descr = 'Правила игры очень просты:\n'
    descr += '    • загадано целое число от 1 до 100 (включительно)\n'
    descr += '    • у тебя 6 попыток\n'
    descr += f'   • на каждый ответ у тебя даётся {timeout} секунд\n'
    descr += '    • при каждой попытке ты будешь знать больше/меньше'
    descr += 'исходного числа ты находишься\n'
    descr += 'В строке должно находится только число (без посторонних символов).\n'
    descr += 'Для использования команды сделай следующее действие:\n'
    descr += '/угадай_число'

    return {'title': title, 'description': descr}

def duel_describe() -> dict[str, str]:
    '''Описание игры Дуэль'''

    title = 'Игра Дуэль'
    descr = 'Правила игры очень просты:\n'
    descr += 'Выбираешь противника с которым хочешь потягаться силой '
    descr += 'и нападаешь на него.\n'
    descr += 'На исход дуэли влияют следущие характеристики:\n'
    descr += '• уровень\n'
    descr += '• урон\n'
    descr += '• здоровье\n'
    descr += '• предметы\n'
    descr += '• и твои статы: сила, ловкость, интеллект'
    descr += '\n\n'
    descr += 'Для использования команды сделай следующее действие:\n'
    descr += '/дуэль имя_игрока'

    return {'title': title, 'description': descr}

def generate_password_describe() -> dict[str, str]:
    '''Сгенерировать пароль'''

    title = 'Генерация пароля'
    descr = 'Ты можешь сгенерировать пароль со следующими параметрами:\n'
    descr += '• длина от 1 до 16 (включительно)\n'
    descr += '• сложность: лёгкая, средняя, сложная\n'
    descr += 'Для использования команды сделай следующее действие:\n'
    descr += '/сгенерировать_пароль'

    return {'title': title, 'description': descr}

def transfer_money_describe() -> dict[str, str]:
    '''Передача монет другому игроку'''

    title = 'Передача монет другому игроку'
    descr = 'Щедрое это дело — делиться монетами:\n'
    descr += 'Для использования команды сделай следующее действие:\n'
    descr += '/дать\_монет монеты \"сообщение\"\n'
    descr += 'Пример команды:\n'
    descr += '/дать\_монет gtai 100 \"Всеотцу на поклонение\"'

    return {'title': title, 'description': descr}

def user_panel() -> dict[str, str]:
    '''Описание комманд пользователя'''

    title = 'Информация о всех коммандах с ботом'
    descr = 'Тут будет информация о тебе'
    
    return {'title': title, 'description': descr}

def shop_panel() -> dict[str, str]:
    '''Описание действий в магазине'''

    title = 'Магазин'
    descr = 'Выбери категорию, которая тебя интересует.'
    
    return {'title': title, 'description': descr}

def roles() -> dict[str, str]:
    '''Покупка ролей в магазине'''

    title = 'Роли'
    descr = 'Ты можешь выбрать любое название, цвет и картинку!\n'
    descr += 'Трать монеты с удовольствием ;)'

    return {'title': title, 'description': descr}

def role_color_with_icon() -> dict[str, str]:
    '''Покупка цветной роли со значком в магазине'''

    cost = roles_cost['role_color_with_icon']
    title = 'Цветная роль с картинкой'
    descr = 'Ты будешь выделяться среди всех, красивым цветом роли '
    descr += 'которая будет отображаться у тебя в профиле и потрясающим значком.\n'
    descr += 'Значок всегда будет отображаться в твоих сообщениях - это очень статусно.\n'
    descr += 'Это не выделенная роль - означает, что она не будет отображаться '
    descr += 'справа отдельно от всех. Но будет классно смотреться при просмотре '
    descr += '+ будет возможность её тегнуть (обращаться через знак @).'
    descr += '\n\n'
    descr += f'Стоимость роли: {cost} монет.\n'
    descr += f'Роль приобретается в виде подписки ежемесячной (цена за месяц).'

    return {'title': title, 'description': descr}

def role_color_with_icon_sep() -> dict[str, str]:
    '''Покупка выделенной цветной роли со значком в магазине'''

    cost = roles_cost['role_color_with_icon_sep']
    title = 'Цветная роль с картинкой'
    descr = 'Ты будешь выделяться среди всех, висеть будешь в топе ролей '
    descr += 'с красивым цветом и зачётной картинкой. Каждый будет видеть '
    descr += 'твою отличающуюся картинку и кайфовый по цвету ник - '
    descr += 'это зачётное зрелище. \n'
    descr += 'Данная роль является выделеной — отображается отдельно от всех (справа).'
    descr += '\n\n'
    descr += f'Стоимость выделенной роли: {cost} монет.\n'
    descr += f'Роль приобретается в виде подписки ежемесячной (цена за месяц).'

    return {'title': title, 'description': descr}

def role_color_without_icon() -> dict[str, str]:
    '''Покупка цветной роли без значка в магазине'''

    cost = roles_cost['role_color_without_icon']
    title = 'Цветная роль'
    descr = 'Ты будешь выделяться среди всех, красивым цветом роли. '
    descr += 'Приятный цвет никого не оставит равнодушным. \n'
    descr += 'Это не выделенная роль - означает, что она не будет отображаться '
    descr += 'справа отдельно от всех. Но будет классно смотреться при просмотре '
    descr += '+ будет возможность её тегнуть (обращаться через знак @).'
    descr += '\n\n'
    descr += f'Стоимость роли: {cost} монет.\n'
    descr += f'Роль приобретается в виде подписки ежемесячной (цена за месяц).'

    return {'title': title, 'description': descr}

def role_color_without_icon_sep() -> dict[str, str]:
    '''Покупка выделенной цветной роли без значка в магазине'''

    cost = roles_cost['role_color_without_icon_sep']
    title = 'Цветная роль'
    descr = 'Ты будешь выделяться среди всех, красивым цветом и '
    descr += 'названием роли. Каждый будет видеть твой кайфовый ник с ролью.'
    descr += 'Приятный цвет никого не оставит равнодушным. \n'
    descr += 'Данная роль является выделеной — отображается отдельно от всех (справа).'
    descr += '\n\n'
    descr += f'Стоимость выделенной роли: {cost} монет.\n'
    descr += f'Роль приобретается в виде подписки ежемесячной (цена за месяц).'

    return {'title': title, 'description': descr}

def role_color_without() -> dict[str, str]:
    '''Покупка роли с цветом и картинкой в магазине'''

    cost = roles_cost['role_without_color']
    title = 'Кастомная роль'
    descr = 'Ты всегда сможешь выделиться среди всех, висеть будешь в топе ролей. '
    descr += 'Приятный цвет никого не оставит равнодушным.'
    descr += '\n\n'
    descr += f'Стоимость данной роли: {cost} монет.\n'
    descr += f'Роль приобретается в виде подписки ежемесячной (цена за месяц).'

    return {'title': title, 'description': descr}

def events() -> dict[str, str]:
    '''Покупка событий в магазине'''

    title = 'События'
    descr = 'Ты можешь выбрать любое заинтересовавшее тебя действие!\n'
    descr += 'Трать монеты с удовольствием ;)'

    return {'title': title, 'description': descr}

def items() -> dict[str, str]:
    '''Покупка предметов в магазине'''

    title = 'Предметы'
    descr = 'Подберём предмет тебе по вкусу!\n'
    descr += 'Трать монеты с удовольствием ;)'

    return {'title': title, 'description': descr}

def all_goods() -> dict[str, str]:
    '''Покупка всех товаров в магазине'''

    title = 'Все товары'
    descr = 'Выбирай из всех товаров!\n'
    descr += 'Трать монеты с удовольствием ;)'
    

    return {'title': title, 'description': descr}

def user_got_item(user: object, item_name: str) -> str | bool:
    '''Сообщение для модераторов о том, что пользователь
    приобрёл товар, если этот товар:
    роль, событие или разное'''

    # check for moderator's action
    actions = ['role', 'event', 'other']
    if any(action for action in actions if action in item):
        msg = f'{user.mention} купил {item_name}.\n'
        msg += 'Требуется действие.'
        return msg
    return False

def user_congratulation(item_name: str) -> dict[str, str]:
    '''Поздравительное сообщению пользователю о приобретении
        товара.'''

    if is_primary_item(item_name):
        return msg_congratulation_primary(item_name)
    return msg_congratulation_standart(item_name)

def msg_congratulation_standart(item_name: str) -> dict[str, str]:
    title = 'Поздравляю с приобретением предмета!'
    descr = f'Поздравляю тебя с покупкой {item_name}!\n'
    descr += f'Только у нас товары по самым выгодным ценам!'

    return {'title': title, 'description': descr}

def msg_congratulation_primary(item_name: str) -> dict[str, str]:
    title = 'Поздравляю с приобретением товара!'
    descr = f'Поздравляю тебя с покупкой {item_name}!\n'
    descr += f'Спасибо тебе за поддержку меня, канала, моей деятельности и сервера!'

    return {'title': title, 'description': descr}

def is_primary_item(item_name: str) -> bool:
    for item in primary_items:
        if item in item_name:
            return True
    return False

def convert_item_promt_to_msg(item_name: str) -> str:
    '''Преобразование промт строки в название для 
    пользователя'''

    match(item_name):
        case 'role_color_with_icon_sep':
            return 'Выделенная цветная роль со значком'
        case 'role_color_without_icon_sep':
            return 'Выделенная цветная роль'
        case 'role_color_with_icon':
            return 'Цветная роль со значком'
        case 'role_color_without_icon':
            return 'Цветная роль'
        case 'role_color_without':
            return 'Роль'
