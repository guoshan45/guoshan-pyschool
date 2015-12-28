# 遍历N能否能被从2到sqrt(N)之间的素数整除。若不能则为素数。
# Hint: Step through the range between (2, number-1),
# and determine if the number is divisible using the modulus operator.


def isPrime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    if x <= 0:
        return False
    return True
