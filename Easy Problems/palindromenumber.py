def isPalindrome(x):
        
        # :type x: int
        # :rtype: bool

#Try 1 - ran in 44 ms and took 12.9 MB of memory        
    # if x == 0:
    #      return True
    # x = str(x)
    # y = x[::-1]
    # y = y.lstrip('0')
    # return x == y

#Try 2 - ran in 40 ms and took 12.9 MB of memory
    # if x < 0:
    #     return False
    # return str(x) == str(x)[::-1]

#Try 3 - ran in 36 ms and took 12.6 MB of memory

    return str(x) == str(x)[::-1]


#Testing
x = 1221
print(isPalindrome(x))