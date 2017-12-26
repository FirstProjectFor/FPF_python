def translate_time(time_str):
    if ":" in time_str:
        splitter = ":"
    elif "-" in time_str:
        splitter = "-"
    else:
        return int(time_str)

    (minute, seconds) = time_str.split(splitter)

    return int(minute) * 100 + int(seconds)


weight_arr = ["2:33", "3:44", "3-44", "20-33", "9:21", "10:23", "4:21", "3:23", "8-44", "455"]

# 推导列表 格式化 -> 去重set -> 排序
weight_format = sorted(set([translate_time(w) for w in weight_arr]))

print(weight_format[0:5])
