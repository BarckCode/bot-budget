import click

# Utils:
from .utils.conf import _get_environment_variables

# Functions:
from .follow import follow_user

@click.command()
@click.option(
    '-a',
    '--action',
    'action',
    type=click.Choice([
        'follow',
        'like',
    ], case_sensitive=False),
    required=True,
    help='Action to be taken by the bot',
)
@click.option(
    '-u',
    '--user',
    'user',
    prompt='Instagram user',
    help='Instagram user'
)
def instagram(action, user):
    """
        Bot for Instagram
    """

    # Get Instagram login data
    _instagram_data = _get_environment_variables()


    # Instagram bot options:
    if action == 'follow' and user != 'undefined' :
        follow_user(
            _instagram_data[0],
            _instagram_data[1],
            user
        )

