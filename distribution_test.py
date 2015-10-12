import png

POPULATION_LENGTH = 1000
K = 100
ITERATIONS = 10000
PNG_HEIGHT = 100


def test_distribution(test_cases):
    for fun in test_cases:
        test_sample(fun[0], fun[1])


def test_sample(name: str, sample_fun):
    population = range(POPULATION_LENGTH)
    dist = [0] * len(population)

    for i in range(ITERATIONS):
        result = sample_fun(population, K)
        for el in result:
            dist[el] += 1

    max_el = max(dist)

    distribution = list(map(
        lambda n: int((1 - n / max_el) * (PNG_HEIGHT - 1)), dist))

    png_data = [[255 for j in range(POPULATION_LENGTH)]
                     for i in range(PNG_HEIGHT)]

    for i in range(len(distribution)):
        dist_value = distribution[i]
        png_data[dist_value][i] = 0

    w = png.Writer(POPULATION_LENGTH, PNG_HEIGHT, greyscale=True)
    file_name = '%s_distribution.png' % name.lower().replace(' ', '_')
    with open(file_name, 'wb+') as f:
        w.write(f, png_data)



