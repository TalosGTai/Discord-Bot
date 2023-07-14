from disnake.ext import commands
import disnake
from Discord.functions.main_func import embed_question, find_channel_by_name, embed_wrong_channel


class Questions(commands.Cog):
    '''Вопросы от ведьмачки'''

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @commands.slash_command(name='вопрос_от_ведьмачки')
    async def question_philosophy(self, 
    inter: disnake.ApplicationCommandInteraction):
        '''Вопросы от ведьмачки'''

        if str(inter.guild.get_channel(inter.channel.id)) == 'вопросы-от-ведьмачки' or \
                inter.author.name == 'gtai':
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
            embed = embed_wrong_channel(channel, 'question')
            await inter.send(embed=embed)
            await inter.send(inter.author.name)


    @commands.slash_command(name='задай_вопрос')
    async def question_to_dina(self, 
    inter: disnake.ApplicationCommandInteraction, вопрос: str):
        '''Задай вопрос ведьмачке'''
        
        msg = 'В процессе разработки.\n Пиши ВСЕОТЦУ, если хочешь помочь ;)'
        await inter.send(msg)


def setup(bot: commands.Bot):
    bot.add_cog(Questions(bot))
