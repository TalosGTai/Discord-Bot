import disnake
from disnake.enums import ButtonStyle
from disnake.ext import commands
import src.modules.panel_shop_buttons as shop
from src.functions.embeds import embed_shop_panel
from src.functions.describe import items, shop_panel


class ItemsPanelButtons(disnake.ui.View):
    def __init__(self, item: object, bot: object):
        super().__init__(timeout=None)
        self.bot = bot
        self.item = item

    @disnake.ui.button(label='Назад',
                       style=ButtonStyle.gray,
                       row=2)
    async def button_back(self,
                          button: disnake.ui.Button,
                          inter: disnake.MessageInteraction):
        '''Возврат к общей панели магазина'''

        await inter.response.edit_message(
            embed=embed_shop_panel(shop_panel()),
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
            embed=embed_shop_panel(items()),
            view=ItemsPanelButtons('', self.bot)
        )
