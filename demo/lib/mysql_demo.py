import pymysql

connect = pymysql.connect(host='10.0.8.36', user='root', password='tuhOSw2Cdg)W', database='cashloan_hades',
                          charset='utf8')
cursor = connect.cursor()
query = ('SELECT id, name FROM arc_sys_menu')
cursor.execute(query)

for id, name in cursor:
    print(id)
    print(name)
