# from matplotlib import pyplot as plt
# from math import trunc as tr
import math
import random

alpha = 2 / (1 + pow(5, 0.5))

def hash1(value):
    global alpha
    m = 971
    bucket = math.trunc((value * alpha -  math.trunc(value * alpha)) * m)
    return bucket

def hash2(n):
    global alpha
    M = 971
    h = math.floor((n * alpha) % 1 * M)
    # print(h)
    return h

myhist = [0] * 971
for i in range(1000000):
    #h = hash1(random.randint(0, 999999))
    h = hash2(i)
    myhist[h] += 1 

print(myhist)