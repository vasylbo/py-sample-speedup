import timeit
import functools

POPULATION_SIZE = 5000
MIN_TEST_POPULATION = 900
MAX_TEST_POPULATION = 5000
TEST_STEP = 2000
TIME_IT_NUMBER = 100


def test_speed(test_cases):
    for fun in test_cases:
        test_sample(fun[0], fun[1])


def test_sample(name, sample_fun):
    print('Speed test for %s' % name)
    population = range(POPULATION_SIZE)

    for k in range(MIN_TEST_POPULATION, MAX_TEST_POPULATION, TEST_STEP):
        tester = functools.partial(sample_fun, population, k)
        time = timeit.timeit(tester, number=TIME_IT_NUMBER)

        print('Getting {k} elements out of {pop_len} - {time} seconds'.format(
            k=k,
            pop_len=len(population),
            time=time
        ))
