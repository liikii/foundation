"""
a recursion example.
A(0, y) = y + 1
A(x, 0) = A(x - 1, 1)
A(x, y) = A(x - 1, A(x, y - 1))
"""


def ack(x: int, y: int):
    if x > 0 and y > 0:
        return ack(x-1, ack(x, y-1))
    if x > 0 and y == 0:
        return ack(x-1, 1)
    if x == 0:
        return y + 1


print(ack(2, 2))
print(ack(5, 5))
