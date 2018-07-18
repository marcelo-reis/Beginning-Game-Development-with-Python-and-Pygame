import random

random.seed(random.randint(1,100))

for roll in range(10):
    print(random.randint(1,6))

print('Re-seeded')
random.seed(random.randint(1,100))

for roll in range(10):
    print(random.randint(1,6))
