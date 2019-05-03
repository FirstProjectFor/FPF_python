class Person:
    def __init__(self):
        self.name = 'LiLei'

    def get_name(self) -> str:
        return self.name

    @staticmethod
    def say(self, text: str = '') -> str:
        print('[{:s}] : {:s} !'.format(self.name, text))


p = Person()
print(Person.get_name(p))
print(p.get_name())

Person.say(p, 'hello')
p.say(p, "hello")
