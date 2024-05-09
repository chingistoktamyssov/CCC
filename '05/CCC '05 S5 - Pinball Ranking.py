import sys
t = int(sys.stdin.readline())
arr = []
for i in range(t):
    arr.append(int(sys.stdin.readline()))

rank = 0
def mergeSort(arr):
    global rank
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
                rank += (len(left) - i)
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

mergeSort(arr)
print("%.2f" % round(rank/t+1, 2))