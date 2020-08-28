from instabot import Bot


def follow_user(user_login, user_password, user):
    """
        Function to follow a user
    """

    # Initialize Bot.
    bot = Bot()


    # Login to Instagram.
    bot.login(username=user_login, password=user_password)


    # Follow user
    bot.follow(user)
