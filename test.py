import functools

from improved_sample import improved_sample
from original_sample import original_sample
from speed_test import test_speed
from distribution_test import test_distribution


def test_population(population, result, k) -> bool:
    assert len(result) == k
    assert len(set(result)) == len(result)  # elements have to be unique
    filter(lambda el: el in population, result)  # elements have to exist in original population


def trace_improved_algorithm():
    k = 20
    p_size = 100
    population = range(p_size)

    for i in range(5):
        result = improved_sample(population, k, False)
        test_population(population, result, k)
        print(result)

        result = improved_sample(population, k, True)
        test_population(population, result, k)
        print(sorted(result, reverse=True))


if __name__ == '__main__':
    no_shuffle_improved_sample = functools.partial(improved_sample, shuffle=False)
    test_cases = [
        ('Original sample', original_sample),
        ('Improved sample', improved_sample),
        ('Improved sample with reversed saved order', no_shuffle_improved_sample)
    ]

    trace_improved_algorithm()

    test_speed(test_cases)
    test_distribution(test_cases)
