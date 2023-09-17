class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        
        for i in range(max(len(s), len(t))):
            if (i<len(s)):
                if (s[i] == '#'):
                    if stack_s != []:
                        stack_s.pop()
                else:
                    stack_s.append(s[i])
            if (i<len(t)):
                if (t[i] == '#'):
                    if stack_t != []:
                        stack_t.pop()
                else:
                    stack_t.append(t[i])
        return stack_s == stack_t