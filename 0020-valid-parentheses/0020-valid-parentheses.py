class Solution:
    def isValid(self, s: str) -> bool:
        str_hash = {')': '(', '}': '{', ']': '['}
        s_list = list(s)

        s_stack = []
        if (len(s_list)%2 == 0 and s_list[0] not in str_hash):
            for i in range(len(s_list)):
                if (s_list[i] == '(' or s_list[i] == '{' or s_list[i] == '['):
                    s_stack.append(s_list[i])
                else:
                    sli = s_list[i]
                    s_stack_last = ''
                    if s_stack: s_stack_last = s_stack[-1]
                    if (s_stack_last == str_hash[sli]):
                        s_stack.pop()
                    else:
                        return False
            if s_stack:
                return False
            else:
                return True
        else:
            return False
            