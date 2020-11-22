之前自己面试的时候总是很怕考代码，参加了算法训练营才知道前辈们已经想了很多办法，靠自己想几乎是想不出来的。听了超哥的几周课之后，感觉还是有些吃力，在力扣上也会看看别人的题解，感觉超哥的课适合基础比较好或比较聪明的同志们。不过超哥总结了很多道理，听过之后还是受益匪浅，超哥的很多方法也刷新了我自己的认知范围，让我快速进入算法的圈子。虽然很难，自己理解一道题也需要很长时间，自己代码水平也一般般，但还是要坚持吧，毕竟花钱啦。
下面的笔记是收集了超哥讲的几个算法题。
22.括号生成
'''
这道题超哥是用java实现的，自己抄了一遍，竟然跑失败了，后来还是转战自己熟悉的python，调试了很久终于提交成功了
'''
def _generate(left, right, n, s):
    if left == n & right == n:
        result.append(s)
        return
    if left < n:
        _generate(left + 1, right, n, s + "(")
    if left > right:
        _generate(left, right + 1, n, s + ")")
    return result


print(_generate(0, 0, 2, ''))

50.Pow(x,n)
'''
这道题自己low low地分别用用土办法和递归实现了一下，然后看了超哥的解法
'''
if n == 0:
    result = 1
elif n < 0:
    for i in range(abs(n)):
        result = result / x
else:
    for i in range(n):
        result = result * x


def myPow(x, n):
    result = 1
    if n == 0:
        return result
    else:
        result = x*myPow(x, n-1)
    return result

78.子集
'''
这道题自己想了很久还是没有思路，摘录超哥推荐的code
'''
def subsets(nums, k):
    res = [[]]
    for i in nums:
        res = res + [[i] + num for num in res]
    return res
    
17.电话号码的组合
'''
这道题自己也挣扎地写了一下，因为和上一道子集题有点像，总是感觉要写出来但实际上还是写不出来，结合了超哥的思路，最后代码写成这样
'''
phone_dict = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

digits = '23'
l = []
for i in digits:
    l.append(phone_dict[i])
result = []


def search(s, digits, i, result, l):
    if i == len(digits):
        result.append(s)
        return
    letters = l[i]
    for j in range(len(letters)):
        search(s + letters[j], digits, i + 1, result, l)


print(search('', digits, 0, result, l))

51.N皇后
'''
这道题虽然超哥给出了思路和解法，但是感觉已经超纲了，估计我还得多刷几遍，才可以理解
'''
