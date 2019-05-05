class Solution:
    def numSubarrayBoundedMax(self, A: list, L: int, R: int) -> int:
        if not A or 0 == len(A):
            return 0

        left_arr_length = 0
        left_in_range_number = 0
        left_in_range_number_sub_count = 0
        result = 0

        for number in A:
            if number > R:
                left_in_range_number = 0
                left_arr_length = 0
                left_in_range_number_sub_count = 0
            else:
                left_arr_length += 1
                # in_range
                if L <= number <= R:
                    left_in_range_number = left_in_range_number + 1
                    left_in_range_number_sub_count = left_arr_length
                    result = result + left_arr_length
                else:
                    result = result + left_in_range_number_sub_count

        return result


solution = Solution()
print(solution.numSubarrayBoundedMax([2, 1, 4, 3], 2, 3))
print(solution.numSubarrayBoundedMax([73, 55, 36, 5, 55, 14, 9, 7, 72, 52], 32, 69))
