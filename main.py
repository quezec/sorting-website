import math


def sorting_number(n):
    s_n = math.floor(math.log(n, 2) + 1)
    return n * s_n - 2 ** s_n + 1


def mergesort(list_):
    print(f"\nMaximum number of comparisons: {sorting_number(len(list_))}")
    width = 1
    n_comps = 0

    while width <= len(list_):
        width *= 2
        for low in range(0, len(list_), width):
            high = low + width
            mid = (low + high) // 2
            list_[low:high], n_comps = merge(list_[low:mid],
                                             list_[mid:high],
                                             n_comps)

    return list_


def merge(left, right, n_comps):
    result = []
    while left and right:
        n_comps += 1
        if is_better_than(left[0], right[0], n_comps):
            result.append((left.pop(0)))
        else:
            result.append((right.pop(0)))

    if left:
        result += left
    elif right:
        result += right
    return result, n_comps


def is_better_than(thing1, thing2, n_comps):
    answer = input(f"{n_comps}: Is {thing1} better than {thing2} (y/n)? ")
    while answer not in ['y', 'n']:
        answer = input(f"Answer y/n: ")
    return answer == 'y'


things = []
thing = input("Input a thing: ")
while thing:
    things.append(thing)
    thing = input("Input a thing: ")

print(mergesort(things))
