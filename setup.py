from setuptools import setup

setup(
    name='bot',
    author='barckcode',
    version='0.1',
    py_modules=['bot'],
    install_requires=[
        'Click',
        'instabot',
        'python-dotenv',
    ],
    entry_points='''
        [console_scripts]
        bot=bot:cli
    ''',
)

