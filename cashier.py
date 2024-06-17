class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        print("Please insert coins.")
        total = 0
        total += int(input("How many dollars?: ")) * 1.00
        total += int(input("How many half dollars?: ")) * 0.50
        total += int(input("How many quarters?: ")) * 0.25
        total += int(input("How many nickels?: ")) * 0.05
        return total

    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False
