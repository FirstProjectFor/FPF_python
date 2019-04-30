import glob

for file in glob.glob("d://*//*//*//*//*"):
    print(glob.escape(file))
