# Coupon Number program

import random

num = int(input("How many random number you want to generate : "))
input_random = []
for i in range(num):
    input_random.append(random.randint(1, 10))
print("The random coupon number are : ", input_random)
distinct_coupon_num = set()
for i in range(num):
    distinct_coupon_num.add(random.randint(1, 10))
print("The distinct coupon number are : ", distinct_coupon_num)
