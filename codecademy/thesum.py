def digit_sum(x):
    sum  = 0
    while x > 0:
        sum  = sum + x % 10
        x = x // 10
        print (x)
    return sum

v = digit_sum(111)
print (v)
