import disnake
from disnake.ext import commands

class DropDownEGE(disnake.ui.StringSelect):
    def __init__(self):
        options = [
            disnake.SelectOption(label='Лёгкая'),
            disnake.SelectOption(label='Средняя'),
            disnake.SelectOption(label='Сложная')
        ]

        super().__init__(
            placeholder='Choice',
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, inter: disnake.MessageInteraction) -> None:
        await inter.response.send_message(f'Выбор {self.values[0]}')


class DrowDownEGEView(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(DropDownEGE)