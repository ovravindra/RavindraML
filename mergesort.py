# mergesort by dividing the array into halves and recursively sorting them out.

def mergesort(A):
    n = len(A)
    if (n % 2) == 0:
        left = A[:n/2] 
        right = A[n/2:]
    else:
        left = A[:(n-1)/2]
        right = A[(n-1)/2:]
    while n > 1:
        mergesort(left)
        mergesort(right)
    mat = merge(left,right,A)
    return mat



def merge(left, right, A):
    n = len(left)
    m = len(right)
    k = 0
    while i < n & j < m:
        if left[i] <= right[j]:
            A[k] = left[i]
            i = i + 1
        elif right[j] < left[i]:
            A[k] = right[i]
            j = j + 1
        k = k + 1
    return A

mtx = [3,2,7,6,8,87,43,1,235,12,564,56] # a random vactor defined.
print(mergesort(mtx))
