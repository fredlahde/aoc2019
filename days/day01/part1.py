
with open("input", 'r') as fd:
    input = [int(d) for d in fd.read().split('\n') if d.rstrip() != '']


s =0
for mass in input:
    s += (mass//3)-2

print(s)

