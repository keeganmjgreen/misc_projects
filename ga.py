import random
import itertools
random.seed(1)
f = lambda x: - x ** 2 + 8 * x + 15
lb = 0
ub = 25
nP = 4
num_decimals = 0
dec_base = 10
def float2bin(my_float, offset = 0):
    my_int = round((my_float) * dec_base ** num_decimals) + offset
    my_bin = bin(my_int).replace('0b', '')
    return my_bin
def bin2float(my_bin, offset = 0):
    my_int = int(my_bin, base = 2)
    my_float = round((my_int - offset) / (dec_base ** num_decimals), num_decimals)
    return my_float
chromosome_len = len(float2bin(max(abs(lb), abs(ub)))) + 1
offset = 2 ** (chromosome_len - 1)
x = [round(random.uniform(lb, ub), num_decimals) for i in range(0, nP)]
# print('x =', x)
P_c = 0.60
P_m = 0.01
for j in range(0, 10):
    y = list(map(f, x))
    # print('y =', y)
    y, x = map(list, zip(*sorted(zip(y, x))))
    # print('sorted(x) =', x)
    # print('sorted(y) =', y)
    FV = [410 + y_i for y_i in y]
    # print('FV =', FV)
    mating_pool = random.choices(x, weights = FV, k = nP)
    # print('mating_pool =', mating_pool)
    couples = []
    parents = []
    while len(couples) != nP / 2:
        for candidate_parent in mating_pool:
            if random.random() < P_c:
                parents.append(candidate_parent)
                if len(parents) == 2:
                    couples.append(parents)
                    if len(couples) == nP / 2:
                        break
                    parents = []
    del parents
    # print('couples =', couples)
    children_bin = []
    for couple in couples:
        parents_bin, siblings_bin = [], []
        for parent in couple:
            parents_bin.append(float2bin(parent, offset).zfill(chromosome_len))
        r = random.randrange(1, chromosome_len - 1)
        # print('r =', r)
        siblings_bin.append(parents_bin[0][:r] + parents_bin[1][r:])
        siblings_bin.append(parents_bin[1][:r] + parents_bin[0][r:])
        children_bin.append(siblings_bin)
    children_bin = list(itertools.chain(*children_bin))
    del parents_bin, siblings_bin, r
    # print('children_bin = ', children_bin)
    mutants_bin = []
    for child_bin in children_bin:
        mutant_bin = []
        for bit in child_bin:
            if random.random() < P_m:
                mutant_bin.append(str(int(not(int(bit)))))
            else:
                mutant_bin.append(bit)
        mutants_bin.append(''.join(mutant_bin))
    del mutant_bin
    # print('mutants_bin =', mutants_bin)
    x = []
    for mutant_bin in mutants_bin:
        x.append(bin2float(mutant_bin, offset))
    print('new x =', x)
