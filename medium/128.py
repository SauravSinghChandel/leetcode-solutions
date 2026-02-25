class Solution:
    def longestConsecutive(self, nums):
        s = set()
        for i in nums:
            s.add(i)
        lon = 0
        
        for n in s:
            # check if its the start of a sequence
            if (n - 1) not in s:
                l = 1
                while (n + l) in s:
                    l += 1
                lon = max(l, lon)
        return lon
    
    
# class Solution(object):
#     def longestConsecutive(self, nums):

#         s = set()
#         for n in nums:
#             s.add(n)
        
#         longest = 0
#         for x in s:
#             if x-1 not in s:
#                 curr = 1
#                 while x+1 in s:
#                     x += 1
#                     curr += 1
                
#                 longest = max(curr, longest)
        
#         return longest
