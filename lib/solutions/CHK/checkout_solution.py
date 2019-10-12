
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    offers = {"A": 50, "B": 30 ,"C": 20, "D": 15, "3A": 130, "2B": 45}

    purchases = skus.split(",")
    res = {}
    for purchase in purchases:
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
