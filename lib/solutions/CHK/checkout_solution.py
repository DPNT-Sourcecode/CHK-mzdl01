
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    offers = {"A": 50, "B": 30 ,"C": 20, "D": 15, "3A": 130, "2B": 45}

    purchases = skus.split(",")
    res = {}
    for purchase in purchases:
        if purchase in offers:
            res[purchase] = 1

    amount = 0

    print(res)


skus = "A,B,C"
checkout(skus)
