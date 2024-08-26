# https://leetcode.com/problems/group-anagrams/

def group_anagrams(words):
    hm = {}
    for word in words:
        code = [0] * 26
        for c in word:
            code[ord(c) - ord('a')] += 1
        hm.setdefault(tuple(code), []).append(word)

    return list(hm.values())


assert (res := sorted(group_anagrams(["eat","tea","tan","ate","nat","bat"]), key=len)) == [["bat"],["nat","tan"],["ate","eat","tea"]], res
# assert group_anagrams(["a"]) == [["a"]]
# assert group_anagrams([""]) == [[""]]
# assert with different lenghts