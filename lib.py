import random
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

WEEK_DAYS = (0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0)

HOURS = (0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0,
         20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0,
         38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0)

DEFAULT_CHROMOSOME = (
    (22, 21, 22, 22, 22, 22, 22),
    (22, 22, 22, 22, 22, 30, 22),
    (22, 22, 22, 22, 22, 32, 22),
    (22, 21, 22, 22, 22, 28, 22),
    (24, 21, 24, 24, 24, 24, 24),
    (28, 22, 28, 28, 28, 28, 28),
    (27, 21, 27, 27, 27, 27, 27),
    (27, 21, 27, 27, 27, 27, 27),
    (28, 23, 28, 28, 28, 28, 28),
    (28, 28, 28, 28, 28, 28, 28),
    (28, 28, 28, 28, 28, 28, 28),
    (26, 26, 26, 26, 26, 26, 26),
    (23, 23, 23, 23, 23, 23, 23),
    (22, 22, 22, 22, 22, 22, 22),
    (23, 23, 23, 23, 23, 23, 23),
    (25, 25, 25, 25, 25, 25, 25),
    (30, 30, 30, 30, 30, 30, 30),
    (36, 36, 36, 36, 36, 36, 36),
    (41, 41, 41, 41, 41, 41, 41),
    (37, 37, 37, 37, 37, 37, 37),
    (32, 32, 32, 32, 32, 32, 32),
    (31, 31, 31, 31, 31, 31, 31),
    (29, 40, 29, 25, 29, 29, 29),
    (30, 30, 30, 30, 30, 30, 30),
    (29, 29, 29, 29, 29, 29, 29),
    (30, 30, 30, 30, 30, 30, 30),
    (30, 30, 30, 30, 30, 30, 30),
    (30, 30, 30, 30, 30, 30, 30),
    (31, 31, 31, 31, 31, 31, 31),
    (31, 31, 31, 31, 31, 31, 31),
    (30, 30, 30, 30, 30, 30, 30),
    (28, 28, 28, 28, 28, 28, 28),
    (28, 28, 28, 28, 28, 28, 28),
    (30, 30, 30, 30, 30, 30, 30),
    (29, 29, 29, 29, 29, 29, 29),
    (30, 30, 30, 30, 30, 30, 30),
    (31, 31, 31, 31, 31, 31, 31),
    (33, 33, 33, 33, 33, 33, 33),
    (30, 30, 30, 30, 30, 30, 30),
    (28, 28, 28, 28, 28, 28, 28),
    (26, 26, 26, 26, 26, 26, 26),
    (25, 25, 25, 25, 25, 25, 25),
    (25, 25, 25, 25, 25, 25, 25),
    (25, 25, 25, 25, 25, 25, 25),
    (24, 24, 24, 24, 24, 24, 24),
    (23, 23, 23, 23, 23, 23, 23),
    (22, 22, 22, 22, 22, 22, 22),
    (22, 22, 22, 22, 22, 22, 22)
)

# Generating static points
Y, X = np.meshgrid(WEEK_DAYS, HOURS)
default_z = np.array(DEFAULT_CHROMOSOME)
# Put plot into dynamic mode
plt.ion()
# Generate plot and subplots
figure = plt.figure()
figure.suptitle('Neuro-Fuzzy Network')
generated_surface = figure.add_subplot(131, projection='3d')

error_evolution = figure.add_subplot(132)
error_evolution.set_title("Error Evolution")
error_evolution.set_ylabel('Error')
error_evolution.grid(True)

default_surface = figure.add_subplot(133, projection='3d')
default_surface.set_xlabel('Hour')
default_surface.set_ylabel('Day')
default_surface.set_zlabel('Average Time')


def generate_chromosome():
    chromosome = []
    for gen in range(len(HOURS)):
        chromosome.append(generate_genes())
    print('This is the generated chromosome: {}'.format(chromosome))
    return chromosome


def generate_genes():
    gen = []
    for allele in range(len(WEEK_DAYS)):
        gen.append(random.choice(range(60)))
    print('The generated gen is: {}'.format(gen))
    return gen


def tournament(fathers):
    participants = []
    aptitude_tag_list = []
    winner = []

    number_of_participants = random.choice(range(2, 30))

    print('Generating randomly {} participants\n'.format(number_of_participants))
    for i in range(number_of_participants):
        candidate_chromosome = fathers[random.choice(range(len(fathers)))]
        participants.append(candidate_chromosome)
    print('These are the participants: {}\n'.format(participants))

    # Calculating and appending curve error
    for candidate in participants:
        error = calculate_error(candidate)
        aptitude_tag_list.append(error)
        if len(candidate) > 48:
            candidate[-1] = error
        else:
            candidate.append(error)

    # Getting winner chromosome
    print('Getting winner chromosome\n')
    winner_value = min(aptitude_tag_list)
    for candidate in participants:
        if winner_value == candidate[-1]:
            winner = candidate

    return winner


def calculate_error(candidate):
    error = []
    for x_axis in range(len(HOURS)):
        for y_axis in range(len(WEEK_DAYS)):
            error.append(abs(DEFAULT_CHROMOSOME[x_axis][y_axis] - candidate[x_axis][y_axis]))
    error = sum(error)
    return error


# TODO: Reuse this function in tournament function
def find_best_in_generation(survivors):
    attitude_tag_list = []
    winner = []
    for chromosome in survivors:
        attitude_tag_list.append(chromosome[-1])

    best_in_generation = min(attitude_tag_list)

    for candidate in survivors:
        if best_in_generation == candidate[-1]:
            winner = candidate
    return winner


def plot_results(generation, error, z, x=X, y=Y):
    # Generate new z matrix
    z_np_real = np.array(z)
    # Clean the subplot
    generated_surface.clear()

    # Generated surface
    generated_surface.set_xlabel('Hour')
    generated_surface.set_ylabel('Day')
    generated_surface.set_zlabel('Average Time')
    generated_surface.plot_surface(x, y, z_np_real, cmap='viridis')

    # Error evolution
    error_evolution.set_xlabel('Generation #{}'.format(generation[-1]))
    error_evolution.plot(generation, error)

    # Default surface
    default_surface.plot_surface(x, y, default_z, cmap='viridis')

    plt.show()
    plt.pause(0.00001)


def reproduction(survivors):
    sons = []
    fathers, mothers = split_list(survivors)
    for chromosome in range(len(fathers)):
        male_chromosome = fathers[chromosome]
        female_chromosome = mothers[chromosome]
        # Generating 2 sons per couple
        for j in range(2):
            slice_point = random.choice(range(48))

            # Adding additional randomness to the genes mixing
            randomizer = bool(random.getrandbits(1))
            if randomizer:
                subject_a = male_chromosome
                subject_b = female_chromosome
            else:
                subject_a = female_chromosome
                subject_b = male_chromosome
            son = subject_a[:slice_point]
            son.extend(subject_b[slice_point:])
            print('Generated son #{0}: {1} from fathers: {2} and {3}'.format(chromosome, son, male_chromosome,
                                                                             female_chromosome))
            sons.append(son)
    # Once reproduction has finished we called mutation to generate random mutations
    mutation(sons)
    return sons


def split_list(a_list):
    half = len(a_list) // 2
    return a_list[:half], a_list[half:]


def mutation(sons, mutation_factor=random.choice(range(1, 25))):
    for i in range(mutation_factor):
        individual = sons[random.choice(range(len(sons)))]
        individual[random.choice(range(48))] = generate_genes()
