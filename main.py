import lib

# List of chromosomes
FATHERS = []
SONS = []
SURVIVORS = []
# Float list
ERROR = []
# Int list
GENERATION = []


if __name__ == '__main__':
    print('Generating new chromosomes')
    for chromosome in range(1000):
        FATHERS.append(lib.fuzzy_chromosome_generator(lib.fuzzy_feeder()))
    for generation in range(200):
        print('Generation #{}'.format(generation))
        for tournament in range(100):
            print('Tournament #{}'.format(tournament))
            SURVIVORS.append(lib.tournament(FATHERS.copy()))

        print('Plot curve and error from best individual from this generation')
        best_in_generation = lib.find_best_in_generation(SURVIVORS.copy())
        GENERATION.append(generation)
        ERROR.append(best_in_generation.pop())
        lib.plot_results(GENERATION, ERROR, best_in_generation)

        print('Substituting individuals')
        SONS = lib.reproduction(SURVIVORS.copy())
        FATHERS.clear()
        FATHERS = SONS.copy()
        SONS.clear()
        SURVIVORS.clear()
