import click

# Local Modules
from instagram_bot.main import instagram
from telegram_bot.main import telegram
from twitter_bot.main import twitter


@click.group()
def cli():
    pass


cli.add_command(instagram)
cli.add_command(telegram)
cli.add_command(twitter)


if __name__ == '__main__':
    cli()