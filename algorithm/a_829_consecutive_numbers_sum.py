import math


class A_829:
    def consecutiveNumbersSum(self, N: int) -> int:
        result = 1
        length = 1

        while True:
            length += 1
            start = math.floor(N / length) - math.floor(length / 2)
            end = start + length - 1

            sum1 = A_829.get_sum(start, end)
            while sum1 < N:
                start += 1
                sum1 += length
            if start <= 0:
                break
            if sum1 == N:
                result += 1

        return result

    @staticmethod
    def get_sum(start, end):
        """
        获取序列和
        :param start:int:
        :param end:int
        :return:int
        """
        return math.floor((end - start + 1) * (start + end) / 2)
