class Algorithm:
    def findLHS(self, nums: list()) -> int:
        if not nums:
            return 0

        number_count_dict = {}

        for value in nums:
            if value in number_count_dict:
                number_count_dict[value] = number_count_dict[value] + 1
            else:
                number_count_dict[value] = 1

        result = 0

        for k, v in number_count_dict.items():
            if k + 1 in number_count_dict:
                result = max(result, v + number_count_dict[k + 1])

        return result

    @staticmethod
    def __get_value(num_count_dict, key) -> int:
        if key not in num_count_dict:
            return 0
        return num_count_dict[key]
