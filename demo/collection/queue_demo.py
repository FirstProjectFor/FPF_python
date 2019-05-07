import queue

"""
队列，线程安全
"""

"""
先进先出
"""
q = queue.Queue()

for i in range(10):
    q.put(i)

while not q.empty():
    print(q.get(), end=' ')
print()

"""
先进后出
"""
s = queue.LifoQueue()
for i in range(10):
    s.put(i)

while not s.empty():
    print(s.get(), end=' ')

"""
优先级队列
"""

priority_queue = queue.PriorityQueue()


class Task:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value

    def __eq__(self, other):
        return self.priority == other.priority

    def __gt__(self, other):
        return self.priority > other.priority


for i in range(10):
    priority_queue.put(Task(i % 3, i))

while not priority_queue.empty():
    task = priority_queue.get()
    print('priority: {:>3}, value: {:>3}'.format(task.priority, task.value))
