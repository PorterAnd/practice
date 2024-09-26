def emulatecpu(cycles, instructions):
    x=0 #initial
    for instruction in instructions:
        if instruction == 0 and cycles >=1:
            x+=1
            cycles-=1
        if instruction == 1 and cycles >=2:
            x*=2
            cycles-=2
        if instruction == 2 and cycles >=3:
            x*=5
            cycles-=3
        if cycles <= 0:
            break
    return x
print(emulatecpu(7, [0,0,1,2]))
