from z3 import *


def check(vars):
    for i in range(0,26):
        if (vars[i] ^ vars[(i+1)%26] ^ vars[(i+2)%26] ^ vars[(i+3)%26] ^ vars[(i+4)%26] ^ vars[(i+5)%26] != keys[i]):
            return False
    return True

keys = [ 0x62, 0x75, 0x4E, 0x77, 0x1F, 0x61, 0x0F, 0x2C, 0x08, 0x25, 0x39, 0x3B, 0x01, 0x65, 0x65, 0x55, 0x13, 0x5A, 0x6B, 0x34, 0x03, 0x46 ]
vars = []
s = Solver()

for i in range(0, len(keys)):
    vars.append(BitVec(str(i),7))

s.add(vars[0] ^ vars[6] ^ vars[0xc] ^ vars[0x11] == 0x62) #done
s.add(vars[0x12] ^ vars[1] ^ vars[4] ^ vars[5] ^ vars[0xb] ^ vars[0xc] ^ vars[0xf] == 0x75) #done
s.add(vars[0x15] ^ vars[3] ^ vars[6] ^ vars[8] ^ vars[10] ^ vars[0xb] ^ vars[0xc] ^ vars[0xd] ^ vars[0xf] ^ vars[0x10] ^ vars[0x11] ^ vars[0x12] ^ vars[0x13] == 0x4E) #done
s.add(vars[0x12] ^ vars[0] ^ vars[5] ^ vars[0xc] ^ vars[0xe] ^ vars[0xf] ^ vars[0x11] == 0x77) #done
s.add(vars[0x15] ^ vars[0] ^ vars[3] ^ vars[5] ^ vars[6] ^ vars[8] ^ vars[0xb] ^ vars[0xd] ^ vars[0xe] ^ vars[0xf] ^ vars[0x10] ^ vars[0x13] == 0x1F) #done
s.add(vars[0x15] ^ vars[0] ^ vars[1] ^ vars[2] ^ vars[4] ^ vars[6] ^ vars[7] ^ vars[8] ^ vars[0xb] ^ vars[0xc] ^ vars[0xe] ^ vars[0xf] ^ vars[0x14] == 0x61) #done
s.add(vars[0x15] ^ vars[0] ^ vars[1] ^ vars[2] ^ vars[4] ^ vars[6] ^ vars[7] ^ vars[8] ^ vars[0xb] ^ vars[0xc] ^ vars[0xd] ^ vars[0xe] ^ vars[0xf] ^ vars[0x14] == 0x0F) #done
s.add(vars[0x15] ^ vars[4] ^ vars[5] ^ vars[8] ^ vars[10] ^ vars[0xb] ^ vars[0xe] ^ vars[0x11] == 0x2C) #done
s.add(vars[0x15] ^ vars[0] ^ vars[3] ^ vars[4] ^ vars[5] ^ vars[6] ^ vars[8] ^ vars[0xb] ^ vars[0xd] ^ vars[0xe] ^ vars[0xf] ^ vars[0x10] ^ vars[0x12] ^ vars[0x13] == 0x08) #done
s.add(vars[0x11] ^ vars[1] ^ vars[5] ^ vars[9] ^ vars[0xc] == 0x25) #done
s.add(vars[0x15] ^ vars[0] ^ vars[1] ^ vars[2] ^ vars[3] ^ vars[4] ^ vars[5] ^ vars[6] ^ vars[7] ^ vars[0xb] ^ vars[0xe] ^ vars[0x10] ^ vars[0x12] == 0x39) #done
s.add(vars[0x15] ^ vars[0] ^ vars[3] ^ vars[4] ^ vars[9] ^ vars[10] ^ vars[0xb] ^ vars[0xc] ^ vars[0xd] ^ vars[0xe] ^ vars[0x10] ^ vars[0x11] ^ vars[0x12] ^ vars[0x13] == 0x3B) #done
s.add(vars[0x12] ^ vars[0] ^ vars[7] ^ vars[9] ^ vars[10] ^ vars[0xb] ^ vars[0xc] ^ vars[0xd] ^ vars[0xe] ^ vars[0xf] ^ vars[0x10] ^ vars[0x11] == 0x01) #done
s.add(vars[0x14] ^ vars[0] ^ vars[2] ^ vars[4] ^ vars[5] ^ vars[8] ^ vars[9] ^ vars[0xc] ^ vars[0xe] ^ vars[0xf] ^ vars[0x10] == 0x65) #done
s.add(vars[8] ^ vars[0] == 0x65) #done
s.add(vars[0x15] ^ vars[7] ^ vars[8] ^ vars[0xb] ^ vars[0xd] ^ vars[0xe] ^ vars[0x10] ^ vars[0x12] == 0x55) #done
s.add(vars[0x15] ^ vars[0] ^ vars[5] ^ vars[0xc] ^ vars[0xe] ^ vars[0xf] ^ vars[0x11] ^ vars[0x12] == 0x13) #done
s.add(vars[0x10] ^ vars[4] ^ vars[8] ^ vars[10] ^ vars[0xc] ^ vars[0xd] ^ vars[0xe] == 0x5A) # done
s.add(vars[0x15] ^ vars[0] ^ vars[1] ^ vars[5] ^ vars[6] ^ vars[7] ^ vars[8] ^ vars[9] ^ vars[0xb] ^ vars[0xd] ^ vars[0xe] ^ vars[0x10] == 0x6B) #done
s.add(vars[0x10] ^ vars[0] ^ vars[1] ^ vars[3] ^ vars[4] ^ vars[5] ^ vars[7] ^ vars[8] ^ vars[9] ^ vars[0xb] ^ vars[0xf] == 0x34) #dopne
s.add(vars[0x14] ^ vars[1] ^ vars[2] ^ vars[4] ^ vars[6] ^ vars[7] ^ vars[8] ^ vars[9] ^ vars[10] ^ vars[0xb] ^ vars[0xc] ^ vars[0xe] == 0x03) #done
s.add(vars[0x15] ^ vars[0] ^ vars[2] ^ vars[5] ^ vars[7] ^ vars[8] ^ vars[9] ^ vars[10] ^ vars[0xb] ^ vars[0xd] ^ vars[0xe] ^ vars[0xf] ^ vars[0x12] ^ vars[0x14] == 0x46) #done


print(s.check())
print(s.model())