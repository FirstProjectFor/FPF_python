class Solution:
    def numSubarrayBoundedMax(self, A: list, L: int, R: int) -> int:
        if not A or 0 == len(A):
            return 0

        length = 0
        pre_in_range_number_length = 0
        result = 0
        for value in A:
            if value > R:
                length = 0
                pre_in_range_number_length = 0
            elif L <= value:
                length = length + 1
                pre_in_range_number_length = length
                result = result + length
            else:
                length = length + 1
                result = result + pre_in_range_number_length

        return result


solution = Solution()
print(solution.numSubarrayBoundedMax([2, 1, 4, 3], 2, 3))
print(solution.numSubarrayBoundedMax([73, 55, 36, 5, 55, 14, 9, 7, 72, 52], 32, 69))
