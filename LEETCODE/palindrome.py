class Solution(object):
    def isPalindrome(self, x):
      pal = list(reversed((str(x))))
      if pal == list(str(x)):
        return True
      else:
        return False
      
      
s1 = Solution()
print(s1.isPalindrome(121))