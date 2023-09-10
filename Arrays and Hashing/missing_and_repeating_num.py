def findMissingRepeatingNumbers(a: [int]) -> [int]:
    n = len(a)
    xor_arr = 0
    xor_n = 0
    for i in range(1,n+1):
        xor_n = xor_n^i
    
    for i in range(n):
        xor_arr = xor_arr^a[i]
    
    xor_arr_n = xor_arr^xor_n

    first_diff_bit = 1
    while first_diff_bit<=xor_arr_n:
        if first_diff_bit&xor_arr_n > 0:
            break
        first_diff_bit = first_diff_bit<<1

    # divide the array and first n elements into two sets
    xor_set_zero = 0
    xor_set_one = 0

    # for first n
    for i in range(1,n+1):
        if i&first_diff_bit>0:
            xor_set_one = xor_set_one^i
        else:
            xor_set_zero = xor_set_zero^i
    
    # for arr elems

    for i in range(n):
        if a[i]&first_diff_bit>0:
            xor_set_one = xor_set_one^a[i]
        else:
            xor_set_zero = xor_set_zero^a[i]
    
    missing = None
    repeated = None

    for i in range(n):
        if a[i]==xor_set_zero or a[i]==xor_set_one:
            repeated = a[i]
            break
    
    if repeated==xor_set_zero:
        missing = xor_set_one
    else:
        missing = xor_set_zero

    return [repeated, missing]


print(findMissingRepeatingNumbers([4,3,6,2,1,1]))

'''
Problem : https://www.codingninjas.com/studio/problems/missing-and-repeating-numbers_6828164
TC : O(n)
SC : O(1)
Approach :

1. Calculate the XOR (`xor_n`) of all numbers from 1 to `n` (where `n` is the length of the input array `a`) using a loop.

2. Calculate the XOR (`xor_arr`) of all elements in the input array `a`.

3. Calculate `xor_arr_n` by XORing `xor_arr` and `xor_n`. This will give you the XOR of the missing and repeating numbers.

4. Find the rightmost bit where `xor_arr_n` is 1. This bit position represents the first difference between the missing and repeating numbers.

5. Divide the elements from 1 to `n` and the elements in the array `a` into two sets based on whether the corresponding bit is 0 or 1.

6. Calculate the XOR of each set separately:
   - `xor_set_zero` for elements with a 0 at the differing bit position.
   - `xor_set_one` for elements with a 1 at the differing bit position.

7. Iterate through the elements in the array `a` and identify the element that matches either `xor_set_zero` or `xor_set_one`. This element is the repeating number.

8. Determine the missing number based on which of `xor_set_zero` or `xor_set_one` does not match the repeating number.

9. Return a list containing the repeating and missing numbers.
'''