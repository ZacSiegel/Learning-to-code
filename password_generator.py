import random 
import string

print('Welcome to Password Generator!')

pass_len = int(input('\nPlease enter the length of the password:\n'))
# lowercase alphabet
lower = string.ascii_lowercase

# uppercase alphabet
upper = string.ascii_uppercase

# ints from 0-9
num = string.digits

# symbol characters
symbols = string.punctuation

combined = lower + upper + num + symbols

# creates a random list chosen from the combined variable 
# that is pass_len length 
temp = random.sample(combined, pass_len)

# this will join all the characters together in the list
password = ''.join(temp)

print(f'Your new password is {password}')
