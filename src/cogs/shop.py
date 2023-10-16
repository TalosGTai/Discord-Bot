from disnake.ext import commands
import disnake
from src.functions.embeds import embed_shop_panel
from src.functions.describe import shop_panel
from src.modules.panel_shop_buttons import ShopPanelButtons


class Shop(commands.Cog):
    '''Магазин'''

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    shop_items = commands.option_enum(['Роли', 'События', 'Предметы',
                                        'Разное'])
    
    #@commands.slash_command(name='купить')
    async def buy_items(self, 
                        inter: disnake.GuildCommandInteraction,
                        тип: shop_items):
        '''Покупка товаров в магазине'''

        msg = f'Находится в разработке. Появится в ближайшее время!'

        await inter.send(msg)

    #@commands.slash_command(name='продать')
    async def sell_items(self,
                         inter: disnake.GuildCommandInteraction,
                        тип: shop_items):
        '''Продажа предметов в магазине'''

        msg = f'Находится в разработке. Появится в ближайшее время!'

        await inter.send(msg)

    @commands.slash_command(name='магазин')
    async def show_items(self,
                         inter: disnake.GuildCommandInteraction):
        '''Здесь ты можешь купить любые товары'''

        view = disnake.ui.View()

        embed = embed_shop_panel(shop_panel())
        await inter.send(embed=embed, view=ShopPanelButtons(self.bot))


def setup(bot: commands.Bot):
    bot.add_cog(Shop(bot))