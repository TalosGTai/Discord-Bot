import disnake
from disnake.enums import ButtonStyle
from disnake.ext import commands
import src.modules.panel_shop_buttons as shop
from src.functions.embeds import embed_shop_panel
from src.functions.describe import shop_panel, \
role_color_with_icon, role_color_without_icon, \
role_color_without, role_color_with_icon_sep, \
role_color_without_icon_sep, user_got_item,\
user_congratulation, roles
from src.functions.discord import purchase_item, \
find_channel_by_name
from src.modules.config import roles_cost


class RolesPanelButtons(disnake.ui.View):
    def __init__(self, role: str, bot: object):
        super().__init__(timeout=None)
        self.role = role
        self.bot = bot

    @disnake.ui.button(label='Выделенная роль с цветом и картинкой',
                       style=ButtonStyle.blurple,
                       row=1)
    async def button_buy_role_color_icon_sep(
        self, 
        button: disnake.ui.Button,
        inter: disnake.MessageInteraction):
        '''Роль с цветом и картинкой'''

        await inter.response.edit_message(
            embed=embed_shop_panel(role_color_with_icon_sep()),
            view=RolesPanelButtons('role_color_with_icon_sep', self.bot)
        )

    @disnake.ui.button(label='Роль с цветом и картинкой',
                    style=ButtonStyle.blurple,
                    row=1)
    async def button_buy_role_color_icon(
        self, 
        button: disnake.ui.Button,
        inter: disnake.MessageInteraction):
        '''Роль с цветом и картинкой'''

        await inter.response.edit_message(
            embed=embed_shop_panel(role_color_with_icon()),
            view=RolesPanelButtons('role_color_with_icon', self.bot)
        )

    @disnake.ui.button(label='Выделенная роль с цветом', 
                       style=ButtonStyle.blurple,
                       row=2)
    async def button_buy_role_color_sep(
        self, 
        button: disnake.ui.Button,
        inter: disnake.MessageInteraction):
        '''Роль с цветом и без картинки'''

        await inter.response.edit_message(
            embed=embed_shop_panel(role_color_without_icon_sep()),
            view=RolesPanelButtons('role_color_without_icon_sep', self.bot)
        )

    @disnake.ui.button(label='Роль с цветом', 
                       style=ButtonStyle.blurple,
                       row=2)
    async def button_buy_role_color(
        self,
        button: disnake.ui.Button,
        inter: disnake.MessageInteraction):
        '''Роль с цветом и без картинки'''

        await inter.response.edit_message(
            embed=embed_shop_panel(role_color_without_icon()),
            view=RolesPanelButtons('role_color_without_icon', self.bot)
        )

    @disnake.ui.button(label='Роль без цвета', 
                       style=ButtonStyle.blurple,
                       row=2)
    async def button_buy_role_without(
        self, 
        button: disnake.ui.Button,
        inter: disnake.MessageInteraction):
        '''Роль без цвета и картинки'''

        await inter.response.edit_message(
            embed=embed_shop_panel(role_color_without()),
            view=RolesPanelButtons('role_color_without', self.bot)
        )

    @disnake.ui.button(label='Назад', style=ButtonStyle.gray,
                       row=3)
    async def button_back(self, button: disnake.ui.Button,
                                       inter: disnake.MessageInteraction):
        '''Возврат к общей панели магазина'''

        await inter.response.edit_message(
            embed=embed_shop_panel(shop_panel()),
            view=shop.ShopPanelButtons(self.bot)
        )

    @disnake.ui.button(label='Купить', style=ButtonStyle.green,
                       row=3)
    async def button_buy_item(self, button: disnake.ui.Button,
                              inter: disnake.MessageInteraction):
        '''Покупка товара'''

        if self.role != '':
            user = inter.author
            item = {
                'name': self.role,
                'price': roles_cost[self.role]
            }

            if purchase_item(item, user.name):
                # add to db
                # msg for moderators
                got_item = user_got_item(user, item['name'])
                if got_item:
                    channel = find_channel_by_name(self.bot, 'модераторы')
                    await channel.send(got_item)
                # msg congratulation to user
                await inter.response.edit_message(
                    embed=embed_shop_panel(user_congratulation(item['name']))
                )
            else:
                msg = 'Недостаточно монет на покупку товара!'
                embed = embed_shop_panel(shop_panel())
                embed.add_field('Недостаточно монет', value=msg, inline=False)

                await inter.response.edit_message(
                    embed=embed,
                    view=RolesPanelButtons('', self.bot)
                )
        else:
            await inter.response.edit_message(
                embed=embed_shop_panel(roles()),
                view=RolesPanelButtons('', self.bot)
            )
