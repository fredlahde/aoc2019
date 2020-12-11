
with open("input", 'r') as fd:
    input = [int(d) for d in fd.read().split('\n') if d.rstrip() != '']


s =0
for mass in input:
    m = (mass//3)-2
    fuel = (m//3)-2
    fs = 0
    
    while fuel > 0:
        fs += fuel
        fuel = (fuel//3)-2
    s += (m+fs)

print(s)

