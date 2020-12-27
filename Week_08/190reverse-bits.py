def reverseBits(n):
    print('n',bin(n))
    global b,c
    b = str(bin(n))
    c = '0b'
    for i in range(0, 32):
        if i < len(b) - 2:
            c = c + b[-1 - i]
        else:
            c = c + '0'
    return bin(int(c, 2))


a = 0b00000010100101000001111010011100
res = reverseBits(a)