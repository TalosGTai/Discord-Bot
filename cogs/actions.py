from disnake.ext import commands
import disnake, session
from functions import find_user


class Actions(commands.Cog):
    '''Действия'''

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @commands.slash_command(name='дать_монет')
    async def transfer_money(self,
        inter: disnake.ApplicationCommandInteraction,
        игрок: str, монет: int):
        '''Дать монет другому игроку'''
        
        money = монет
        hero = inter.author.name
        hero = find_user(hero, session.all_users)
        player = find_user(игрок, session.all_users)

        if player:
            if inter.author.name != игрок:
                if hero.money >= money:
                    hero.money -= money
                    player.money += money
                    title = 'Передача монет'
                    descr = f'Игрок {inter.author.name} отдал '
                    descr += f'{money} монет игроку {игрок}'
                    embed = disnake.Embed(title=title, description=descr)
                    await inter.send(embed=embed)
                else:
                    msg = 'У тебя нет столько монет'
                    await inter.send(msg)
            else:
                msg = 'Забирать у себя и отдавать себе — бессмысленно.'
                await inter.send(msg)
        else:
            msg = 'Выбери существующего человека'
            await inter.send(msg)


    #@commands.slash_command(name='сгенерировать_пароль')
    async def generate_password(self,
        inter: disnake.ApplicationCommandInteraction,
        длина: int, сложность: str):
        ''''''
        pass


def setup(bot: commands.Bot):
    bot.add_cog(Actions(bot))
