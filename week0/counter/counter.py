class Counter:
    __counter: str

    def __init__(self) -> None:
        self.__counter = 0

    def addCount(self) -> None:
        self.__counter += 1

    def getCount(self) -> int:
        return self.__counter

    def zeroCount(self) -> None:
        self.__counter = 0
