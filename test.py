import timeit
import functools

from my_sample import improved_sample
from original_sample import original_sample

POPULATION_SIZE = 5000
MIN_TEST_POPULATION = 900
MAX_TEST_POPULATION = 5000
TEST_STEP = 2000
TIME_IT_NUMBER = 100


def test_sample(sample_fun):
    print(sample_fun.__name__)
    population = range(POPULATION_SIZE)

    for k in range(MIN_TEST_POPULATION, MAX_TEST_POPULATION, TEST_STEP):
        tester = functools.partial(sample_fun, population, k)
        test_population(population, tester(), k)  # assert algorithm

        print('Getting {k} elements out of {pop_len} - {time} seconds'.format(
            k=k,
            pop_len=len(population),
            time=timeit.timeit(tester, number=TIME_IT_NUMBER)
        ))


def test_population(population, result, k) -> bool:
    assert len(result) == k
    assert len(set(result)) == len(result)  # elements have to be unique
    filter(lambda el: el in population, result)  # elements have to exist in original population


if __name__ == '__main__':
    for fun in [original_sample, improved_sample]:
        test_sample(fun)
