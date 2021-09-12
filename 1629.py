'''
모듈러 성질 : (a * b) mod c = (a mod c * b mod c) mod c
'''

def pow1(base, exponent):
  if exponent == 1:
    return base

  else:
    half = pow(base, exponent // 2)

    if exponent % 2 == 1: 
      return half * half * base
    else:  
      return half * half


a, b, c = map(int, input().split())

print(pow(a, b))

