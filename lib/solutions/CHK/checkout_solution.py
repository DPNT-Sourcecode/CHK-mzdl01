
# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):
    purchases = sorted(skus)
    A = {"price": 50, "discount_number": 3, "discount_price": 130} 
    B = {"price": 30, "discount_number": 2, "discount_price": 145}
    C = {"price": 20, "discount_number": 0, "discount_price": 0}

    available_items = {"A": A, "B": B, "C": C}
    counts = {"A": 0, "B": 0, "C": 0}
    if len(skus) == 0:
        return 0

    amount = 0
    for purchase in purchases:
        if purchase in available_items:
            print(purchase)
            counts[purchase] += 1
            if counts[purchase] == available_items[purchase][discount_number]:
                amount = amount - (available_items[purchase][amount] * 2)
                amount+= available_items[purchase][discount_price]
                counts[purchase] = 0
            else:
                amount += available_items[purchase][amount]
        else:
            return -1
    
    return amount

print(checkout("AAAA"))
