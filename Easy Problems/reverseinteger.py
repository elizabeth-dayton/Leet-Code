def reverse(x):
    # :type x: int
    # :rtype: int

#Try 1 - ran in 16 ms and took 12.7 MB of memory
    if x == 0:
        return x
    x = str(x)[::-1]
    x = x.lstrip('0')
    if x.endswith('-'):
        x = x.rstrip('-')
        x = '-' + x
    x = int(x)
    if x > pow(2, 31) - 1 or x < pow(-2, 31):
        return 0    
    return x
    
#Testing
x = -321
print(reverse(x))