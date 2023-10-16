import disnake
from disnake.enums import ButtonStyle
from disnake.ext import commands
from src.functions.embeds import embed_shop_panel
from src.functions.describe import roles, events, items,\
all_goods
import src.modules.panel_roles_buttons as rls
import src.modules.panel_items_buttons as its
import src.modules.panel_events_shop_buttons as events_shop
import src.modules.panel_all_goods_buttons as goods


class ShopPanelButtons(disnake.ui.View):
    def __init__(self, bot: object):
        super().__init__(timeout=None)
        self.bot = bot

    @disnake.ui.button(label='Роли', style=ButtonStyle.blurple,
                       row=1)
    async def button_roles(self, button: disnake.ui.Button,
                                    inter: disnake.MessageInteraction):
        '''Запуск панели ролей'''

        await inter.response.edit_message(
            embed=embed_shop_panel(roles()),
            view=rls.RolesPanelButtons('', self.bot)
        )

    @disnake.ui.button(label='События', style=ButtonStyle.blurple,
                       row=1)
    async def button_events_shop(self, button: disnake.ui.Button,
                                       inter: disnake.MessageInteraction):
        '''Запуск панели событий'''

        await inter.response.edit_message(
            embed=embed_shop_panel(events()),
            view=events_shop.EventsShopPanelButtons('', self.bot)
        )

    @disnake.ui.button(label='Предметы', style=ButtonStyle.blurple,
                       row=1)
    async def button_items(self, button: disnake.ui.Button,
                                       inter: disnake.MessageInteraction):
        '''Запуск панели Предметов'''

        await inter.response.edit_message(
            embed=embed_shop_panel(items()),
            view=its.ItemsPanelButtons('', self.bot)
        )

    @disnake.ui.button(label='Все товары', style=ButtonStyle.blurple,
                       row=1)
    async def button_all_goods(self, button: disnake.ui.Button,
                                       inter: disnake.MessageInteraction):
        '''Запуск панели всех товаров'''

        await inter.response.edit_message(
            embed=embed_shop_panel(all_goods()),
            view=goods.GoodsPanelButtons('', self.bot)
        )
