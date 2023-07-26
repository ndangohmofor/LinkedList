def count_down(value):
    if value <= 0:
        print("Done...")
        return

    print(value)
    count_down(value - 1)
    return


count_down(10)


def sum_list(lst):
    if len(lst) == 0:
        return 0
    #
    # if len(lst) == 1:
    #     return lst[0]

    return lst[0] + sum_list(lst[1:])


print(sum_list([2, 4, 6, 8, 10]))


def factorial(num):
    if num == 1:
        return num
    return num * factorial(num - 1)


print("Factorial: ", factorial(10))
