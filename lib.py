import math
import random
from matplotlib import pyplot as plt

# DEFAULT_CHROMOSOME = (8, 25, 4, 45, 10, 17, 35)
WEEK_DAYS = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

# Hour in military format for ease of use
HOURS = ('0000', '0030', '0100', '0130', '0200', '0230', '0300', '0330', '0400', '0430', '0500', '0530', '0600', '0630',
         '0700', '0730', '0800', '0830', '0900', '0930', '1000', '1030', '1100', '1130', '1200', '1230', '1300', '1330',
         '1400', '1430', '1500', '1530', '1600', '1630', '1700', '1730', '1800', '1830', '1900', '1930', '2000', '2030',
         '2100', '2130', '2200', '2230', '2300', '2330')

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

figure, axis = plt.subplots(nrows=1, ncols=2)
figure.suptitle('Curve GA')
plt.ion()
axis[1].set_title("Error evolution")
axis[1].set_ylabel('Error')
axis[1].grid(True)


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
    # Obtaining default curve values
    # default_x, default_y = generate_default_curve_points()
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


def plot_results(x, default_y, new_y, generation, error, current_generation):
    # Clean th curve plot
    axis[0].clear()
    axis[0].grid(True)
    axis[0].set_title("Curve adaptation")

    # Curve adaptation
    axis[0].plot(x, default_y, color='g', label='Default curve')
    axis[0].plot(x, new_y, color='r', label='Generated curve')
    axis[0].legend()

    # Error evolution
    axis[1].set_xlabel('Generation #{}'.format(current_generation))
    axis[1].plot(generation, error)

    plt.show()
    plt.pause(0.00001)


def reproduction(survivors):
    # TODO: Remove aptitude function to avoid introduce false values
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
        # for j in range(mutation_factor):
        individual[random.choice(range(48))] = generate_genes()
