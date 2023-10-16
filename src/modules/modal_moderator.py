import disnake
from disnake.ext import commands
from disnake import TextInputStyle


class ModeratorModal(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="Имя",
                placeholder="nickname",
                custom_id="user_name",
                style=TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="Причина",
                placeholder="Оскорбительное поведение",
                custom_id="reason",
                style=TextInputStyle.paragraph,
            ),
        ]
        super().__init__(
            title="Предупреждение пользователю",
            custom_id="warn",
            components=components,
        )


    async def callback(self, inter: disnake.ModalInteraction):
        embed = disnake.Embed(title="Создание тега")
        for key, value in inter.text_values.items():
            embed.add_field(
                name=key.capitalize(),
                value=value[:1024],
                inline=False,
            )
        await inter.response.send_message(embed=embed)
