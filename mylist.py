class MyList(list):
    """
    继承自 list
    """

    def __init__(self, list_name):
        list.__init__([])
        self.list_name = list_name

    def get_name(self):
        return self.list_name


m_list = MyList(list_name="MyList")
m_list.append("1")
m_list.append("23")

print(m_list)
# 查看对象类型
print(type(m_list))
# 查看对象的方法
print(dir(m_list))
