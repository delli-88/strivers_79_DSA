from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break  # The current asteroid is destroyed

            else:
                stack.append(asteroid)

        return stack

print(Solution().asteroidCollision(asteroids = [-1,7, 3, 6, -7, 2, -11]))

'''
Problem : https://leetcode.com/problems/asteroid-collision/
TC : O(n)
SC : O(n)
Approach : 

1. Initialize an empty stack to keep track of the asteroids that haven't collided.

2. Iterate through each asteroid in the given list:
   - If the stack is empty or the current asteroid is moving to the right (positive), simply append it to the stack.
   - If the current asteroid is moving to the left (negative) and there are positive asteroids on the stack, handle the collision:
     - While the top of the stack is positive and greater in magnitude than the current asteroid, pop elements from the stack until there's a smaller positive asteroid or an empty stack.
     - If the top of the stack has the same magnitude as the current asteroid, pop it and continue to the next asteroid.
     - If the stack is empty or the top of the stack is negative, append the current asteroid to the stack.

3. After processing all asteroids, the stack will contain the surviving asteroids that haven't collided. Return the stack as the result.
'''
