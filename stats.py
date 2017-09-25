#!/usr/bin/python

f = open("ether.log", "r")
raw = f.read()
f.close()

shares = []
amounts = []

for line in raw.split("\n"):
    fields = line.split()
    if len(fields)>0:
        amounts.append(float(fields[-1]))
        shares.append(float(fields[-3]))

print(sum(amounts[-25:-1]))
print(24*sum(amounts)/len(amounts))
