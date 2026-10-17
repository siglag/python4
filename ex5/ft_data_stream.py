from typing import Generator
import random


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
        print(f"Event {index}: Player {data[0]} did action {data[1]}")
    built_list = [next(events) for _ in range(10)]
    print(f"Built list of 10 events: {built_list}")
    for event in consume_event(built_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {built_list}")
