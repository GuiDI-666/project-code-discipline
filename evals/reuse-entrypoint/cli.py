import argparse

from labels import item_count


CAPACITY = 10


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("installed", type=int, choices=range(CAPACITY + 1))
    args = parser.parse_args()
    print(f"Installed: {item_count(args.installed)}")


if __name__ == "__main__":
    main()
