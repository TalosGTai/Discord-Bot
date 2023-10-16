import disnake
from disnake.enums import ButtonStyle
from disnake.ext import commands
from src.functions.describe import warn_describe, mute_describe,\
    unmute_describe, kick_describe, ban_describe, unban_describe, \
    user_panel
from src.functions.embeds import embed_moderator_panel, \
    embed_user_panel
import src.modules.panel_mainplus_buttons as mpp


class ModeratorPanelButtons(disnake.ui.View):
    def __init__(self, permissions: bool):
        super().__init__(timeout=None)
        self.permissions = permissions

    @disnake.ui.button(label='Предупреждение', style=ButtonStyle.danger,
                       row=1)
    async def button_warn(self, button: disnake.ui.Button,
                                inter: disnake.MessageInteraction):
        '''Команда Предупреждение'''

        await inter.response.edit_message(
                embed=embed_moderator_panel(warn_describe()),
            view=ModeratorPanelButtons(self.permissions)
                )

    @disnake.ui.button(label='Мут', style=ButtonStyle.danger,
                       row=1)
    async def button_mute(self, button: disnake.ui.Button,
                                   inter: disnake.MessageInteraction):
        '''Команда Мут'''

        await inter.response.edit_message(
            embed=embed_moderator_panel(mute_describe()),
            view=ModeratorPanelButtons(self.permissions)
        )

    @disnake.ui.button(label='Размут', style=ButtonStyle.danger,
                       row=1)
    async def button_unmute(self, button: disnake.ui.Button,
                                 inter: disnake.MessageInteraction):
        '''Команда Размут'''

        await inter.response.edit_message(
            embed=embed_moderator_panel(unmute_describe()),
            view=ModeratorPanelButtons(self.permissions)
        )

    @disnake.ui.button(label='Кик', style=ButtonStyle.danger,
                       row=2)
    async def button_moderator(self, button: disnake.ui.Button,
                               inter: disnake.MessageInteraction):
        '''Команда Кик'''

        await inter.response.edit_message(
            embed=embed_moderator_panel(kick_describe()),
            view=ModeratorPanelButtons(self.permissions)
        )

    @disnake.ui.button(label='Бан', style=ButtonStyle.danger,
                       row=2, )
    async def button_ban(self, button: disnake.ui.Button,
                                 inter: disnake.MessageInteraction):
        '''Команда Бан'''

        await inter.response.edit_message(
                embed=embed_moderator_panel(ban_describe()),
            view=ModeratorPanelButtons(self.permissions)
            )

    @disnake.ui.button(label='Разбан', style=ButtonStyle.danger,
                       row=2)
    async def button_unban(self, button: disnake.ui.Button,
                                inter: disnake.MessageInteraction):
        '''Команда Разбан'''
        
        await inter.response.edit_message(
            embed=embed_moderator_panel(unban_describe()),
            view=ModeratorPanelButtons(self.permissions)
        )
    
    @disnake.ui.button(label='Назад', style=ButtonStyle.gray,
                       row=3)
    async def button_back(self, button: disnake.ui.Button,
                          inter: disnake.MessageInteraction):
        '''Назад'''

        await inter.response.edit_message(
                embed=embed_user_panel(user_panel()),
                view=mpp.MainPlusPanelButtons(self.permissions)
            )
