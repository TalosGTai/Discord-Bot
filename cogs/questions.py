from disnake.ext import commands
import disnake
from functions import embed_question, find_channel_by_name


class Questions(commands.Cog):
    '''Вопросы от ведьмачки'''

    def __init__(self, bot) -> None:
        self.bot = bot


    @commands.slash_command(name='вопрос_от_ведьмачки')
    async def question_philosophy(self, 
    inter: disnake.ApplicationCommandInteraction):
        '''Вопросы от ведьмачки'''

        if str(inter.guild.get_channel(inter.channel.id)) == 'вопросы-от-ведьмачки' or \
                inter.author.display_name == 'GTai':
            description, color = embed_question()
            question = description
            embed = disnake.Embed(description=description, color=color)
            
            if len(question) >= 100:
                question = str(question.split('?')[0])
            if len(question) >= 100:
                question = 'Философия X'

            await inter.send(embed=embed)
            msg = await inter.channel.history().flatten()
            await inter.channel.create_thread(name=question, message=msg[0])
        else:
            channel = find_channel_by_name(self.bot, 'вопросы-от-ведьмачки')
            msg = f'Вопросы от меня ты можешь получить на канале {channel.mention}'
            await inter.send(msg)


def setup(bot):
    bot.add_cog(Questions(bot))
