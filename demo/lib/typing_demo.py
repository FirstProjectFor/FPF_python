from typing import List

Vector = List[float]


def scale(scalar: float, vector: Vector) -> Vector:
    return [v * scalar for v in vector]


print(scale(10.0, [1, 2, 3, 4]))
