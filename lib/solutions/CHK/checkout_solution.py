
# noinspection PyUnusedLocal
# skus = unicode string
from item import Item

def checkout(skus):
    sorted(skus)
    A = Item("A", 50, 3, 130)
    B = Item("B", 30, 2, 45)
    C = Item("C", 20)

    # offers = {"3A": 130, "2B": 45}
    # prices = {"A": 50, "B": 30 ,"C": 20}

    available_items = {"A": A, "B": B, "C": C}
    counts = {"A": 0, "B": 0, "C": 0}
    if len(sku) == 0:
        return 0

    amount = 0
    for purchase in skus:
        if purchase in available_items:
            counts[purchase] += 1
            if counts[purchase] == available_items[purchase].discount_number:
                amount = amount - (available_items[purchase].amount * 2)
                amount+= available_items[purchase].discount_number
            else:
                amount += available_items[purchase].amount
            print(amount)
        else:
            return -1
    
    return amount


sku = "ABAA"
print(checkout(sku))
