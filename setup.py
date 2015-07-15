from distutils.core import setup

setup(
    name='pokerWinner',
    version='1.0.0',
    packages=[
        'pokerWinner',
        'pokerWinner.tests'
    ],
    author='@jbrunsek',
    author_email='jbrunsek@outlook.com',
    description='Takes in two poker hands as separate strings and determins which hand is the winner'
)