from itertools import permutations
import time
import inspect

___XOR___ = lambda x, y: x ^ y
___AND___ = lambda x, y: x & y
___OR____ = lambda x, y: x | y
___NOT___ = lambda x: 1 - x
NO_CHANGE = lambda x: x
NOT__USED = lambda x, y: x

OPS = [___XOR___, ___AND___, ___OR____, NOT__USED]
signs = [NO_CHANGE, ___NOT___,]

names = {"NO_CHANGE" : "", "___XOR___" : "^", "___AND___" : "&", "___OR____" : "|", "___NOT___" : "~",
         "NOT__USED" : "NOT__USED" }

# finds all the permutations of possible arrangements of bits and functions and signs
def findPerms(nibble):
    nibbleList = [(int(nibble[i]), i) for i in range(len(nibble))]
    permList = [(sign, bit) for sign in signs for bit in nibbleList]
    permList = list(permutations(permList))

    result = []
    for permutation in permList:  # permutation is list of tuples with signs and bits,
        used = []  # list that checks for duplicates
        temp = []  # list that contains the permutation to be added
        for item in permutation:  # item is tuple with sign and bit
            if item[1] not in used:
                temp.append(item)
                used.append(item[1])
        if temp not in result:
            result.append(temp)
    return result

# evaluates the expression given
def evaluate(expression):  # expression is an alternating list of tuples and functions:
    # [(sign, (bit, index), function, .....)]
    result = expression[0][0](expression[0][1][0])
    index = 1
    while index < len(expression):
        sign = expression[index + 1][0]
        bit = sign(expression[index + 1][1][0])

        result = expression[index](result, bit)
        index += 2
    return result

# finds the operations that make the permutations true
def findOps(perm, answer):
    sols = []
    def helper(perm, answer, curr):
        if len(perm) == 1:
            if evaluate(curr + [perm[0]]) == answer:
                sols.append(curr + [perm[0]])
            return
        for op in OPS:
            helper(perm[1:], answer, curr + [perm[0], op])
    helper(perm, answer, [])
    return sols

def applyAll(solutions, answers, nibbles):
    for nibble_index in range(len(nibbles)):
        sol_number = 0
        while sol_number < len(solutions):
            sol = list(solutions[sol_number])
            for i in range(len(sol)):
                if type(sol[i]) == type(()):
                    index = sol[i][1][1]
                    new_bit = (int(nibbles[nibble_index][index]), index)
                    sol[i] = (sol[i][0], new_bit)
            if evaluate(sol) != answers[nibble_index]:
                solutions.pop(sol_number)
            else:
                sol_number += 1
    return solutions



def printSol(solution):
    sol_to_print = []
    for item in solution:

        if type(item) == type(___AND___):
            sol_to_print.append(names[inspect.getsource(item)[:9]])
        elif type(item) == type(()):
            sol_to_print.extend([names[inspect.getsource(item[0])[:9]], "index %s" % item[1][1]])

        else:
            sol_to_print.append(item)
    stringsol = ""

    i = 0
    while i < len(sol_to_print):
        if sol_to_print[i] != "NOT__USED":
            stringsol += " "
            stringsol += sol_to_print[i]
            i += 1
        else:
            i += 3
    return stringsol

def solver(nibbles, keys):
    nibble1 = nibbles[0]
    key1 = keys[0]
    nibbles = nibbles[1:]
    keys = keys[1:]

    print("----------------------------------------------")

    start_time = time.time()

    p = findPerms(nibble1)

    operation_time = time.time()

    print("findPerms takes  %s seconds" % (operation_time - start_time))

    ans = []
    for perm in p:
        ans.extend(findOps(perm, key1))
    ans = [i for i in ans if i is not None]

    function_time = time.time()

    print("findOps takes    %s seconds" % (function_time - operation_time))

    sols = applyAll(ans, keys, nibbles)
    print("applyAll takes   %s seconds" % (time.time() - function_time))
    print("TOTAL TIME:      %s seconds" % (time.time() - start_time))
    print()
    print("TOTAL SOLUTIONS: %s solutions" % len(sols))
    try:
        if len(sols) > 10:
            print("FIRST SOLUTION: ", printSol(sols[1]))
        else:
            for i in range(len(sols)):
                print("SOLUTION " + str(i) + ":", printSol(sols[i]))
        print("----------------------------------------------")

    except IndexError:
        print("----------------------------------------------")

# solver(["1011", "1010", "1001", "1111"],[1, 1, 0, 1])