import time


class Solution:
    def maxProduct(self, n: int) -> int:
        n_list = [int(x) for x in str(n)]
        max_product = 0
        firts_max = max(n_list)
        n_list.remove(firts_max)
        second_max = max(n_list)
        max_product = firts_max * second_max
        return max_product
time_start = time.time()

sol = Solution()
result = sol.maxProduct(5645654651165456415631685749849879846313249874651231)
time_end = time.time()
print("Time taken: ", time_end - time_start, "seconds")
print(result)