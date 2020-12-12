import sys
import copy

with open(sys.argv[1], 'r') as fd:
    input = [int(d) for d in fd.read().split(',') if d.rstrip() != '']

OP_HALT = 99
OP_ADD  =  1
OP_MUL  =  2

class IntCodeComputer():
    def __init__(self, memory, mutations):
        self.memory = copy.deepcopy(memory)
        self.pc = 0

        for (k,v) in mutations.items():
            self.memory[k] = v

    def run(self):
        while True:
            op = self.memory[self.pc]
            if op == OP_HALT:
                return 0
            # add source, source, target
            elif op == OP_ADD:
                s1  = self.read(self.read(self.pc+1))
                s2  = self.read(self.read(self.pc+2))

                ti = self.read(self.pc + 3)
                self.write(ti, (s1 + s2))
            # mul source, source, target
            elif op == OP_MUL:
                s1  = self.read(self.read(self.pc+1))
                s2  = self.read(self.read(self.pc+2))

                ti = self.read(self.pc + 3)
                self.write(ti, (s1 * s2))
            else:
                print("fail, no opcode %d" % op)
                exit(1)


            self.pc+= 4

    def read(self, idx):
        return self.memory[idx]

    def write(self, idx, v):
        self.memory[idx] = v

from random import randint
while True:
    a = randint(0, 99)
    b = randint(0, 99)

    c = IntCodeComputer(input, {1: a, 2: b})
    c.run()

    res = c.read(0)
    if res == 19690720:
        print(100 * a + b)
        break

