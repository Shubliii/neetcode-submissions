class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        stack = []

        for i in range(n-k, n):
            stack.append(nums[i])

        for i in range(n-k):
            stack.append(nums[i])

        for i in range(n):
            nums[i] = stack[i]