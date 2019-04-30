import shutil

GB = 2 ** 30

total, used, free = shutil.disk_usage("c:")

print("total: {:6.2f} GB, used: {:6.2f} GB, free: {:6.2f} GB".format(total / GB, used / GB, free / GB))