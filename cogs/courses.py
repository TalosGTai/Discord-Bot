from dis import disco
from http import client
from discord.ext import commands
import discord
from functions import ege_24_text_1
from functions import ege_24_text_2
from functions import ege_25_text_1
from functions import ege_25_text_2
from functions import ege_26_text_1
from functions import ege_26_text_2


class COURSES(commands.Cog):
    '''Курсы'''

    def __init__(self, client) -> None:
        self.client = client

    @commands.cooldown(rate=1, per=1, type=commands.BucketType.user)
    @commands.command()
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
        
        #await ctx.message.delete()
        await user.send(embed=embed_1)
        await user.send(embed=embed_2)

    @commands.cooldown(rate=1, per=1, type=commands.BucketType.user)
    @commands.command()
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

        #await ctx.message.delete()
        await user.send(embed=embed_1)
        await user.send(embed=embed_2)

    @commands.cooldown(rate=1, per=1, type=commands.BucketType.user)
    @commands.command()
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

        #await ctx.message.delete()
        await user.send(embed=embed_1)
        await user.send(embed=embed_2)


    @commands.cooldown(rate=1, per=1, type=commands.BucketType.user)
    @commands.command()
    async def krugosvetka_pro(self, ctx):
        '''Мастер-группа Кругосветка PRO ЕГЭ по Информатике'''

        user = ctx.message.author
        author = 'GTai — Всеотец'
        owner = await self.client.fetch_user(172383544201445376)

        title, description, color = ege_26_text_1()
        embed_1 = discord.Embed(
            title=title, description=description, color=color)
        embed_1.set_author(name=author)

        description = ege_26_text_2(owner)
        embed_2 = discord.Embed(description=description, color=color)

        #await ctx.message.delete()
        await user.send(embed=embed_1)
        await user.send(embed=embed_2)
    

    @commands.cooldown(rate=1, per=1, type=commands.BucketType.user)
    @commands.command()
    async def c_university(self, ctx):
        '''Видео-курс Си для ВУЗа'''

        user = ctx.message.author
        author = 'GTai — Всеотец'
        owner = await self.client.fetch_user(172383544201445376)

        title, description, color = ege_26_text_1()
        embed_1 = discord.Embed(
            title=title, description=description, color=color)
        embed_1.set_author(name=author)

        description = ege_26_text_2(owner)
        embed_2 = discord.Embed(description=description, color=color)

        #await ctx.message.delete()
        await user.send(embed=embed_1)
        await user.send(embed=embed_2)


def setup(client):
    client.add_cog(COURSES(client))