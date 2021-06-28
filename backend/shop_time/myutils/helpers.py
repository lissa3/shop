import random
import string
import os
from django.utils import timezone

# return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

def make_rand_str():    
    return ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(4))


def upload_prod(instance, filepath):
    """make path to uploaded file (product) and adjust file name if needed. 
    
    """
    # TODO: check for spaces or other awkward characters in file name
    filename = os.path.basename(filepath)         # 'abababa.jpeg'
    name, ext = os.path.splitext(filename)         # tuple ('abababa', '.jpeg')
    if len(name) > 5:
        name = name[:15]
    new_file_name = name +  ext
    added_time = timezone.now().strftime('%B-%Y')
    path = added_time.strftime("%B-%Y")
    folder = f'{path}'
        # new_file_name = name + instance.slug+ext
        # return os.path.join('ideapot', new_file_name)
    return os.path.join('products', folder, new_file_name)
    
        