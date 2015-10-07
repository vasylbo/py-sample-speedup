from math import log as _log, ceil as _ceil
from _collections_abc import Set as _Set, Sequence as _Sequence


# original sample from random (python internal lib) copied as is
# except of not being a bounded to random now and that's why changed from
# randbelow = self._randbelow
# to
# randbelow = functools.partial(random.randrange, 0)
import random
import functools


def original_sample(population, k):
    """Chooses k unique random elements from a population sequence or set.
    Returns a new list containing elements from the population while
    leaving the original population unchanged.  The resulting list is
    in selection order so that all sub-slices will also be valid random
    samples.  This allows raffle winners (the sample) to be partitioned
    into grand prize and second place winners (the subslices).
    Members of the population need not be hashable or unique.  If the
    population contains repeats, then each occurrence is a possible
    selection in the sample.
    To choose a sample in a range of integers, use range as an argument.
    This is especially fast and space efficient for sampling from a
    large population:   sample(range(10000000), 60)
    """

    # Sampling without replacement entails tracking either potential
    # selections (the pool) in a list or previous selections in a set.

    # When the number of selections is small compared to the
    # population, then tracking selections is efficient, requiring
    # only a small set and an occasional reselection.  For
    # a larger number of selections, the pool tracking method is
    # preferred since the list takes less space than the
    # set and it doesn't suffer from frequent reselections.

    if isinstance(population, _Set):
        population = tuple(population)
    if not isinstance(population, _Sequence):
        raise TypeError("Population must be a sequence or set.  For dicts, use list(d).")
    randbelow = functools.partial(random.randrange, 0)
    n = len(population)
    if not 0 <= k <= n:
        raise ValueError("Sample larger than population")
    result = [None] * k
    setsize = 21        # size of a small set minus size of an empty list
    if k > 5:
        setsize += 4 ** _ceil(_log(k * 3, 4)) # table size for big sets
    if n <= setsize:
        # An n-length list is smaller than a k-length set
        pool = list(population)
        for i in range(k):         # invariant:  non-selected at [0,n-i)
            j = randbelow(n-i)
            result[i] = pool[j]
            pool[j] = pool[n-i-1]   # move non-selected item into vacancy
    else:
        selected = set()
        selected_add = selected.add
        for i in range(k):
            j = randbelow(n)
            while j in selected:
                j = randbelow(n)
            selected_add(j)
            result[i] = population[j]
    return result
