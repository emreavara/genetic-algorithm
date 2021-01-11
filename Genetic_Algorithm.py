from random import uniform, randint
from math import cos

number_of_individuals = 200
group = []  # creation of a list
number_of_iterations = 100

# initialization of variables

length_of_group = 200
number_of_missing = 0
number_of_crossover = 0
number_of_mutation = 0


def initialization(n):  # generation of a cluster
    for i in range(n):
        group.append([uniform(-5, +5), uniform(-5, +5)])

def fitness_function(x, y):
    # result = 10*number_of_individuals + x**2 - 10*cos(2*3.14*x) + y**2 - 10*cos(2*3.14*y)  # rastrigin function
    # result = x**2+y**2 # sphere function
    result = (1-x)**2+100*(y-x)**2 # rosenbrock function
    return result

def takeSecond(elem):
    return elem[2]


def selection(n):

    sum_of_fitness = 0

    for i in range(n):
        fitness_value = fitness_function(group[i][0], group[i][1])
        sum_of_fitness += fitness_value
        group[i].append(fitness_value)

    # normalization
    for j in range(n):
        group[j][2] = group[j][2]/sum_of_fitness

    # sorting
    group.sort(key=takeSecond)

    # Accumulated normalized fitness value computation and selection
    selection_value = 0.075  # at first I selected this value randomly then I tried other values anf found app. %30
    accumulated_sum = 0

    for i in range(n):
        accumulated_sum += group[i][2]
        if accumulated_sum > selection_value:
            del group[i:n]
            break
        else:
            continue
    for i in range(len(group)):  # deleting the normalization values
        del group[i][2]


def calculations():
    global length_of_group
    global number_of_missing
    global number_of_crossover
    global number_of_mutation
    length_of_group = len(group)
    number_of_missing = number_of_individuals - length_of_group
    number_of_crossover = int((number_of_missing / 2) - 1)
    number_of_mutation = number_of_missing - number_of_crossover


def crossover(n):
    for i in range(n):
        a = randint(0, length_of_group - 1)
        b = randint(0, 1)
        c = randint(0, length_of_group - 1)
        d = randint(0, 1)
        group.append([group[a][b], group[c][d]])

def mutation(n):
    for i in range(n):
        mutation_amount_x = uniform(-0.015, 0.015)
        mutation_amount_y = uniform(-0.015, 0.015)
        group.append([group[i][0] + mutation_amount_x, group[i][1] + mutation_amount_y])




# main part of code

initialization(number_of_individuals)

for i in range(number_of_iterations):
    selection(number_of_individuals)
    calculations()
    # print("# missing :", number_of_missing, " # crossover", number_of_crossover, "# mutation : ", number_of_mutation)
    crossover(number_of_crossover)
    mutation(number_of_mutation)

print("Values ", group[0])