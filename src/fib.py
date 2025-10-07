from multiprocessing import Pool


def fib_worker(n):
    if n < 2:
        return n
    return fib_worker(n - 1) + fib_worker(n - 2)


def fib(n: int) -> int:
    if n < 2:
        return n
    with Pool(2) as p:
        a, b = p.map(fib_worker, [n - 1, n - 2])
    return a + b
