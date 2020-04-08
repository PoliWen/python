'''
@Author: kingw
@Date: 2020-03-09 15:11:55
@Description: file content
'''
#这里面写关于数据的各种查找方法
#写一个二分查找，这真的是一个很简单的算法呀，大哥
def binarysearch(arr,l,r,x):
    if r>=1:
        mid = int(l + (r - l)/2) #关键问题在这里，中间位置的计算
        print('mid',mid,arr[mid])
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binarysearch(arr,mid+1,r,x)
        else:
            return binarysearch(arr,l,mid-1,x)
    else:
        return -1
arr = [ 2, 3, 4, 10, 40 ]
print('arr',arr,len(arr)-1)
n = binarysearch(arr,0,len(arr)-1,10)
print(n)
#这是一个二分查找法
#普通线性查找,这种方法是最慢的查找方式，比二分查找慢了一个指数倍,时间复杂度是O(1)
def search(arr,x):
    for i in range(0,len(arr)):
        if arr[i]==x:
            return i
    return -1
m = search(arr,10)
print(m)
#插入排序，https://www.runoob.com/python3/python-insertion-sort.html
#选择排序 https://www.runoob.com/python3/python-selection-sort.html
def selectsort(arr):
    for i in range(0,len(arr)):
        min_i = i
        for j in range(i+1,len(arr)):
            if arr[min_i]>arr[j]:
                min_i = j
        arr[i],arr[min_i] = arr[min_i],arr[i]
    return arr
arr2 = selectsort(arr)
print(arr2)


