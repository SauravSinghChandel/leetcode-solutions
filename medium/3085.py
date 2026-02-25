class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:

        freq_list = Counter(word).values()

        res = inf

        for freq in freq_list:
            deletions = 0

            for temp_freq in freq_list:
                deletions += temp_freq if temp_freq < freq else max(0, temp_freq - (freq + k))
            
            res = min(deletions, res)

        return res

        # freq_list = sorted(Counter(word).values())

        # def window(max_del):
        #     for i in range(len(freq_list)):
        #         min_freq = freq_list[i]
        #         max_freq = min_freq + k
        #         deletions = 0

        #         for freq in freq_list:

        #             if freq < min_freq:
        #                 deletions += freq
                    
        #             elif freq > max_freq:
        #                 deletions += freq - max_freq

        #         if deletions <= max_del:
        #             return True

        #     return False

        # left, right = 0, len(word)
        # answer = right
        # while left <= right:
        #     mid = (right + left) // 2

        #     if window(mid):
        #         answer = mid
        #         right = mid - 1

        #     else:
        #         left = mid + 1

        # return answer
