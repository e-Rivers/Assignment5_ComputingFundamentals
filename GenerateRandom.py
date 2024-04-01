import random

# Generation of randomized integer array files
for i in range(2, 7):
    randomIntegers = [random.randint(0, random.choice([10, 100, 1000, 10000])) for _ in range(10**i)]

    arrayString = ','.join(map(str, randomIntegers))

    fileName = f'randomScrambled_10to{i}.txt'
    with open(fileName, 'w') as file:
        file.write(arrayString)

# Generation of ascending integer array files
for i in range(2, 7):
    ascendingIntegers = [j for j in range(10**i)]

    arrayString = ','.join(map(str, ascendingIntegers))

    fileName = f'orderedAscending_10to{i}.txt'
    with open(fileName, 'w') as file:
        file.write(arrayString)

# Generation of descending integer array files
for i in range(2, 7):
    descendingIntegers = [j for j in range(10**i, 0, -1)]

    arrayString = ','.join(map(str, descendingIntegers))

    fileName = f'orderedDescending_10to{i}.txt'
    with open(fileName, 'w') as file:
        file.write(arrayString)
