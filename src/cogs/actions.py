from src.functions.discord import find_user, \
    get_user_money, add_user_money, find_user_by_name_discord
from src.functions.main_func import get_complexity, create_password,\
    get_key_by_value, load_phrases
from disnake.ext import commands
import disnake


class Actions(commands.Cog):
    '''Действия'''

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @commands.slash_command(name='дать_монет')
    async def transfer_money(self,
        inter: disnake.ApplicationCommandInteraction,
        игрок: str = 'GTai', монет: int = 100, сообщение: str = ''):
        '''Дать монет другому игроку
        
        Щедрое это дело. 
        '''
        
        
        money = монет
        hero = inter.author.name
        hero_money = get_user_money(hero)

        if hero_money is not None:
            if find_user(игрок) or (игрок[0] == '@' and find_user(игрок[1::])):
                if inter.author.name != игрок:
                    if игрок not in ['dina', 'Dina']:
                        if money > 0:
                            if hero_money >= money:
                                add_user_money(hero, -money)
                                add_user_money(игрок, money)
                                user = find_user_by_name_discord(self.bot, игрок)
                                
                                title = 'Передача монет\n'
                                descr = f'Игрок {inter.author.name} отдал '
                                descr += f'{money} монет игроку {user.mention}.\n'
                                if len(сообщение) > 0:
                                    descr += f'Сообщение: {сообщение}'
                                msg = title + descr
                                #embed = disnake.Embed(title=title, description=descr)
                                #await inter.send(embed=embed)
                                await inter.send(msg)
                            else:
                                msg = load_phrases('social', 'transfer_money')
                                await inter.send(msg)
                        else:
                            msg = 'Количество монет должно быть положительным числом.'
                            await inter.send(msg)
                    else:
                        msg = 'Спасибо, конечно, но мне монеты не нужны.'
                        await inter.send(msg)
                else:
                    msg = load_phrases('social', action='transfer_money_self')
                    await inter.send(msg)
            else:
                msg = 'Выбери существующего человека.'
                await inter.send(msg)
        else:
            msg = load_phrases()
            await inter.send(msg)


    @commands.slash_command(name='сгенерировать_пароль')
    async def generate_password(self,
        inter: disnake.ApplicationCommandInteraction,
        сложность: str = 'средняя', длина: int = 8):
        '''Сгенерировать пароль
        
        сложность: лёгкая, средняя, сложная
        длина: [1, 16]
        '''
        
        complexity_dict = get_complexity()
        complexity_pass = get_key_by_value(сложность, complexity_dict)
        if complexity_pass:
            if 0 < длина <= 16:
                password = create_password(complexity_pass, длина)
                msg = f'Твой сгенерированный пароль: {password}'
                await inter.send(msg)
            else:
                msg = 'Длина пароля должна быть от 1 до 16 символов (включительно).'
                await inter.send(msg)
        else:
            msg = 'Выбери одну из сложностей: лёгкая, средняя, сложная.'
            await inter.send(msg)


def setup(bot: commands.Bot):
    bot.add_cog(Actions(bot))