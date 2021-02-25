import sys

print((any(map(lambda x: x == 0, map(int, sys.stdin.read().strip().split())))))
