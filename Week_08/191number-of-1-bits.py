def hammingWeight(n):
    num = 0
    n = bin(n)
    while n != 0:
        num = num + 1
        n = n & (n - 1)
    return num

# print(hammingWeight(00000000000000000000000000001011))
