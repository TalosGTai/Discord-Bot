import disnake
from disnake.enums import ButtonStyle
from disnake.ext import commands


class RowButtons(disnake.ui.View):
    def __init__(self, answer: str):
        super().__init__(timeout=None)
        self.answer = answer

    @disnake.ui.button(label='Показать ответ', style=ButtonStyle.green)
    async def first_button(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        button.label = f'Ответ: {self.answer}'
        await inter.response.edit_message(view=self)
        #await inter.response.send_message('Ответ = 5')