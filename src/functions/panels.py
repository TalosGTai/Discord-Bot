def moderator_functions() -> dict[str, str, int]:
    # kick, ban, unban, mute, unmute, warn
    title = 'Панель модератора'
    descr = 'В данной панели описаны все твои возможности:\n\n'
    descr += '.warn user "reason" — данная команда даёт предупреждение '
    descr += 'участнику по указанной причине.\n'
    descr += 'Например: .warn Test "оскорбительное поведение"\n\n'
    descr += '.mute user time "reason" — данная команда даёт мут в чате'
    descr += 'участнику по указанной причине, время указывается в минутах.\n'
    descr += 'Например: .mute Test 30 "не реагировал на предупреждения".\n\n'
    descr += '.unmute user — данная команда снимает мут с участника.\n'
    descr += 'Например: .unmute Test\n\n'
    descr += '.kick user "reason" — данная команда кикает с сервера'
    descr += 'участника по указанной причине.\n'
    descr += 'Например: .kick Test "после предупреждний и мутов нужно было его унять".\n\n'
    descr += '.ban user "reason" — данная команда банит навсегда на сервере'
    descr += 'участника по указанной причине.\n'
    descr += 'Например: .ban Test "полностью неадекватный человек".\n\n'
    descr += '.unban user "reason" — данная команда разбаиит на сервере'
    descr += 'участника.\n'
    descr += 'Например: .unban Test.'
    descr += '\n\n'
    descr += 'Все команды старайся использовать вдумчиво.\n'
    descr += 'Несколько наставлений по этому поводу:\n'
    descr += '1. Warn — предупреждение давай после, хотя бы, 1ого'
    descr += 'словесногл замечания и пояснения его.\n'
    descr += '2. Mute — после нескольких warn и словесных замечаний.'
    descr += 'Используй ответственно.\n'
    descr += '3. Kick — если не помогли муты и варны, то остаётся кикнуть.'
    descr += 'Старайся не спешить с этим действием - это одна из крайних мер.\n'
    descr += '4. Ban — если даже после кика человек не начал себя вести как нужно.'
    descr += 'Обязательно посоветуйся с другим модератором или со мной перед баном.\n'
    descr += 'Большая сила — это большая ответственность.'
    color = 0x38016b
    
    return {'title': title, 'description': descr, 'color': color}


def tutor_functions() -> str:
    title = 'Панель репетитора'
    descr = ''
    color = 0

    return {'title': title, 'description': descr, 'color': color}


def user_functions() -> str:
    title = 'Панель пользователя'
    descr = ''
    color = 0

    return {'title': title, 'description': descr, 'color': color}