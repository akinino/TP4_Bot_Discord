from log import Logger
from discord.ext import commands
import discord


class CustomCommands(commands.Cog):
	
	def __init__(self, bot) -> None:
		super().__init__()
		self.bot = bot


	@commands.command(name="ping", pass_context=True)
	async def ping(self, ctx):
		msg = f"{ctx.message.author.name} a dit " + str(ctx.message.content)
		Logger.infoLog(msg)
		await ctx.send("pong")


	@commands.command(name="HELP", pass_context=True)
	async def HELP(self, ctx):
		msg = f"{ctx.message.author.name} a dit " + str(ctx.message.content)
		Logger.infoLog(msg)
		await ctx.send("les commandes possibles sont : ping")
