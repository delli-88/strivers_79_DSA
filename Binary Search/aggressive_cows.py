def aggressiveCows(stalls, k):
    stalls.sort()

    start = stalls[1] - stalls[0]
    end = stalls[-1] - stalls[0]

    maxi = 0

    while start<=end:
        mid = (start+end)//2
        isPossible = checkDist(stalls, mid, k)
        if isPossible:
            maxi = max(maxi, mid)
            start = mid+1
        else:
            end = mid-1
    return maxi # or we can also return end

def checkDist(stalls, dist, k):

    cowsPlaced = 1
    reqDist = stalls[0] + dist

    for i in range(1,len(stalls)):
        if stalls[i]>=reqDist:
            cowsPlaced+=1
            reqDist = stalls[i] + dist
        
        if cowsPlaced>=k:
            break
    
    if cowsPlaced==k:
        return True
    else:
        return False
    
print(aggressiveCows([0, 3, 4, 7, 10, 9],4))

'''
Problem : https://www.codingninjas.com/studio/problems/aggressive-cows_1082559
TC : O(n log n) + O(n log(max-min))
SC : O(1)
Approach :

1. Start by sorting the `stalls` array in ascending order. Sorting is essential for binary search.

2. Initialize two pointers, `start` and `end`, to represent the search range for the minimum distance. Set `start` to the difference between the first and second stall positions (`stalls[1] - stalls[0]`) and set `end` to the difference between the last and first stall positions (`stalls[-1] - stalls[0]`).

3. Initialize a variable `maxi` to 0. This variable will store the maximum minimum distance found during the search.

4. Use a `while` loop to perform binary search within the search range:
   - Calculate the middle value `mid` as `(start + end) // 2`.

   - Check if it's possible to place `k` cows with a minimum distance of `mid` using the `checkDist` function.

   - If it's possible (`isPossible` is `True`), update `maxi` to the maximum of its current value and `mid` and move the search range to the right by setting `start` to `mid + 1`.

   - If it's not possible (`isPossible` is `False`), move the search range to the left by setting `end` to `mid - 1`.

5. After the `while` loop completes, return the value of `maxi`. This represents the maximum minimum distance that allows placing `k` cows in the stalls.

The `checkDist` function checks if it's possible to place `k` cows with a minimum distance of `dist` between them in the stalls. It iterates through the sorted stalls and tracks the number of cows placed, ensuring that the distance between any two consecutive cows is at least `dist`. If `k` cows are successfully placed, it returns `True`; otherwise, it returns `False`.
'''