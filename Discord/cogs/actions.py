from Discord.functions.main_func import find_user, get_complexity, create_password, get_key_by_value
from disnake.ext import commands
import disnake
import Discord.session as session


class Actions(commands.Cog):
    '''Действия'''

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @commands.slash_command(name='дать_монет')
    async def transfer_money(self,
        inter: disnake.ApplicationCommandInteraction,
        игрок: str, монет: int):
        '''Дать монет другому игроку
        
        Щедрое это дело. 
        '''
        
        money = монет
        hero = inter.author.name
        hero = find_user(hero, session.all_users)
        player = find_user(игрок, session.all_users)

        if player:
            if inter.author.name != игрок and игрок != 'dina':
                if money > 0:
                    if hero.money >= money:
                        hero.money -= money
                        player.money += money

                        title = 'Передача монет'
                        descr = f'Игрок {inter.author.name} отдал '
                        descr += f'{money} монет игроку {игрок}'
                        embed = disnake.Embed(title=title, description=descr)
                        await inter.send(embed=embed)
                    else:
                        msg = 'У тебя нет столько монет :('
                        await inter.send(msg)
                else:
                    msg = 'Количество монет должно быть положительным числом'
                    await inter.send(msg)
            else:
                msg = 'Забирать у себя и отдавать себе — бессмысленно.'
                await inter.send(msg)
        else:
            msg = 'Выбери существующего человека.'
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