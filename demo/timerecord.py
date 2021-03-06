class TimeRecord:
    def __init__(self, name: str, data, records: list = list()):
        self.name = name
        self.data = data
        self.records = records

    def get_name(self):
        return self.name

    def get_date(self):
        return self.data

    def get_records(self):
        return self.records

    def top_five(self):
        return sorted(set([float(self.translate_time(r)) for r in self.records]))[0:5]

    def add_record(self, record: str):
        self.records.append(record)

    def add_records(self, records):
        self.records.extend(records)

    @staticmethod
    def read_data(name):
        data = [name, "2017-12-26", "2:33", "3:44", "3-44", "20-33", "9:21", "10:23", "4:21", "3:23", "8-44", "455"]
        return TimeRecord(data.pop(0), data.pop(0), data)

    @staticmethod
    def translate_time(time_str: str) -> str:
        if isinstance(time_str, float):
            return str(time_str)
        if ":" in time_str:
            splitter = ":"
        elif "-" in time_str:
            splitter = "-"
        else:
            return time_str
        (minute, seconds) = time_str.split(splitter)
        return minute + "." + seconds
