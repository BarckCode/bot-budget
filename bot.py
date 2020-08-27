import click
from instagram_bot.main import instagram_main


@click.group()
def cli():
    pass


@click.command()
def instagram():
    click.echo('Bot para Instagram')


@click.command()
def telegram():
    click.echo('Bot para Telegram')


@click.command()
def twitter():
    click.echo('Bot para Twitter')


cli.add_command(instagram)
cli.add_command(telegram)
cli.add_command(twitter)


if __name__ == '__main__':
    cli()