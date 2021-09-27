import argparse
import pickle
import tempfile

from collections import defaultdict
from pathlib import Path

arg_parser = argparse.ArgumentParser(description="homework 1 for Nvidia Master's program at MIPT")
arg_parser.add_argument("--key", "-k", type=str, required=True)
arg_parser.add_argument("--val", "-v", type=str, required=False)

STORAGE_PATH = Path(tempfile.gettempdir()) / Path("storage.data")


def main(args: argparse.Namespace):
    if STORAGE_PATH.exists():
        with open(STORAGE_PATH, "rb") as dumped_storage:
            storage = pickle.load(dumped_storage)
    else:
        storage = defaultdict(list)

    if not args.val:
        print(", ".join(storage[args.key]).strip())
    else:
        storage[args.key].append(args.val)

    with open(STORAGE_PATH, "wb") as storage_dump:
        pickle.dump(storage, storage_dump)


if __name__ == "__main__":
    main(arg_parser.parse_args())
