# Oskar Svedlund
# TEINF-20
# 2023-01-11 (year:month:day)
# data classes

from dataclasses import dataclass

@dataclass
class test1:
    name: str
    value: int
    cunt: bool

    def print_out(self):
        print("hello")

me = test1("sup", 10, False)
mr = test1("mr elden ring", 412, True)

def testfunction(thing: test1):
    thing.print_out()


if __name__ == "__main__":
    in_use = input()
    print(me.name)

    testfunction(me)
