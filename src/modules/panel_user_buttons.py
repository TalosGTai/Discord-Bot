import disnake
from disnake.enums import ButtonStyle
from disnake.ext import commands
from src.functions.describe import generate_password_describe,\
    transfer_money_describe, user_panel
from src.functions.embeds import embed_user_panel
import src.modules.panel_main_buttons as mp
import src.modules.panel_mainplus_buttons as mpp


class UserPanelButtons(disnake.ui.View):
    def __init__(self, permissions: bool):
        super().__init__(timeout=None)
        self.permissions = permissions

    @disnake.ui.button(label='Отправить монеты', style=ButtonStyle.blurple,
                       row=1)
    async def button_transfer_money(self, button: disnake.ui.Button,
                                    inter: disnake.MessageInteraction):
        '''Отправить монеты'''

        await inter.response.edit_message(
            embed=embed_user_panel(transfer_money_describe()),
            view=UserPanelButtons(self.permissions)
        )

    @disnake.ui.button(label='Генерация пароля', style=ButtonStyle.blurple,
                       row=1)
    async def button_generate_password(self, button: disnake.ui.Button,
                                       inter: disnake.MessageInteraction):
        '''Сгенерировать пароль'''

        await inter.response.edit_message(
            embed=embed_user_panel(generate_password_describe()),
            view=UserPanelButtons(self.permissions)
        )

    @disnake.ui.button(label='Назад', style=ButtonStyle.gray,
                       row=2)
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
