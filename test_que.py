import time
from itertools import product
sentences = [("can I, can I, can I",0), ("call you", 0.5), ("mine", 0.5)]


def gen(sens):
    for sen, delay in sens:
        time.sleep(delay)
        yield sen

for i in gen(sentences):
    print(i)

