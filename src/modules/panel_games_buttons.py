import disnake
from disnake.enums import ButtonStyle
from disnake.ext import commands
from src.functions.describe import lucky_number_describe,\
    duel_describe, user_panel
from src.functions.embeds import embed_games_panel, \
    embed_user_panel
from data.actions_config import lucky_number
import src.modules.panel_main_buttons as mp
import src.modules.panel_mainplus_buttons as mpp


class GamesPanelButtons(disnake.ui.View):
    def __init__(self, permissions: bool):
        super().__init__(timeout=None)
        self.permissions = permissions

    @disnake.ui.button(label='Угадай число', style=ButtonStyle.blurple,
                       row=1)
    async def button_warn(self, button: disnake.ui.Button,
                          inter: disnake.MessageInteraction):
        '''Игра Угадай число'''

        await inter.response.edit_message(
            embed=embed_games_panel(lucky_number_describe(
                lucky_number['timeout'])),
            view=GamesPanelButtons(self.permissions)
        )

    @disnake.ui.button(label='Дуэль', style=ButtonStyle.blurple,
                       row=1)
    async def button_duel(self, button: disnake.ui.Button,
                          inter: disnake.MessageInteraction):
        '''Игра Дуэль'''

        await inter.response.edit_message(
            embed=embed_games_panel(duel_describe()),
            view=GamesPanelButtons(self.permissions)
        )

    @disnake.ui.button(label='Назад', style=ButtonStyle.gray,
                       row=3)
    async def button_back(self, button: disnake.ui.Button,
                          inter: disnake.MessageInteraction):
        '''Назад'''

        if self.permissions:
            await inter.response.edit_message(
                embed=embed_user_panel(user_panel()),
                view=mpp.MainPlusPanelButtons(self.permissions)
            )
        else:
            await inter.response.edit_message(
                embed=embed_user_panel(user_panel()),
                view=mp.MainPanelButtons(self.permissions)
            )
