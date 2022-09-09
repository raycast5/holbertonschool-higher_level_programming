#!/usr/bin/python3
if __name__ == "__main__":
    import sys
argv = sys.argv
argc = len(argv) - 1
if argc == 0:
    print("0 arguments.")
else:
    print(f"{argc} argument", end=":\n" if argc == 1 else "s:\n")
    for a in range(1, argc + 1):
        print(f"{a}: {argv[a]}")
