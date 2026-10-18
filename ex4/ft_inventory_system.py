import sys


class colors:
    GREEN = "\033[0;92m"
    RED = "\033[0;91m"
    BLUE = "\033[0;94m"
    MAGENTA = "\033[0;95m"
    RESET = "\033[0m"

    def green(self, text: str) -> str:
        return f"{self.GREEN}{text}{self.RESET}"

    def red(self, text: str) -> str:
        return f"{self.RED}{text}{self.RESET}"

    def blue(self, text: str) -> str:
        return f"{self.BLUE}{text}{self.RESET}"

    def magenta(self, text: str) -> str:
        return f"{self.MAGENTA}{text}{self.RESET}"


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = {}

    for argument in sys.argv[1:]:
        parts = argument.split(":")

        if len(parts) != 2 or not parts[0] or int(parts[1]) < 0:
            print(f"{colors().red("Error - invalid parameter")} {
                colors().blue(argument)}")
            continue

        item = parts[0]

        if item in inventory:
            print(f"{colors().magenta("Redundant item")} '{
                colors().blue(item)}' {colors().magenta("- discarding")}")
            continue

        try:
            quantity = int(parts[1])
        except ValueError as error:
            print(f"{colors().red("Quantity error for")} '{
                colors().blue(item)}': {error}")
            continue

        inventory.update({item: quantity})

    print(f"Got inventory: {inventory}")

    items = list(inventory.keys())
    print(f"Item list: {items}")

    total_quantity = sum(inventory.values())
    print(
        f"Total quantity of the {len(items)} items: "
        f"{total_quantity}"
    )

    if total_quantity > 0:
        for item in inventory:
            percentage = inventory[item] / total_quantity * 100
            print(f"Item {item} represents {round(percentage, 1)}%")

    if len(inventory) > 0:
        most_abundant = list(inventory.keys())[0]
        least_abundant = most_abundant

        for item in inventory:
            if inventory[item] > inventory[most_abundant]:
                most_abundant = item

            if inventory[item] < inventory[least_abundant]:
                least_abundant = item

        print(
            f"Item most abundant: {most_abundant} "
            f"with quantity {inventory[most_abundant]}"
        )
        print(
            f"Item least abundant: {least_abundant} "
            f"with quantity {inventory[least_abundant]}"
        )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
