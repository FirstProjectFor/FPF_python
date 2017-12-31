class MyList(list):
    """
    继承自 list
    """

    def __init__(self, list_name):
        list.__init__([])
        self.list_name = list_name

    def get_name(self):
        return self.list_name
