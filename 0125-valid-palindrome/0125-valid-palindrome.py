import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None or len(s) == 1:
            return True
        alphanum = re.sub(r'[^a-z0-9]','', s.lower())

        return True if alphanum==alphanum[::-1] else False