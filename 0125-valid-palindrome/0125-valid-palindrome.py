import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        alphanum = re.sub(r'[^a-z0-9]','', s.lower())

        return True if alphanum==alphanum[::-1] else False