from typing import List

g = [1, 2]
s = [1, 2, 3]
# g = [10, 9, 8, 7]
# s = [5, 6, 7, 8]


def findContentChildren(g: List[int], s: List[int]) -> int:
    '''
    新建一个字典v，用来存现在有多少5元和10元。
    如果顾客付的是5元，则5元数量加1；
    如果顾客付的是10元，则5元数量减1，10元数量加1；如果5元数量不够，则无法找零；
    如果顾客付的是20元，首先先用10元来找零，没有10元，则用5元找零，如果5元或10元数量不够，则无法找零。

    :param g:
    :param s:
    :return:
    '''
    num = 0
    i = 0
    s.sort()
    g.sort()
    for j in range(len(s)):
        if i < len(g) and s[j] >= g[i]:
            num = num + 1
            i = i + 1
        else:
            continue
    return num


print(findContentChildren(g, s))
