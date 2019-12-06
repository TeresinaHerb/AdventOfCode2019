file = open('input.txt', 'r')
temp = file.read().strip()
file.close()

intcode = temp.split(",")
intcode = list(map(int, intcode))
intcode[1] = 12
intcode[2] = 2
#print (intcode)
opcode = 0
while (opcode < len(intcode)-4):
    a = intcode[opcode+1]
    b = intcode[opcode+2]
    k = intcode[opcode+3]
    if (intcode[opcode] == 1):
        intcode[k] =  intcode[a] + intcode[b]
    else:
        if  (intcode[opcode] == 2):
            intcode[k] =  intcode[a] * intcode[b]
        else:
            if  (intcode[opcode] == 99):
                print (intcode[0])
                print("done")
            else:
                print("error")
    opcode += 4

#print(intcode)