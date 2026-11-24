
import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser(
        description="description"
    )

    parser.add_argument(
        "--col",
        type=int,
        required = True,
    )

    parser.add_argument(
        "--threshold",
        type=float, 
        default=50
    )

    parser.add_argument(
        "--target_threshold",
        type = float,
        default=50.0
    )

    return parser.parse_args()


def main():
    args = parse_args()

    if args.col < 1:
        print("Error: --col must be >= 1", file=sys.stderr)
        sys.exit(1)

    count = 0

    for line in sys.stdin:
        print(f"raw: {line}")
        
        fields = line.split()

        if len(fields) < args.col:
            continue

        value = 0.0
        try:
            value = float(fields[args.col - 1])
        except Exception:
            # Skip header file
            continue

        if value > args.target_threshold:
            count += 1
            if count > args.threshold:
                print(f"Value:{value} of index {args.col} has violated the normal threshold for {args.threshold} times")
                count = 0


if __name__ == "__main__":
    main()
    
