def f(n):
    if n<3:
      return n-1
    else:
      return f(n-2) + f(n-1)


print(f(10))