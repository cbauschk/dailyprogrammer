import math
import sys

def dottie(num):
    prev = num
    num = math.cos(num)
    while prev != num:
        prev = num
        num = math.cos(num)
    return num

def dottie_tan(num):
    prev = num
    num = num - math.tan(num)
    while prev != num:
        prev = num
        num = num - math.tan(num)
    return num

def dottie_div(num):
    prev = num
    num = num - (1 / num)
    while prev - num >= 0.0001:
        prev = num
        num = num - (1 / num)
    return num

def dottie_log_map(num):
    prev = num
    num = 4 * num * (1 - num)
    while prev != num:
        prev = num
        num = 4 * num * (1 - num)
    return num

if __name__ == '__main__':
    num = float(sys.argv[1])
    print(dottie(float(num)))
    print(dottie_tan(float(num)))
    print(dottie_div(float(num)))
    print(dottie_log_map(float(num)))
