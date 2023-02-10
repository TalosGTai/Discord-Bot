from discord.ext import commands
import os


class Cogs(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load_all(self, ctx):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                self.client.load_extension(f'cogs.{filename[:-3]}')
        await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, extension):
        self.client.load_extension(f'cogs.{extension}')
        await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')
        await ctx.message.delete()

def setup(client):
    client.add_cog(Cogs(client))