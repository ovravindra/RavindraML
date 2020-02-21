# writing code to sort the given vector(one dimensional) in an ascending order
# the following sort is called selection sort.
# Assumptions: 1. the matrix is a 1-D vector. 2. there are no repetitions of the elements

def selectsort(A):
    n = len(A)
    for i in range (1,n):
        a = A[i]
        for j in range ((i+1),(n)):
            [b,x] = mini(A[j:n])
            if a > b:
                mat2 = swap(i,j,A)
    print(mat2)



def position(a,A):  # extra function not used in the code: return the position of an element in an array
    n = len(A)
    if a in A:
        for i in range (1,n):
            if a == A[i]:
                # x.append(i) is used in case of repetitions of elements in the matrix
                x = i
                break
        return x
    # else print("the element is not present in the vector")



def mini(A):  # return the minimum element of an array(y) and its position(x)
    n = len(A)

    y = A[1]
    i = 1
    for j in range ((i+1),n):
        if A[j] < y:
            x = A[j]
            i = j
            break
        else:
            print("the matrix has all same elements")
    return [x, i]



def swap(i,j,A):  # swap positions between two elements of an array and return the matrix
    emp = A[i]
    A[i] = A[j]
    A[j] = emp
    return A

mtx = [3,2,7,6,8,87,43,1,235,12,564,56] # a random vactor defined.
print(selectsort(mtx))