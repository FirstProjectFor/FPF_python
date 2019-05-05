class Solution:
    def numSubarrayBoundedMax(self, A: list, L: int, R: int) -> int:
        if not A or 0 == len(A):
            return 0

        start = 0
        pre_in_range_number_index = -1
        result = 0

        for index in range(len(A)):
            if A[index] > R:
                start = -1
                pre_in_range_number_index = -1
            else:
                if start < 0:
                    start = index

                if L <= A[index]:
                    pre_in_range_number_index = index
                    result = result + index - start + 1
                elif pre_in_range_number_index >= 0:
                    result = result + pre_in_range_number_index - start + 1

        return result


solution = Solution()
print(solution.numSubarrayBoundedMax([2, 1, 4, 3], 2, 3))
print(solution.numSubarrayBoundedMax([73, 55, 36, 5, 55, 14, 9, 7, 72, 52], 32, 69))
