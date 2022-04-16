from discord.ext.commands import Bot
from discord.ext.commands.context import Context
from message import CustomCommands
from log import Logger

import argparse
import json

class MyBot(Bot):

	def __init__(self, config):
		super().__init__(str(config['prefix']))
		
		self.add_cog(CustomCommands(self))
		self.add_cog(Logger(self, config))


	async def on_ready(self):
		print(f'{self.user} has connected to Discord!')


def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-c", "--config", help="Config file", required=True, dest="config")
	return parser.parse_args()


def main():
	args = get_args()
	config = json.load(open(args.config))
	
	bot = MyBot(config)
	bot.run(str(config['token']))


if __name__ == "__main__":
	main()