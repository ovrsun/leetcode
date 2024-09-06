# https://leetcode.com/problems/valid-anagram/

def is_anagram(s, t):
    if len(s) != len(t) or set(s) != set(t):
        return False
    s_hm, t_hm = {}, {}

    for c in s:
        s_hm[c] = s_hm.setdefault(c, 0) + 1
    
    for c in t:
        t_hm[c] = t_hm.setdefault(c, 0) + 1

    return s_hm == t_hm


assert is_anagram('', '') is True
assert is_anagram('a', 'b') is False
assert is_anagram('abc', 'bca') is True
assert is_anagram('qwerty', 'qqwerty') is False
assert is_anagram('qweerty', 'qqwerty') is False
