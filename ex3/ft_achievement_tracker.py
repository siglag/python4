import random


class colors:
    GREEN = "\033[0;92m"
    RED = "\033[0;91m"
    BLUE = "\033[0;94m"
    MAGENTA = "\033[0;95m"
    RESET = "\033[0m"


def gen_player_achievements(all_achievements: list[str]) -> set[str]:
    count = random.randint(3, len(all_achievements) - 1)
    return set(random.sample(all_achievements, count))


def format_achievements(achievements: set[str]) -> str:
    return f"{colors.MAGENTA}{achievements}{colors.RESET}"


def format_name(name: str) -> str:
    return f"{colors.GREEN}{name}{colors.RESET}"


def main() -> None:
    print("=== Achievement Tracker System ===")

    all_achievements = [
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Boss Slayer",
        "Hidden Path Finder"
    ]

    player_names = ["Alice", "Bob", "Charlie", "Dylan"]
    player_achievements = {}

    for player in player_names:
        achievements = gen_player_achievements(all_achievements)
        player_achievements[player] = achievements
        print(f"Player {format_name(player)}: {
            format_achievements(achievements)}")

    unique_achievements: set[str] = set()
    common_achievements: set[str] = set(all_achievements)

    for achievements in player_achievements.values():
        unique_achievements = unique_achievements.union(achievements)
        common_achievements = common_achievements.intersection(
            achievements
        )

    print(f"\nAll distinct achievements: {format_achievements(
        unique_achievements)}")
    print(f"Common achievements: {format_achievements(common_achievements)}")

    for player in player_names:
        other_achievements: set[str] = set()

        for other_player in player_names:
            if other_player != player:
                other_achievements = other_achievements.union(
                    player_achievements[other_player]
                )

        exclusive = player_achievements[player].difference(
            other_achievements
        )
        print(f"Only {format_name(player)} has: {
            format_achievements(exclusive)}\n")

    for player in player_names:
        missing = set(all_achievements).difference(
            player_achievements[player]
        )
        print(f"{format_name(player)}  {colors.RED}is missing{
            colors.RESET}: {format_achievements(missing)}\n")


if __name__ == "__main__":
    main()
