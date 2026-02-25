class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        for i in range(n):
            if i - k >= 0 and energy[i - k] >= 0:
                energy[i] += energy[i - k]

        return max(energy[n - k:])
