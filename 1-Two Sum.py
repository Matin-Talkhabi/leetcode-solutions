class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in range(len(nums)):
            complement = target -nums[i]
            if complement in nums[i+1:]:
                answer=[nums[i], complement]
                return answer
            
            


----------------------------


        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []