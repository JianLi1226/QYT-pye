import random

n = 4
sections = list()

while n > 0:
    n = n - 1
    section = random.randint(0, 255)
    sections.append(section)

print(str(sections[0]) + '.' + str(sections[1]) + '.' + str(sections[2]) + '.' + str(sections[3]))
