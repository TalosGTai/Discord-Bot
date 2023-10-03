from disnake.ext import commands
from disnake import Embed
import disnake
from src.functions.roles import get_all_roles, roles_main,\
    roles_games, roles_it, get_all_msg_roles
from src.functions.discord import find_channel_by_name,\
    find_role_by_name, find_user_by_id


class Dina(commands.Cog):
    '''Управление Диной'''

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @commands.command(name='send_msg', aliases=['send', 'смс'])
    @commands.has_permissions(administrator=True)
    async def send_msg(self, inter: disnake.ApplicationCommandInteraction,
     msg_channel, msg):
        '''Отправить сообщение в чат
        
        Шаблон: command channel msg
        Пример: .send_msg "егэ-чат" "Привет, ведьмак ^_^"
        '''

        for guild in self.bot.guilds:
            for channel in guild.channels:
                if channel.name == msg_channel:
                    await channel.send(msg)


    @commands.command(name='send_embed', aliases=['embed'])
    @commands.has_permissions(administrator=True)
    async def send_embed(self, inter: disnake.ApplicationCommandInteraction,
     msg_channel: str, title: str, description: str, color: str):
        '''Отправить сообщение в чат
        
        Шаблон: command channel msg
        Пример: .send_embed "егэ-чат" "Заголовок" "текст" "0x0004eb"
        '''
        
        color = int(color, 16)
        embed = disnake.Embed(title=title,
                              description=description, color=color)

        for guild in self.bot.guilds:
            for channel in guild.channels:
                if channel.name == msg_channel:
                    await channel.send(embed=embed)


    @commands.command(name='clear', aliases=['очистить', 'удалить'])
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, count: int):
        '''Удаление сообщений
        
        Шаблон: .clear count
        Пример: .clear 5
        '''

        await ctx.channel.purge(limit=int(count))
        await ctx.message.delete()
        

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        '''События при добавлении роли'''

        msg_id = int(payload.message_id)
        if msg_id in get_all_msg_roles():
            emoji = str(payload.emoji)
            member = payload.member
            roles = get_all_roles(self.bot)
            role = find_role_by_name(self.bot, roles[emoji])
            await member.add_roles(role)


    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        '''События при удалении роли'''

        msg_id = int(payload.message_id)
        if msg_id in get_all_msg_roles():
            emoji = str(payload.emoji)
            member = find_user_by_id(self.bot, payload.user_id)
            roles = get_all_roles(self.bot)
            role = find_role_by_name(self.bot, roles[emoji])
            await member.remove_roles(role)


    @commands.command(name='create_msg_role_main')
    @commands.has_permissions(administrator=True)
    async def create_msg_role_main(self, ctx):
        msg = roles_main()
        embed = Embed(description=msg['description'], color=msg['color'])
        channel = find_channel_by_name(self.bot, 'роли')
        await channel.send(embed=embed)


    @commands.command(name='create_msg_role_code')
    @commands.has_permissions(administrator=True)
    async def create_msg_role_it(self, ctx):
        msg = roles_it(self.bot)
        embed = Embed(title=msg['title'], description=msg['description'],
                       color=msg['color'])
        channel = find_channel_by_name(self.bot, 'роли')
        await channel.send(embed=embed)


    @commands.command(name='create_msg_role_games')
    @commands.has_permissions(administrator=True)
    async def create_msg_role_games(self, ctx):
        msg = roles_games()
        embed = Embed(description=msg['description'], color=msg['color'])
        channel = find_channel_by_name(self.bot, 'роли')
        await channel.send(embed=embed)
    

    @commands.command(name='add_role_to_msg')
    @commands.has_permissions(administrator=True)
    async def add_role_to_msg(self, ctx):
        channel = find_channel_by_name(self.bot, 'роли')
        msg = await channel.fetch_message(1158408970160050287)
        await msg.add_reaction('<:js:848668818385010708>')
        

def setup(bot: commands.Bot):
    bot.add_cog(Dina(bot))