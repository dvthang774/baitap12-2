import random, string

tt = dict()
d = random.randint(2,6)
g = random.choice(string.ascii_lowercase)
ch = g + ''.join(random.choice(string.ascii_lowercase) for _ in range(d - 1))
tt['name'] = ch
tuoi = random.randint(1,100)
tt['age'] =tuoi
print(tt)


