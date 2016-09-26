#求平方的和
def calc_my(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
