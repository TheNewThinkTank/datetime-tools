
from enum import Flag, auto


class Timezone(Flag):
    CET = auto()
    CEST = auto()
    ICT = auto()
    DK = CET | CEST


if __name__ == "__main__":
    dk = Timezone.DK
    print(dk)
    print(Timezone.CET in dk)
    print(Timezone.DK.value)
