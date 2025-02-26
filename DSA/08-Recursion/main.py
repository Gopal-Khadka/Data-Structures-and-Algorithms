# Read concepts of: recursion, call stack of normal and recursive function


def fact(n):
    # factorial using recursion
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


def loop_fact(n):
    # factorial using loop
    result = 1
    for i in range(n, 1, -1):
        result *= i
    return result


def fibo(n):
    # fibonacci using recursion
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


def loop_fibo(n):
    # fibonacci using loop
    items = [0, 1]
    for _ in range(2, n):
        items.append(items[-1] + items[-2])  # add last and second-to-last item
    return items


def print_fibo_nums(num: int):
    for i in range(num):
        print(fibo(i), end=", " if i != num - 1 else "")
    print()

    print("Using loop:", loop_fibo(num))


# print(fact(5))
# print(loop_fact(5))

print_fibo_nums(10)
