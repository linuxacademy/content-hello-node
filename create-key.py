import string
import random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

random_string = id_generator(32)

file = open("key.txt","w")
file.write(random_string)
file.close()
