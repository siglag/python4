import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coordinates = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )

        try:
            values = coordinates.split(",")

            if len(values) != 3:
                print("Invalid syntax")
                continue

            x = float(values[0])
            y = float(values[1])
            z = float(values[2])

            return (x, y, z)

        except ValueError as error:
            invalid_value = str(error).split("'")[1]
            print(f"Error on parameter '{invalid_value}': {error}")


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")

    first_pos = get_player_pos()

    print(f"Got a first tuple: {first_pos}")
    print(
        f"It includes: X={first_pos[0]}, "
        f"Y={first_pos[1]}, Z={first_pos[2]}"
    )

    distance = math.sqrt(
        first_pos[0] ** 2
        + first_pos[1] ** 2
        + first_pos[2] ** 2
    )

    print(f"Distance to center: {round(distance, 4)}")

    print("Get a second set of coordinates")
    second_pos = get_player_pos()

    distance = math.sqrt(
        (second_pos[0] - first_pos[0]) ** 2
        + (second_pos[1] - first_pos[1]) ** 2
        + (second_pos[2] - first_pos[2]) ** 2
    )

    print(
        "Distance between the 2 sets of coordinates: "
        f"{round(distance, 4)}"
    )


if __name__ == "__main__":
    main()
