# bounce.py
#
# Exercise 1.5

height = 100
bounce = 3/5
count = 1

while count <= 10:
    height = height * bounce
    print(f"{count} : {height:.4f}")
    count += 1
