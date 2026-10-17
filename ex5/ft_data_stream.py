from typing import Generator
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


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["motch", "siglag", "mohammad", "dude"]
    actions = ["killed", "found", "helped", "lost", "stapped"]

    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(
        built_list: list[tuple[str, str]]
                  ) -> Generator[tuple[str, str], None, None]:

    for _ in range(len(built_list)):
        yield built_list.pop(random.randint(0, len(built_list) - 1))


if __name__ == "__main__":

    events = gen_event()
    for index in range(1000):
        data = next(events)
        print(f"Event {colors().blue(str(index))}: Player {
            colors().blue(data[0])} did action {colors().blue(data[1])}")
    built_list = [next(events) for _ in range(10)]
    print(f"\n{colors().green("Built list of 10 events:")} {
        colors().magenta(str(built_list))}\n")
    for event in consume_event(built_list):
        print(f"{colors().green("Got event from list:")} {
            colors().magenta(str(event))}")
        print(f"{colors().red("Remains in list:")} {
            colors().magenta(str(built_list))}\n")
