
def square_root(a):
    x = a
    prev = x
    while True:
        x = (x + a/x)*0.5
        if abs(prev - x ) <1e-10:
            return x
        prev = x


if __name__ == "__main__":
   print(square_root(10))
   print(square_root(100))
   print(square_root(1000))