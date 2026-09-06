class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:


        # Asteroid Collision Logic:
# Use a stack. Collision happens only when stack[-1] > 0 and asteroid < 0 (→ ←).
# Compare sizes:
# 1. stack[-1] < -asteroid → stack asteroid destroyed → pop and continue checking.
# 2. stack[-1] == -asteroid → both destroyed → pop and stop.
# 3. stack[-1] > -asteroid → current asteroid destroyed → stop.
# Add the current asteroid to stack only if it was NOT destroyed.

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
    
