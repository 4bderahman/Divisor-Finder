x = int(input("Please enter an integer x : "))

count = 0

print(f"The divisors of {x} are:")

for i in range(1, x + 1):
    if x % i == 0:
        print(i)
        count += 1

print(f"Total number of divisors: {count}")
