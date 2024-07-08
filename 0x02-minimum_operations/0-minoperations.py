#!/usr/bin/python3
def minOperations(n):
    """
    func to get few # of operations needed to result in n H chars
    """
    if n < 2:
        return 0

    total_ops = 0

    # Iterate over possible divisors from 2 to n
    for divisor in range(2, n + 1):
        # Repeatedly divide n by the current divisor
        while n % divisor == 0:
            total_ops = total_ops + divisor
            n //= divisor
    return total_ops
