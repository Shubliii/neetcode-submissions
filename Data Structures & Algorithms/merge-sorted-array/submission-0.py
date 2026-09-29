class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        p1 = 0
        p2 = 0

        OP = []

        # Compare elements while both arrays have elements
        while p1 < m and p2 < n:

            if nums1[p1] < nums2[p2]:
                OP.append(nums1[p1])
                p1 += 1
            else:
                OP.append(nums2[p2])
                p2 += 1

        # Add remaining elements of nums1
        while p1 < m:
            OP.append(nums1[p1])
            p1 += 1

        # Add remaining elements of nums2
        while p2 < n:
            OP.append(nums2[p2])
            p2 += 1

        # Put the result back into nums1
        for i in range(len(OP)):
            nums1[i] = OP[i]


