class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remvoe non-alphanumeric characters in the string
        cleaned_s = "".join(c for c in s if c.isalnum())
        print(cleaned_s)
        l = 0
        r = len(cleaned_s) - 1

        while r >= 0:
            if cleaned_s[l].lower() != cleaned_s[r].lower():
                # print('l:', cleaned_s[l].lower(), 'r: ', cleaned_s[r].lower(), sep='\n')
                return False
            r -= 1
            l += 1
            
        return True