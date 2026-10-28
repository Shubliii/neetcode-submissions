
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        stack = []
        nums.sort()
        n = len(nums)

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            b = i + 1

            while b < n - 2:
                if b > i + 1 and nums[b] == nums[b - 1]:
                    b += 1
                    continue

                l, r = b + 1, n - 1

                while l < r:
                    Fsum = a + nums[b] + nums[l] + nums[r]

                    if Fsum > target:
                        r -= 1
                    elif Fsum < target:
                        l += 1
                    else:
                        stack.append([a, nums[b], nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

                b += 1

        return stack
