#lab 10  
def consecutive_numbers(filename,n):
    #sig: str,int -> NoneType
    f = open(filename,"w")
    for number in range (1,n+1):
        f.write(str(number)+"\n")
    f.close()


def squared_numbers(filename, outFile):
    #sig: str,str -> nonetype
    myFile= open(filename,"r")
    writeFile = open(outFile,"w")
    for line in myFile:
        line = int(line.strip())
        writeFile.write(str(line**2)+"\n")
    myFile.close()
    writeFile.close()
import copy
def create_world():
    myFile= open("initial_world.txt","r")
    world = []
    world.append(["-"]*12)
    for line in myFile:
        line = line.strip().split()
        world.append(["-"]+line+["-"])
    world.append(["-"]*12)
    myFile.close()
    return world

def gen(world):
    temp = copy.deepcopy(world)
    for row in range(1,11):
        for col in range(1,11):
            count = 0
            for i in range(-1,2):
                for j in range (-1,2):
                    if temp[i][j] == "*"
                    count+=1
    if temp[row][col] == "*":
        count-=1
    if temp[row][col] == "*":
        if count not in [2,3]:
            temp[row][col] = "-"
    else:
        if count==3:
            temp[row][col] ="*"
    return temp

def display(world):
    for row in(1,11):
        for col in (1,11):
            print(world[row][col],end = " ")
        print()
            
            
def main():
    world = create_world()
    for i in range (11):
        print("generation",i)
        display(world)
        world = gen(world)

