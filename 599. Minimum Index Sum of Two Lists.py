# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

# I
# class Solution:
    # def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
    #     hm = {}
    #     for i in range(len(list1)):
    #         hm[list1[i]] = [i]
        
    #     for i in range(len(list2)):
    #         if list2[i] in hm:
    #             hm[list2[i]].append(i)

    #     smallest = len(list1) + len(list2) - 2
    #     res = []

    #     for k, v in hm.items():
    #         if len(v) != 2:
    #             continue
    #         sum_ids = sum(v)
    #         if smallest == sum_ids:
    #             res.append(k)
    #         elif sum_ids < smallest:
    #             smallest = sum_ids
    #             res = [k]

    #     return res

# II
class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        hm = {}
        for i in range(len(list1)):
            hm[list1[i]] = i
        
        smallest = len(list1) + len(list2) - 2
        res = []
        
        for i in range(len(list2)):
            if list2[i] in hm:
                # hm[list2[i]].append(i)
                if hm[list2[i]] + i == smallest:
                    res.append(list2[i])
                if hm[list2[i]] + i < smallest:
                    smallest = hm[list2[i]] + i
                    res = [list2[i]]

        return res


sln = Solution()

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
assert (res := sln.findRestaurant(list1, list2)) == ['Shogun'], res

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]
assert (res := sln.findRestaurant(list1, list2)) == ['Shogun'], res

list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]
assert (res := sln.findRestaurant(list1, list2)) in (['sad', 'happy'], ['happy', 'sad']), res

print('ok')
