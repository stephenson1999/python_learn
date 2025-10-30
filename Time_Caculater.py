import time

start = time.time()
def print_pairs(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])

print_pairs("11")
stop = time.time()

print(stop - start)