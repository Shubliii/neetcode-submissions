class Solution:
    def isPalindrome(self, s: str) -> bool:


        newstr=""


        for c in s:
            if c.isalnum(): #character alpha numeric hai ki nhi check karooo
                newstr+=c.lower()

        return newstr==newstr[::-1]        


    
                



        
        