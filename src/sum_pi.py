""" SICP for Python """


def sum_pi(num):
    """
    get Pi by adding fracs
    ex)
    8 / 1 * 3 + 8 / 5 * 7 + 8 / 9 * 11 + ...
    """
    total, k = 0, 1
    while k <= num:
        total += 8 / ((4 * k - 3) * (4 * k - 1))
        k += 1
    return total


if __name__ == '__main__':
    num = int(input())
    print(sum_pi(num))

    # print(sum_pi(1000000))
    # input 100,000: 3.141587653589818
    # input 1,000,000: 3.141592153589902
