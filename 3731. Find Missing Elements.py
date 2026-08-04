class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        low = min(nums)
        high = max(nums)

        s = set(nums)
        out = []

        for i in range(low, high + 1):
            if i not in s:
                out.append(i)

        return out