# -*- coding:utf-8 -*-

li = [1, 3, 4, 2, 5]
s ='hello'
t = (1, 2, 'a', 'b')
def search(li, key):
    '''
1.顺序查找
'''
    for i,element in enumerate(li):
        if element == key:
            print('顺序查找：找到{1}在第{0}个位置'.format(i+1, key))
search(li,2)
search(s, 'e')
search(t, 1)


def search_two(li,key):
    '''
    2.二分查找
    '''

    li = sorted(li)
    i = 0
    j = len(li)-1
    while i < j:
        mid = (i+j)//2
        if li[mid] == key:
            print('二分法查找：找到了！'+str(key))
            break
        elif li[mid] > key:
            i = mid + 1
        else:
            j = mid - 1

search_two(li,3)

def select_sort(li):
    '''
    1.选择排序：第一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，
    然后再从剩余的未排序元素中寻找到最小（大）元素，然后放到已排序的序列的末尾。
    以此类推，直到全部待排序的数据元素的个数为零。
    '''

    for i in range(len(li)):
        min = i
        for j in range(i+1, len(li)):
            if li[min] > li[j]:
                min = j
        li[i], li[min] = li[min], li[i]
    print('选择排序:' + str(li))
select_sort(li)


def bubble_sort(li):
    '''
    2.冒泡排序：依次比较相邻两个元素大小，交换两元素位置使之满足递增或递减关系，
    完成一次从序列头到序列尾部的过程称为一次冒泡，一次冒泡会产生最大或最小值于队列尾部，
    下一次冒泡序列长度减1，序列尾部的有序序列长度加1
    '''

    for i in range(len(li)-1):
        for j in range(len(li)-1-i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    print('冒泡排序:' + str(li))
bubble_sort(li)


def insert_sort(li):
    '''
    3.插入排序：类似于打扑克，取出未排序的一张牌插入到已排序的牌中，取出的一张牌是在已排序好的牌中从后向前查找，
    直到查找到比当前牌小的那个位置，然后插入进去
    '''

    for i in range(len(li)):
        pre = i-1
        now = li[i]
        while pre >= 0 and li[pre] > now:
            li[pre+1] = li[pre]
            pre -= 1
        li[pre+1] = now
    print('插入排序:' + str(li))
insert_sort(li)


def quicker_sort( li ):
    '''
    4.快速排序:通过一趟排序将要排序的数据分割成独立的两部分，
    其中一部分的所有数据都比另外一部分的所有数据都要小，
    然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，
    以此达到整个数据变成有序序列
    '''

    if len(li) <= 1:
        return li
    pivot = li[len(li)//2]
    left = [x for x in li if x < pivot]
    right = [x for x in li if x > pivot]
    mid = [x for x in li if x == pivot]
    return quicker_sort(left) + mid + quicker_sort(right)
print('快速排序:'+ str(quicker_sort(li)))


import sys
sys.setrecursionlimit(10000)
# 因为递归次数超过了python规定的最大递归次数999
def merge_sort( li ):
    '''
    5.归并排序：将序列通过递归二分拆分到不可分，不可分的序列可以认为是有序序列，
    然后将两个有序序列合并为一个有序序列，直到整个序列变为一个有序序列
    '''

    #递归到只有一个元素就返回
    if len(li) == 1:
        return li
    mid = li[len(li)//2]
    left = li[:mid]
    right = li[mid:]
    #一直拆分
    le = merge_sort(left)
    ri = merge_sort(right)
    return merge(li, ri)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            #加上删掉pop的最小一个
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    #最后有单独的剩余加上来
    result += left
    result += right
    return result
# print(merge_sort(li))

def shell_sort(items):

    '''
    希尔排序:把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
    随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止
    '''

    lenth = len(items)
    mid = lenth // 2
    while mid > 0:
        for i in range(mid, lenth):
            item = i
            while item >= mid and items[item-mid] > items[item]:
                items[item - mid], items[item] = items[item], items[item-mid]
                item -= mid
        mid = mid // 2
    return items
print('希尔排序:'+ str(shell_sort(li)))