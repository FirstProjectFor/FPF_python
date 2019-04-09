class MyQueue:
    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        self.data.insert(0, x)

    def pop(self) -> int:
        return self.data.pop()

    def peek(self) -> int:
        return self.data[-1]

    def empty(self) -> bool:
        if self.data:
            return False
        else:
            return True
