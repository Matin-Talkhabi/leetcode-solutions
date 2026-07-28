### 628. Maximum Product of Three Numbers

from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(
            nums[-1] * nums[-2] * nums[-3],  # سه عدد بزرگ
            nums[0] * nums[1] * nums[-1]     # دو عدد منفی و بزرگ‌ترین عدد
        )

sol = Solution()
result = sol.maximumProduct([-10, -3, 5, 6])
print(result)
