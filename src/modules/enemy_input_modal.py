import disnake
from disnake.ext import commands


class EnemyModal(disnake.ui.Modal):
    def __init__(self, inter: disnake.MessageInteraction, bot: commands.Bot):
        super().__init__(
            title="Введи имя твоего противника",
            custom_id="enemy",
            timeout=30,
            components=[disnake.ui.TextInput(custom_id="enemy", label="enemy")],
        )
        self.inter = inter
        self.bot = bot

    async def send_enemy_modal(self):
        await self.inter.response.send_modal(
            title=self.title,
            custom_id=self.custom_id,
            components=self.components,
        )
        response: disnake.ModalInteraction = await self.bot.wait_for(
            "modal_submit",
            check=lambda i: i.custom_id == "enemy" and i.author.id == self.inter.author.id,
            timeout=300,
        )
        return response

