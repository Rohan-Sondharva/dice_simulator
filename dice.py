import random

# All possible dice result.
dice = ["""
-------
|     |
|  o  |
|     |
-------
""","""
-------
| o   |
|     |
|   o |
-------
""","""
-------
| o   |
|  o  |
|   o |
-------
""","""
-------
| o o |
|     |
| o o |
-------
""","""
-------
| o o |
|  o  |
| o o |
-------
""","""
-------
| o o |
| o o |
| o o |
-------
"""]

# Selecting random dice and print it.
print(f'{random.choice(dice)}')

