class Solution:
    def validPalindrome(self, s: str) -> bool:


        # LOGIC:
        # 1. Use two pointers: l → left, r → right.
        # 2. If s[l] == s[r], move both pointers inward.
        # 3. At the FIRST mismatch, we can delete only ONE character.
        # 4. Try deleting left OR right character.
        # 5. If either remaining part is a palindrome → True.
        # 6. If no mismatch occurs → already a palindrome → True.

        # Helper function to check if substring is palindrome
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                # Skip either left or right character once
                return isPalindrome(l + 1, r) or isPalindrome(l, r - 1)

            l += 1
            r -= 1

        return True

        
        