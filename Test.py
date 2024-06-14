class SandwichMachine:

    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for item in ingredients:
            if ingredients[item] > self.machine_resources.get(item, 0):
                print(f"Sorry there is not enough {item}.")
                return False
        return True

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

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]

def main():
    machine_resources = {
        "bread": 12,
        "ham": 18,
        "cheese": 24
    }

    recipes = {
        "small": {
            "ingredients": {
                "bread": 2,
                "ham": 4,
                "cheese": 4
            },
            "cost": 1.75,
        },
        "medium": {
            "ingredients": {
                "bread": 4,
                "ham": 6,
                "cheese": 8
            },
            "cost": 3.25,
        },
        "large": {
            "ingredients": {
                "bread": 6,
                "ham": 8,
                "cheese": 12
            },
            "cost": 5.5,
        }
    }

    machine = SandwichMachine(machine_resources)

    while True:
        choice = input("What would you like? (small/medium/large/off): ").strip().lower()

        if choice in ["small", "medium", "large"]:
            sandwich_recipe = recipes[choice]

            if machine.check_resources(sandwich_recipe['ingredients']):
                print(f"The cost of the {choice} sandwich is ${sandwich_recipe['cost']}.")
                payment = machine.process_coins()

                if machine.transaction_result(payment, sandwich_recipe['cost']):
                    machine.make_sandwich(choice, sandwich_recipe['ingredients'])

        elif choice == "off":
            print("Turning off the machine. Goodbye!")
            break

        else:
            print("Invalid selection. Please choose again.")

if __name__ == "__main__":
    main()
