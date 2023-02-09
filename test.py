from time import time
import sys

assert len(sys.argv) == 2

with open("test.txt", "a") as f:
    f.write(f"{time()}\n")
    f.write(f"{sys.argv[1]}\n")
