def minimiseMaxDistance(arr: [int], k: int) -> float:
    low = 0
    high = 0
    for i in range(1,len(arr)):
        high = max(high, arr[i] - arr[i-1])

    
    diff = pow(10, -6)
    while high - low>diff:
        mid = (low+high)/2.0
        numGasStations = getNumGasStations(arr, mid)

        if numGasStations>k:
            low = mid
        else:
            high = mid

    return high

def getNumGasStations(arr, dist):
    count = 0
    epsilon = 1e-9  # A very small value to account for floating-point precision
    for i in range(1, len(arr)):
        numInBetween = ((arr[i] - arr[i-1]) / dist)
        if abs(numInBetween - int(numInBetween)) > epsilon:
            numInBetween = int(numInBetween)  # Round down if not very close to an integer
        else:
            numInBetween = int(numInBetween) - 1  # Round down if very close to an integer
        count += numInBetween
    return count








import heapq
def minimiseMaxDistance(arr: [int], k: int) -> float:

    # O(k * log(n))
    numInBetween = [0 for _ in range(len(arr)-1)]
    heap = []

    for i in range(1,len(arr)):
        dist = arr[i] - arr[i-1]
        heapq.heappush(heap,(-dist,i))

    for _ in range(k):
        maxDistTillNow,  maxIdx= heapq.heappop(heap)
        numInBetween[maxIdx-1] += 1
        maxDistTillNow = -(arr[maxIdx] - arr[maxIdx-1])
        heapq.heappush(heap, (maxDistTillNow/(numInBetween[maxIdx-1]+1),maxIdx))

        # O(k * n)
        # for i in range(1, len(arr)):
        #     distTillNow = (arr[i] - arr[i-1])/(numInBetween[i-1]+1)
        #     if distTillNow>maxDistTillNow:
        #         maxDistTillNow = distTillNow
        #         maxIdx = i-1
        # numInBetween[maxIdx] += 1 
    
    maxi = -1
    for i in range(len(numInBetween)):
        currLen = (arr[i+1] - arr[i])/(numInBetween[i]+1)
        maxi = max(maxi, currLen)
    return maxi

    return heap[0]

print(minimiseMaxDistance([1,13,17,23],5))
print(minimiseMaxDistance([1,2,3,4,5,6],6))

'''
Problem : https://www.codingninjas.com/studio/problems/minimise-max-distance_7541449

'''

