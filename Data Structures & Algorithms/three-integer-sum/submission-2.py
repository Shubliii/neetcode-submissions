
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):

            # a mein duplicate check: agar current a, previous a ke equal hai,
            # toh skip karo taaki same triplets dobara na banein
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1

                elif threeSum < 0:
                    l += 1

                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # l mein duplicate check: previous l ki value same hai,
                    # toh skip karo taaki same triplet repeat na ho
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res
