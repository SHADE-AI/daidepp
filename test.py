from time import time

with open("test.txt", "a") as f:
    f.write(f"{time()}\n")
