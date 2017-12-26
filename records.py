from TimeRecord import TimeRecord

records = list()
records.append(TimeRecord.read_data(name="XiaoTian"))
records.append(TimeRecord.read_data(name="XiaoSun"))

for record in records:
    print("姓名 : " + record.name)
    print("日期 : " + record.data)
    print("最好的5个成绩", record.top_five())
