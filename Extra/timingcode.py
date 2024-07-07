import time
import timeit


def measureTime(func):
    start = time.time()
    func()
    end = time.time()
    print("Time taken: ", end - start)


def powers(limit):
    return [x**2 for x in range(limit)]


# start = time.time()
# powers(500000)
# end = time.time()
# print(end - start)

measureTime(lambda: powers(500000))

print(timeit.timeit("[x**2 for x in range(10)]"))
