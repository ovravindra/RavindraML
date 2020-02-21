"""
comparing two adjcent elements in the matrix and swapping them.
iterating throught the set with each iteration few elements sorted.
"""

def bubbleSort(A):
    n = len(A)
    for j in range (1,n):
        for i in range (0,(n-j)):
            if A[i] > A[i+1]:
                swap(i,(i+1),A)
    return A


def swap(i,j,A):  # swap positions between two elements of an array and return the matrix
    emp = A[i]
    A[i] = A[j]
    A[j] = emp
    return A


mtx = [3,2,7,6,8,87,43,564,1,235,12,56] # a random vactor defined.
print(mtx[0])
print(bubbleSort(mtx))
