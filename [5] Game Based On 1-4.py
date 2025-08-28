# ROLL THE DICE GAME

import random
nums = random.randrange(1, 6)
print("You rolled: ", nums)


# GIVE A RANDOM PASSWORD

import random
import string

characters = string.ascii_letters + string.digits # a-z, A-Z, 0-9
password = ''.join(random.choices(characters, k=8))

print("Your random password is: ", password)