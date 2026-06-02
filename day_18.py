#leetcode problem-4 use if class for ispalindrome 
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        
        return s == s[::-1]
        
        
