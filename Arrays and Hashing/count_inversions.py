from typing import *

def numberOfInversions(a : List[int], n : int) -> int:
    count = [0]
    copyArr = a[:]
    modifiedMergeSort(copyArr, 0, len(a)-1, count)
    return count[0]

def modifiedMergeSort(arr, start, end, count):
    if start==end:
        return
    
    mid = (start + end)//2
    modifiedMergeSort(arr, start, mid, count)
    modifiedMergeSort(arr, mid+1, end, count)

    left = [i for i in arr[start:mid+1]]
    right = [i for i in arr[mid+1:end+1]]

    i,j,k = 0,0,start

    while i<len(left) and j<len(right) and k<len(arr):
        if left[i]>right[j]:
            count[0]+= len(left)-i
            arr[k] = right[j]
            j+=1
        else:
            arr[k] = left[i]
            i+=1
        k+=1
    
    while i<len(left):
        arr[k] = left[i]
        i+=1
        k+=1
    
    while j<len(right):
        arr[k] = right[j]
        j+=1
        k+=1
    
    return

print(numberOfInversions([5,3,2,1,4],5))

'''
Problem : https://www.codingninjas.com/studio/problems/number-of-inversions_6840276
TC : O(n log n)
SC : O(n)
Approach :

1. Initialize a variable `count` to keep track of the number of inversions (initialized as 0).

2. Create a copy of the input array `a` called `copyArr` to avoid modifying the original array.

3. Define a `modifiedMergeSort` function that takes the `arr`, `start`, `end`, and `count` as parameters:

   - In the `modifiedMergeSort` function:
     - If `start` equals `end`, return, as it represents the base case of a single element.

     - Calculate the midpoint `mid` as `(start + end) // 2`.

     - Recursively call `modifiedMergeSort` on the left half of `arr` from `start` to `mid`.
     
     - Recursively call `modifiedMergeSort` on the right half of `arr` from `mid+1` to `end`.

     - Create two lists, `left` and `right`, by splitting `arr` into these two halves.

     - Initialize three pointers, `i`, `j`, and `k`, to 0, representing the indices of `left`, `right`, and `arr`, respectively.

     - Merge `left` and `right` back into `arr` while counting inversions:
       - While `i` is less than the length of `left` and `j` is less than the length of `right`:
         - If `left[i]` is greater than `right[j]`, it indicates an inversion. Increment `count` by the number of remaining elements in `left` (i.e., `len(left) - i`) because all elements in `left` after `i` are greater than `right[j]`. Set `arr[k]` to `right[j]`, increment `j`, and increment `k`.
         - Otherwise, set `arr[k]` to `left[i]`, increment `i`, and increment `k`.

       - After the above loop, there might be remaining elements in `left` or `right`. Copy them to `arr`.

   - Return from the `modifiedMergeSort` function.

4. Call `modifiedMergeSort` on `copyArr` with `start` as 0 and `end` as `n-1`, and pass the `count` variable by reference.

5. After the `modifiedMergeSort` function returns, `count` will contain the number of inversions in the array.

6. Return the value of `count` as the result.
'''