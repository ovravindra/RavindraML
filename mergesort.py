# mergesort by dividing the array into halves and recursively sorting them out.

def mergesort(A):
    n = len(A)//2
    left = A[:n] 
    right = A[n:]
    while n >= 1:
        mergesort(left)
        mergesort(right)
    mat = merge(left,right)
    return mat



def merge(left, right):
    n = len(left)
    m = len(right)
    A = []
    i = j = 0
    while i < n and j < m:
        if left[i] <= right[j]:
            A.append(left[i])
            i = i + 1
        if right[j] < left[i]:
            A.append(right[i])
            j = j + 1
    return A


mtx = [3,2,7,6,8,87,43,1,235,12,564,56] # a random vactor defined.
print(mergesort(mtx))
