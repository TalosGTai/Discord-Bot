from discord.ext import commands
import discord
from functions import ege_24_text_1
from functions import ege_24_text_2
from functions import ege_25_text_1
from functions import ege_25_text_2
from functions import ege_26_text_1
from functions import ege_26_text_2
from functions import krugosvetka_pro_text_1
from functions import krugosvetka_pro_text_2
from functions import c_university_text_1
from functions import c_university_text_2
from functions import trainer_2_text

class COURSES(commands.Cog):
    '''Курсы'''

    def __init__(self, client) -> None:
        self.client = client

    @commands.cooldown(rate=1, per=1, type=commands.BucketType.user)
    @commands.command(name='егэ_24', aliases=['егэ24', 'ege24', 'ege_24'])
    async def ege_24(self, ctx):
        '''Курс 24ого задания ЕГЭ по Информатике'''
        
        user = ctx.message.author
        author = 'GTai — Всеотец'
        owner = await self.client.fetch_user(172383544201445376)

        title, description, color = ege_24_text_1()
        embed_1 = discord.Embed(title=title, description=description, color=color)
        embed_1.set_author(name=author)
        description = ege_24_text_2(owner)
        embed_2 = discord.Embed(description=description, color=color)
        
        await user.send(embed=embed_1)
        await user.send(embed=embed_2)
        await ctx.message.delete()


    @commands.cooldown(rate=1, per=1, type=commands.BucketType.user)
    @commands.command(name='егэ_25', liases=['егэ25', 'ege25', 'ege_25'])
    async def ege_25(self, ctx):
        '''Курс 25ого задания ЕГЭ по Информатике'''

        user = ctx.message.author
        author = 'GTai — Всеотец'
        owner = await self.client.fetch_user(172383544201445376)

        title, description, color = ege_25_text_1()
        embed_1 = discord.Embed(
            title=title, description=description, color=color)
        embed_1.set_author(name=author)

        description = ege_25_text_2(owner)
        embed_2 = discord.Embed(description=description, color=color)

        await user.send(embed=embed_1)
        await user.send(embed=embed_2)
        await ctx.message.delete()


    @commands.cooldown(rate=1, per=1, type=commands.BucketType.user)
    @commands.command(name = 'егэ_26', aliases=['егэ26', 'ege26', 'ege_26'])
    async def ege_26(self, ctx):
        '''Курс 26ого задания ЕГЭ по Информатике'''

        user = ctx.message.author
        author = 'GTai — Всеотец'
        owner = await self.client.fetch_user(172383544201445376)

        title, description, color = ege_26_text_1()
        embed_1 = discord.Embed(
            title=title, description=description, color=color)
        embed_1.set_author(name=author)

        description = ege_26_text_2(owner)
        embed_2 = discord.Embed(description=description, color=color)

        await user.send(embed=embed_1)
        await user.send(embed=embed_2)
        await ctx.message.delete()


    @commands.cooldown(rate=1, per=1, type=commands.BucketType.user)
    @commands.command(name='кругосветка', aliases=['кругосветкапро', 'krugosvetka', 'кругосветка_про', 'krugosvetka_pro'])
    async def krugosvetka_pro(self, ctx):
        '''Мастер-группа Кругосветка PRO ЕГЭ по Информатике'''

        user = ctx.message.author
        author = 'GTai — Всеотец'
        owner = await self.client.fetch_user(172383544201445376)

        title, description, color = krugosvetka_pro_text_1()
        embed_1 = discord.Embed(
            title=title, description=description, color=color)
        embed_1.set_author(name=author)

        description = krugosvetka_pro_text_2(owner)
        embed_2 = discord.Embed(description=description, color=color)

        await user.send(embed=embed_1)
        await user.send(embed=embed_2)
        await ctx.message.delete()
    

    @commands.cooldown(rate=1, per=1, type=commands.BucketType.user)
    @commands.command(name='c_university', aliases=['с вуз', 'с_вуз', 'c_univer'])
    async def c_university(self, ctx):
        '''Видео-курс Си для ВУЗа'''

        user = ctx.message.author
        author = 'GTai — Всеотец'
        owner = await self.client.fetch_user(172383544201445376)

        title, description, color = c_university_text_1()
        embed_1 = discord.Embed(
            title=title, description=description, color=color)
        embed_1.set_author(name=author)

        description = c_university_text_2(owner)
        embed_2 = discord.Embed(description=description, color=color)

        await user.send(embed=embed_1)
        await user.send(embed=embed_2)
        await ctx.message.delete()


    @commands.cooldown(rate=1, per=1, type=commands.BucketType.user)
    @commands.command(name='егэ_2', aliases=['егэ2', 'ege2', 'тренажёр2', 'тренажер2', 'trainer2', 'trainer_2'])
    async def trainer_2(self, ctx):
        '''Курс-тренажёр по 2ому заданию ЕГЭ Информатика'''

        user = ctx.message.author
        author = 'GTai — Всеотец'
        owner = await self.client.fetch_user(172383544201445376)

        title, description, color = trainer_2_text()
        embed_1 = discord.Embed(
            title=title, description=description, color=color)
        embed_1.set_author(name=author)

        await user.send(embed=embed_1)
        await ctx.message.delete()


def setup(client):
    client.add_cog(COURSES(client))