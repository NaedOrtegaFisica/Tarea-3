

class serie:
    def __init__(self, length, range_down, range_top,):

        from random import randint
        self.list = [randint(range_down, range_top) for n in range(length)]



import pandas as pd

serie_1 = serie(100, 1, 4)

serie_2 = serie(100, 1, 3)

serie_3 = serie(100, 10000, 30000)

list = [[serie_1.list[m], serie_2.list[m], serie_3.list[m]] for m in range(len(serie_1.list)) ]

print(pd.DataFrame(list, columns=["bedrs", "bathrs", "price_sqr_meter"]))

bigcoulums = pd.DataFrame(serie_3.list)

print(bigcoulums)

n = [i for i in range(0,300)]

print(bigcoulums.reindex(index = [n]))



