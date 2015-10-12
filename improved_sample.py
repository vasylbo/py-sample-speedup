import random
import functools

from _collections_abc import Set as _Set, Sequence as _Sequence


# my sample
def improved_sample(population, k, shuffle=True):
    if isinstance(population, _Set):
        population = tuple(population)
    if not isinstance(population, _Sequence):
        raise TypeError("Population must be a sequence or set.  For dicts, use list(d).")

    n = len(population)
    if not 0 <= k <= n:
        raise ValueError("Sample larger than population")

    result = []

    left = k
    available = n

    rand_gen = functools.partial(random.random)  # to equalize chances of being slower cause of closure

    while left > 0 and available > 0:
        rand = rand_gen()

        if rand < left / available:
            result.append(population[available - 1])
            left -= 1
        available -= 1

    if shuffle:
        random.shuffle(result)

    return result
