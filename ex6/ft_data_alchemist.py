import random


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
    print("=== Game Data Alchemist ===")

    players = ["Alice", "bob", "Charlie", "dylan", "Emma",
               "Gregory", "john", "kevin", "Liam"]

    print(f"Initial list of players: {colors().magenta(str(players))}")

    capitalized_players = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {
        colors().magenta(str(capitalized_players))}")

    capitalized_only = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {
        colors().magenta(str(capitalized_only))}")

    scores = {name: random.randint(50, 1000) for name in capitalized_players}
    print(f"Score dict: {colors().magenta(str(scores))}")

    average = sum(scores.values()) / len(scores)
    print(f"Score average is {colors().green(f'{average:.2f}')}")

    high_scores = {name: score for name, score in scores.items()
                   if score > average}
    print(f"High scores: {colors().magenta(str(high_scores))}")


if __name__ == "__main__":
    main()
