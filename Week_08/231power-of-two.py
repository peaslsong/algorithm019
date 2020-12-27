def isPowerOfTwo(n):
    if bin(n).count('1') == 1:
        return True
    return False

a = 15
print(isPowerOfTwo(a))