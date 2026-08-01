class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x<10 :
             return True
        x_string = list(str(x))
        mid = len(x_string) // 2
        for i in range(mid):
            if x_string[i] != x_string[-i-1]:
                return False
        return True
    
    
    
    class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x<10 :
             return True
        x_string = list(str(x))
        mid = len(x_string) // 2
        
        
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return x >= 0 and str(x) == str(x)[::-1]
    
    
    
class Solution:
    def isPalindrome(self, x: int) -> bool:

        s = str(x)

        return s == s[::-1]