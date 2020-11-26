# import string
# import random


# def get_random_string(length):
#     rand_str = string.ascii_letters + string.digits
#     final_str = "".join(random.choice(rand_str) for i in range(length))
#     return final_str

j = [{"price": 5}, {"price": 10}]

t = []

for i in j:
    t.append(i["price"])

h = [i["price"] for i in j]
print(h)

print(sum(t))