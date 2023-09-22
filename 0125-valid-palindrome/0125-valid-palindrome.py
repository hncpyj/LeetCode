import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None or len(s) == 1:
            return True
        lower_s = s.lower()
        alphanum = re.sub(r'[^a-z0-9]','', lower_s)

        return True if alphanum==alphanum[::-1] else False