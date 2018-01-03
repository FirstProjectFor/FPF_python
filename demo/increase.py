from util import printutil

money = 10000 * 10
everyday_increase = (0.04 / 365)
printutil.print_key_value("本金是: ", str(money))
printutil.print_key_value("每日收益是", everyday_increase)
print("------------------------- ge -------------------------")

year = 0
times = 1

start = 1
end = 1

temp_money = money

for day in range(365 * 100):
    real_times = (temp_money - money) / money
    if real_times >= times:
        need_year = day / 365
        printutil.print_key_value("第" + str(day) + "天", "收益是本金的 " + str(int(real_times)) + " 倍")
        print("从开始投资，大约经历了: " + str(int(need_year)) + " 年")
        print("距离上一次翻倍花费时间: " + str(end - start) + " 天，大约 " + str(int((end - start) / 365)) + " 年")
        printutil.print_key_value("收益是", str(int(temp_money - money)))
        print("------------------------- ge -------------------------")
        start = end
        while times < real_times:
            times = times + 1

    end = end + 1
    temp_money = temp_money * (1 + everyday_increase)
