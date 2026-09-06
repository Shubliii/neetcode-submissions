class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for asteroid in asteroids:

            destroyed = False

            while stack and stack[-1] > 0 and asteroid < 0:

                if stack[-1] < -asteroid:
                    stack.pop()
                    continue

                if stack[-1] == -asteroid:
                    stack.pop()
                    destroyed = True
                    break

                if stack[-1] > -asteroid:
                    destroyed = True
                    break

            if not destroyed:
                stack.append(asteroid)

        return stack
    
