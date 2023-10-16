import disnake
from disnake.enums import ButtonStyle
from disnake.ext import commands
import src.modules.panel_shop_buttons as shop
from src.functions.embeds import embed_shop_panel
from src.functions.describe import all_goods, shop_panel


class GoodsPanelButtons(disnake.ui.View):
    def __init__(self, item: object, bot: object):
        super().__init__(timeout=None)
        self.item = item
        self.bot = bot

    @disnake.ui.button(label='Назад',
                       style=ButtonStyle.gray,
                       row=2)
    async def button_back(self,
                          button: disnake.ui.Button,
                          inter: disnake.MessageInteraction):
        '''Возврат к общей панели магазина'''

        await inter.response.edit_message(
            embed=embed_shop_panel(all_goods()),
            view=shop.ShopPanelButtons(self.bot)
        )

    @disnake.ui.button(
        label='Купить',
        style=ButtonStyle.green,
        row=2)
    async def button_buy(self,
                         button: disnake.ui.Button,
                         inter: disnake.MessageInteraction):
        '''Покупка товара'''

        await inter.response.edit_message(
            embed=embed_shop_panel(all_goods()),
            view=GoodsPanelButtons('', self.bot)
        )
