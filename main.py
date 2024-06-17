import data
import sandwich_maker
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
machine = sandwich_maker.SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    while True:
        choice = input("What would you like? (small/medium/large/off): ").strip().lower()

        if choice in ["small", "medium", "large"]:
            sandwich_recipe = recipes[choice]

            if machine.check_resources(sandwich_recipe['ingredients']):
                print(f"The cost of the {choice} sandwich is ${sandwich_recipe['cost']}.")
                payment = cashier_instance.process_coins()

                if cashier_instance.transaction_result(payment, sandwich_recipe['cost']):
                    machine.make_sandwich(choice, sandwich_recipe['ingredients'])

        elif choice == "off":
            print("Turning off the machine. Goodbye!")
            break

        else:
            print("Invalid selection. Please choose again.")

if __name__ == "__main__":
    main()
