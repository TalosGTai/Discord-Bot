import disnake
from disnake.enums import ButtonStyle
from src.modules.games import Games


class PlayWarnButton(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label='Играть в Угадай число', style=ButtonStyle.blurple,
                       row=1)
    async def button_warn_play(self, button: disnake.ui.Button,
                               inter: disnake.MessageInteraction):
        game: Games = Games(inter.bot)
        await game.lucky_number(inter)


class PlayDuelButton(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label='Играть в Дуэль', style=ButtonStyle.blurple,
                       row=1)
    async def button_duel_play(self, button: disnake.ui.Button,
                          inter: disnake.MessageInteraction):
        game: Games = Games(inter.bot)
        await game.duel(inter)
