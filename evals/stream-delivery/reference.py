"""逐行交付数字的原实现，仅作为评估输入。"""


def consume(data, apply):
    for line in data.splitlines():
        value = int(line)
        apply(value)
