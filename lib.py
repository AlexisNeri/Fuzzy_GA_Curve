import math
import random
from matplotlib import pyplot as plt
# from mpl_toolkits import mplot3d
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


# def generate_chromosome():
#     chromosome = []
#     for gen in range(len(HOURS)):
#         chromosome.append(generate_genes())
#     print('This is the generated chromosome: {}'.format(chromosome))
#     return chromosome


def generate_genes():
    gen = []
    for allele in range(len(WEEK_DAYS)):
        gen.append(random.choice(range(20, 44)))
    print('The generated gen is: {}'.format(gen))
    return gen


def fuzzy_feeder():
    seed = []
    for i in range(39):
        seed.append(random.choice(range(1, 60)))
    return seed


def fuzzy_chromosome_generator(chromosome, weight=random.choice(range(1, 6))):
    m1 = float(chromosome[0]) / float(weight)
    m2 = float(chromosome[1]) / float(weight)
    m3 = float(chromosome[2]) / float(weight)
    m4 = float(chromosome[3]) / float(weight)
    m5 = float(chromosome[4]) / float(weight)
    m6 = float(chromosome[5]) / float(weight)
    de1 = float(chromosome[6]) / float(weight)
    de2 = float(chromosome[7]) / float(weight)
    de3 = float(chromosome[8]) / float(weight)
    de4 = float(chromosome[9]) / float(weight)
    de5 = float(chromosome[10]) / float(weight)
    de6 = float(chromosome[11]) / float(weight)
    p1 = float(chromosome[12]) / float(weight)
    p2 = float(chromosome[13]) / float(weight)
    p3 = float(chromosome[14]) / float(weight)
    p4 = float(chromosome[15]) / float(weight)
    p5 = float(chromosome[16]) / float(weight)
    p6 = float(chromosome[17]) / float(weight)
    p7 = float(chromosome[18]) / float(weight)
    p8 = float(chromosome[19]) / float(weight)
    p9 = float(chromosome[20]) / float(weight)
    q1 = float(chromosome[21]) / float(weight)
    q2 = float(chromosome[22]) / float(weight)
    q3 = float(chromosome[23]) / float(weight)
    q4 = float(chromosome[24]) / float(weight)
    q5 = float(chromosome[25]) / float(weight)
    q6 = float(chromosome[26]) / float(weight)
    q7 = float(chromosome[27]) / float(weight)
    q8 = float(chromosome[28]) / float(weight)
    q9 = float(chromosome[29]) / float(weight)
    r1 = float(chromosome[30]) / float(weight)
    r2 = float(chromosome[31]) / float(weight)
    r3 = float(chromosome[32]) / float(weight)
    r4 = float(chromosome[33]) / float(weight)
    r5 = float(chromosome[34]) / float(weight)
    r6 = float(chromosome[35]) / float(weight)
    r7 = float(chromosome[36]) / float(weight)
    r8 = float(chromosome[37]) / float(weight)
    r9 = float(chromosome[38]) / float(weight)

    mf1 = []
    mf2 = []
    mf3 = []

    x = []
    y = []
    z = []

    for i in range(48):
        x.append(float(i))
        mf1.append(math.exp((-(x[i] - m1) ** 2) / (2 * de1 ** 2)))
        mf2.append(math.exp((-(x[i] - m2) ** 2) / (2 * de2 ** 2)))
        mf3.append(math.exp((-(x[i] - m3) ** 2) / (2 * de3 ** 2)))
        result = []
        mf4 = []
        mf5 = []
        mf6 = []
        a1 = []
        a2 = []
        a3 = []
        a4 = []
        a5 = []
        a6 = []
        a7 = []
        a8 = []
        a9 = []
        b = []
        a = []
        for j in range(7):
            if float(j) in y:
                pass
            else:
                y.append(float(j))

            mf4.append(math.exp((-(y[j] - m4) ** 2) / (2 * de4 ** 2)))
            mf5.append(math.exp((-(y[j] - m5) ** 2) / (2 * de5 ** 2)))
            mf6.append(math.exp((-(y[j] - m6) ** 2) / (2 * de6 ** 2)))

            b.append(mf1[i] + mf2[i] + mf3[i] + mf4[j] + mf5[j] + mf6[j])

            a1.append(mf1[i] * mf4[j] * ((p1 * x[i]) + (q1 * y[j]) + r1))
            a2.append(mf1[i] * mf5[j] * ((p2 * x[i]) + (q2 * y[j]) + r2))
            a3.append(mf1[i] * mf6[j] * ((p3 * x[i]) + (q3 * y[j]) + r3))
            a4.append(mf2[i] * mf4[j] * ((p4 * x[i]) + (q4 * y[j]) + r4))
            a5.append(mf2[i] * mf5[j] * ((p5 * x[i]) + (q5 * y[j]) + r5))
            a6.append(mf2[i] * mf6[j] * ((p6 * x[i]) + (q6 * y[j]) + r6))
            a7.append(mf3[i] * mf4[j] * ((p7 * x[i]) + (q7 * y[j]) + r7))
            a8.append(mf3[i] * mf5[j] * ((p8 * x[i]) + (q8 * y[j]) + r8))
            a9.append(mf3[i] * mf6[j] * ((p9 * x[i]) + (q9 * y[j]) + r9))

            a.append(a1[j] + a2[j] + a3[j] + a4[j] + a5[j] + a6[j] + a7[j] + a8[j] + a9[j])

            result.append(a[j] / b[j])
        z.append(result)
    return z


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


def mutation(sons, mutation_factor=random.choice(range(1, 5))):
    for i in range(mutation_factor):
        individual = sons[random.choice(range(len(sons)))]
        individual[random.choice(range(48))] = generate_genes()
