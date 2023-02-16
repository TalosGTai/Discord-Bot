from disnake.ext import commands
import disnake
from functions import embed_question


class Questions(commands.Cog):
    '''Вопросы от ведьмачки'''

    def __init__(self, bot) -> None:
        self.bot = bot


    @commands.slash_command(name='вопрос_от_ведьмачки')
    async def question_philosophy(self, 
    inter: disnake.ApplicationCommandInteraction):
        '''Вопросы от ведьмачки'''

        description, color = embed_question()
        question = description
        embed = disnake.Embed(description=description, color=color)
        
        if len(question) >= 100:
            question = str(question.split('?')[0])
        if len(question) >= 100:
            question = 'Философия X'

        await inter.send(embed=embed)
        msg = await inter.channel.history().flatten()
        await inter.channel.create_thread(name=question, message=msg[-1])


def setup(bot):
    bot.add_cog(Questions(bot))
