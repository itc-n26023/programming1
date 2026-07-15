def func_square(*args):
    results = []
    for n in args:
        results.append(n * n)
    return results

many_numbers = list(range(100))
print(func_square(*many_numbers))
