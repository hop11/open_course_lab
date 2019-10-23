import math
import random

def f(x):
  """ function for pollard's rho """
  return x**2 + 1

def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b);

def pollard_rho1(n):
  x_i = 2
  y_i = 2
  c = random.randint(2, n)

  while True:
    x_i = f(x_i, c, n)
    y_i = f(f(y_i, c, n), c, n)
    gcd_check = gcd(abs(x_i - y_i), n)

    if gcd_check == n:
      print("finding factor failed, try different x_i, y_i, c or f(x) function")
    elif gcd_check == 1:
      continue
    else:
      print(f"one factor is: {gcd_check}")
      break

def pollard_rho2(n):
  i = 1
  x = random.randint(0, n - 1)
  y = x
  k = 2

  while True:
    i = i + 1
    x = (x * x - 1) % n
    d = gcd(y - x, n)

    if d != 1 and d != n:
      return d

    if i == k:
      y = x
      k = 2*k

def brent(N):
    if N % 2 == 0:
        return 2
    y, c, m = random.randint(1, N - 1), random.randint(1, N - 1), random.randint(1, N - 1)
    g, r, q = 1, 1, 1
    while g == 1:
        x = y
        for i in range(r):
            y = ((y * y) % N + c) % N
        k = 0
        while k < r and g == 1:
            ys = y
            for i in range(min(m, r - k)):
                y = ((y * y) % N + c) % N
                q = q * (abs(x - y)) % N
            g = gcd(q, N)
            k = k + m
        r *= 2
    if g == N:
        while True:
            ys = ((ys * ys) % N + c) % N
            g = gcd(abs(x - ys), N)
            if g > 1:
                break

    return g

def main():
  print(gcd(-6,3))

if __name__ == "__main__":
  main()