def even(n):
    if n%2==0:
        return True
    else:
        return False

for i in range(50):
    if even(i):
        print(f"{i} is even")
    else:
        print(f"{i} is odd")