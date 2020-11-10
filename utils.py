import string
import random


def get_random_string(length):
    rand_str = string.ascii_letters + string.digits
    final_str = "".join(random.choice(rand_str) for i in range(length))
    return final_str