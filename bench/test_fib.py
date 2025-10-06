from src.fib import fib


def test_fib(benchmark):
    result = benchmark(fib, 20)
    assert result >= 0
