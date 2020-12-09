def iq_test(numbers):
    numbers = numbers.split(' ')
    booleans = []
    num_list = [int(i) for i in numbers]
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            booleans.append(True)
        if num_list[i] % 2 != 0:
            booleans.append(False)
    res = list(filter(lambda n: booleans.count(n) == 1, booleans))
    index = booleans.index(res[0]) + 1
    return index
