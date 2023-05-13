def mergesort(list_):
    if len(list_) == 1:
        return list_

    midpoint = len(list_) // 2
    left = mergesort(list_[:midpoint])
    right = mergesort(list_[midpoint:])

    return merge(left, right)


def merge(left, right):
    result = []
    while left and right:
        if is_better_than(left[0], right[0]):
            result.append((left.pop(0)))
        else:
            result.append((right.pop(0)))

    if left:
        result += left
    elif right:
        result += right
    return result


def is_better_than(thing1, thing2):
    answer = input(f"Is {thing1} better than {thing2} (y/n)? ")
    while answer not in ['y', 'n']:
        answer = input(f"Answer y/n: ")
    return answer == 'y'


things = []
thing = input("Input a thing: ")
while thing:
    things.append(thing)
    thing = input("Input a thing: ")

print(mergesort(things))
