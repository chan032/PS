'''
모듈러 성질 : (a * b) mod c = (a mod c * b mod c) mod c
'''

a, b, c = map(int, input().split())


def pow(base, exponent):
    if exponent == 1:
        return base
    else:
        half = exponent // 2
        halfPow = pow(base, half)

        if exponent % 2 == 0:  # even
            return (halfPow % c) * (halfPow % c) 
        else:  # odd
            return (halfPow % c) * (halfPow % c) * base

print(pow(a, b)%c)


