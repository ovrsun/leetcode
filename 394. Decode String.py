class Solution:
    def decodeString(self, s):
        stack = []
        curr_num = 0
        curr_str = ''

        for c in s:
            if c == '[':
                stack.append(curr_str)
                stack.append(curr_num)
                curr_str = ''
                curr_num = 0
            elif c == ']':
                num = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + num*curr_str
            elif c.isdigit():
                curr_num = curr_num*10 + int(c)
            else:
                curr_str += c
        return curr_str


sln = Solution()
assert (res := sln.decodeString("3[a]2[bc]")) == 'aaabcbc', res
assert (res := sln.decodeString("3[a2[c]]")) == 'accaccacc', res
# assert (res := sln.decodeString("2[abc]3[cd]ef")) == 'abcabccdcdcdef', res
# assert (res := sln.decodeString("abc3[cd]xyz")) == "abccdcdcdxyz", res
assert (res := sln.decodeString("3[a]2[2[b]cd4[2[ef]g1[h]]]jk")) == "aaabbcdefefghefefghefefghefefghbbcdefefghefefghefefghefefghjk", res
# assert (res := sln.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")) == "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef", res
# 3[z] 2 [2[y] pq 4[ 2[jk] e 1[f] ] ]ef
# zzz yy pq jkjk ef jkjk ef jkjk ef jkjk ef yypqjkjkefjkjkefjkjkefjkjkef ef

