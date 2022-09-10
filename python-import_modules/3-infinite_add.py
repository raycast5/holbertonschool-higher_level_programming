#!/usr/bin/python3
if __name__ == "__main__":
    import sys
argv = sys.argv
argc = len(argv)
total = 0
for i in range(1, argc):
    total += int(argv[i])
print(total)
