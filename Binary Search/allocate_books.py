def findPages(arr: [int], n: int, m: int) -> int:
    if len(arr)<m:
        return -1
    max_pages = max(arr)
    sum_pages = sum(arr)

    start = max_pages
    end = sum_pages

    while start<=end:
        mid = (start+end)//2
        numStudents = allocate(arr, m, mid)
        if numStudents>m:
            start = mid + 1
        else:
            end = mid -1 

    return start

def allocate(arr, students, pages):

    allocatedTo = 1
    currAllocation = arr[0]
    for i in range(1,len(arr)):
        if currAllocation+arr[i]<=pages:
            currAllocation+=arr[i]
        else:
            allocatedTo+=1
            currAllocation=arr[i]
        
        if allocatedTo>students:
            break
    
    return allocatedTo

print(findPages([12,34,67,90],4,2))
# print(findPages([1,2,3,4,5],5,3))

'''
Problem : https://www.codingninjas.com/studio/problems/allocate-books_1090540
TC : O(n log m) where m = sum(arr) - max(arr)
SC : O(1)
Approach : 

1. Check if the length of the `arr` (array of pages in books) is less than `m`. If it is, return -1 because it's impossible to allocate `m` students with fewer books than `m`.

2. Calculate the maximum number of pages in any book (`max_pages`) and the total number of pages in all books (`sum_pages`).

3. Initialize two pointers, `start` and `end`, to represent the search range for the minimum number of pages to allocate. Set `start` to `max_pages` (minimum possible allocation) and `end` to `sum_pages` (maximum possible allocation).

4. Use a `while` loop to perform binary search within the search range:
   - Calculate the middle value `mid` as `(start + end) // 2`.

   - Calculate the number of students required to allocate the books with a minimum allocation of `mid` pages using the `allocate` function.

   - If the number of students required (`numStudents`) is greater than `m`, it means the allocation is not feasible with the current minimum allocation. So, update `start` to `mid + 1` to search for a larger allocation.

   - If the number of students required is less than or equal to `m`, it means the allocation is possible, so update `end` to `mid - 1` to search for a smaller allocation while still keeping it possible.

5. After the `while` loop completes, return the value of `start`. This represents the minimum number of pages that can be allocated to `m` students while maximizing the minimum number of pages allocated.

The `allocate` function calculates the number of students required to allocate `pages` pages optimally. It iterates through the books in `arr` and tracks the current allocation. If the current allocation exceeds `pages`, it allocates the next book to a new student. The function returns the total number of students required for the given allocation.

'''
