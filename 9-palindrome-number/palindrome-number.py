class Solution:
    def isPalindrome(self, x):
        
        original = x
        reverse = 0

        while x > 0:
            r = x % 10
            reverse = reverse * 10 + r
            x //= 10

        if reverse == original:
            return True
        else:
            return False
        