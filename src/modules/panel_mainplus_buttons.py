import disnake
from disnake.enums import ButtonStyle
from disnake.ext import commands
import src.modules.panel_moderator_buttons as pm
from src.functions.embeds import embed_moderator_panel, \
    embed_games_panel, embed_user_panel
from src.functions.describe import moderator_panel, games_panel, \
    user_panel
import src.modules.panel_games_buttons as pg
import src.modules.panel_user_buttons as pu


class MainPlusPanelButtons(disnake.ui.View):
    def __init__(self, permissions: bool):
        super().__init__(timeout=None)
        self.permissions = permissions

    @disnake.ui.button(label='Действия', style=ButtonStyle.blurple,
                       row=1)
    async def button_user_actions(self, button: disnake.ui.Button,
                                   inter: disnake.MessageInteraction):
        '''Команды для Действий пользователя'''

        await inter.response.edit_message(
            embed=embed_user_panel(user_panel()),
            view=pu.UserPanelButtons(self.permissions)
        )

    @disnake.ui.button(label='Игры', style=ButtonStyle.blurple,
                       row=1)
    async def button_user_games(self, button: disnake.ui.Button,
                                 inter: disnake.MessageInteraction):
        '''Команды для Игр через бота'''

        await inter.response.edit_message(
            embed=embed_games_panel(games_panel()),
            view=pg.GamesPanelButtons(self.permissions)
        )

    @disnake.ui.button(label='Администрирование', style=ButtonStyle.blurple,
                       row=1)
    async def button_moderator(self, button: disnake.ui.Button,
                               inter: disnake.MessageInteraction):
        '''Команды для модераторов'''

        await inter.response.edit_message(
            embed=embed_moderator_panel(moderator_panel()),
            view=pm.ModeratorPanelButtons(self.permissions)
            )