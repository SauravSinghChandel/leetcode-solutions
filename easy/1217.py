class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        
        even_sum, odd_sum, even_max, odd_max = 0, 0, 0, 0

        for i, n in enumerate(position):
            if n % 2 == 0:
                even_sum += 1
                #even_max = max(even_max, n)
            
            else:
                odd_sum += 1
                #odd_max = max(odd_max, n)
        
        if even_sum > odd_sum:
            return odd_sum

        else:
            return even_sum
