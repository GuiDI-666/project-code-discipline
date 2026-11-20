"""待审查的改写，不表示推荐实现。"""


def consume(data, apply):
    values = [int(line) for line in data.splitlines()]
    for value in values:
        apply(value)
