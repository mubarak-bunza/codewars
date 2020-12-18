
def shifted_diff(first, second):
    if first == "  ":
        return -1
    first, second = list(first), list(second)
    rotate = 0
    for i in range(len(first)-1):
        if first == second:
            return rotate
        elif first != second:
            rotate += 1
            le = first.pop()
            first.insert(0,le)
            print(''.join(second))
            print(''.join(first),rotate)
    if first[0] is not second[0] or first[-1] is not second[-1]:
        return -1
    return rotate