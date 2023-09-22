import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None or len(s) == 1:
            return True
        lower_s = s.lower()
        alpanum = re.sub(r'[^a-z0-9]','', lower_s)
        
        for i in range(int(len(alpanum)/2)):
            if alpanum[i] != alpanum[-i-1]:
                return False

        return True