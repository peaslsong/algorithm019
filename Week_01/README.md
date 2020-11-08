11.2
所有高级的的算法结构到了最后都会转化为if-else、for-loop、递归。所有算法化繁为简之后，找到重复单元，就可以泛化为下面的这些高级数据结构。

1.    切成碎片
2	Deliberate Practicing刻意练习
·	刻意练习-过遍数（五毒神掌）练习5遍
在第三、第四遍的时候看leetcode国际版的与你相关语言的前3个高赞

·	练习缺陷、弱点地方（有不舒服的地方就对了）
·	不舒服、不爽、枯燥
·	生活中的例子：乒乓球、台球、游戏等等，当你某一方面练习比较好的时候，这个会成为你的舒适区
3	Feedback
即时反馈
主动型反馈（自己去找）
高手代码（github、leetcode、etc）
第一视角直播
被动式反馈（高手给你指点）
Code review
教练看你打，给你反馈
切题

Pycharm中常用快捷键：
Ctrl+左右键 整个单词的移动
按住ctrl键之后，可以删除整个单词
点击三下 选取一行
自动生成函数 alt + enter
自顶向下编程思想
类似新闻稿的形式
把关键的内容、关键的逻辑放在最前面，把细节放在最后面
时间和空间复杂度
1.	知道你所写代码的时间和空间复杂度
2.	能够用最简洁的时间和空间复杂度完成


主定律
 
1.	二分查找（已排序）
2.	二叉树
3.	矩阵查找（已排序）
4.	归并排序

二叉树遍历、图遍历、DFS、BFS的时间复杂度是O（ｎ）

数组、链表、跳表的基本实现和特性
1.	看题5-10min
2.	看答案
3.	默写
4.	看题解
5.	去到国际站（去掉-cn）接着看题解：大千世界，就展现在我们面前，全世界的优秀解法。




11 盛最多的水
根据老师的想法用python写：
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        i = 0
        j = len(height)-1
        for i in range(len(height)-1):
            if i<j:
                if height[i]<height[j]:
                    minHeight=height[i]
                    i = i+1
                else:
                    minHeight = height[j]
                    j = j-1
                area = max(area, minHeight*(j-i+1))
        return area
但是会报错：
输入：
[2,3,4,5,18,17,6]
输出：
16
预期结果：
17


70. 爬楼梯
最大误区：做题只做一遍 至少5遍
优化思想：空间换时间，升维到2维去
懵逼的时候解题思路：
暴力？基本情况？

找最近重复子问题
If else，
For while，recursion
1:1
2:2
3:f(1)+f(2)
4:f(2)+f(3)
 
…
F(n) = f(n-1)+f(n-2)
递归
