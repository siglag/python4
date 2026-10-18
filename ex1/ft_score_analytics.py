import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")
        return

    scores = []

    for argument in sys.argv[1:]:
        try:
            score = int(argument)
            if score < 0:
                raise Exception("Score cannot be negative")
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{argument}'")
        except Exception as e:
            print(f"Error: {e}")

    if len(scores) == 0:
        print("No scores provided. Usage: python3"
              "ft_score_analytics.py <score1> <score2> ...")
        return

    total = sum(scores)
    average = total / len(scores)
    high_score = max(scores)
    low_score = min(scores)
    score_range = high_score - low_score

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()
