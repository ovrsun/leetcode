# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        # ({[  ||||  ]})
        # ()()()
        # ((((({})
        # ((((
        # (()))()
        # (((((
        if len(s) % 2 != 0:
            return False
        
        stack = []
        for bracket in s:
            if bracket in '({[':
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                if [stack[-1], bracket] in [['(', ')'], ['{', '}'], ['[', ']']]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
