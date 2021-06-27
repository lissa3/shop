import random
import string
# return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

def make_rand_str():    
    return ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(4))