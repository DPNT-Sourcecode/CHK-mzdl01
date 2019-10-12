
# noinspection PyUnusedLocal
# skus = unicode string
from . import item
def checkout(skus):
    A = Item("A", 50, 3, 130)
    offers = {"3A": 130, "2B": 45}
    prices = {"A": 50, "B": 30 ,"C": 20}
    if len(sku) == 0:
        return 0

    res = {}
    for purchase in skus:
        if purchase in offers:
            if purchase in res:
                res[purchase] += 1
            else:
                res[purchase] = 1
        else:
            return -1

    amount = 0

    for key, val in res.items():
        off = str(val) + str(key)
        if off in offers:
            amount += offers[off]
        else:
            amount+= offers[key] * val

    return amount


sku = "AAAA"
print(checkout(sku))