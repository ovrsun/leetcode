# https://leetcode.com/problems/keys-and-rooms/description/

class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set()
        queue = [0]
        
        while queue:
            current = queue.pop(0)
            if current in visited:
                continue
            visited.add(current)
            queue.extend(rooms[current])

        return len(rooms) == len(visited)



sln = Solution()
assert (res := sln.canVisitAllRooms([[1],[2],[3],[]])) is True, res
assert (res := sln.canVisitAllRooms([[1,3],[3,0,1],[2],[0]])) is False, res





# [1], [2], [3], []


# [0, 1, 2, 3]