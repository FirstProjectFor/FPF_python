from dataclasses import dataclass


@dataclass
class Person:
    x: float = 0
    y: int = 1
    z: str = 2


print(Person())
