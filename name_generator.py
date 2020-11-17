import sys
from faker import Faker

fake = Faker()

n = sys.argv[1]

for i in range(int(n)):
    print(fake.name())

