filepath = "valaszok.txt"
fileobject = open(filepath, "r+")



max_length = 0
names = ""
x = 0
correct = "BCCCDBBBBCDAAA"
first = "BXCDBBACACADBC"



print("Adjon meg egy azonosítót: ");
id = str(input())
id = id.upper()
indexOfid = 0
cont = False



wn = 0
h = 0
reh = 0
indexOfwn = 0

for line in fileobject:
    reh=0

    if(correct[0] == line[0]):
        reh= reh + 3

    if (correct[1] == line[1]):
        reh = reh + 3

    if (correct[2] == line[2]):
        reh = reh + 3

    if (correct[3] == line[3]):
        reh = reh + 3

    if (correct[4] == line[4]):
        reh = reh + 3


    if (correct[5] == line[5]):
        reh = reh + 4

    if (correct[6] == line[6]):
        reh = reh + 4

    if (correct[7] == line[7]):
        reh = reh + 4

    if (correct[8] == line[8]):
        reh = reh + 4

    if (correct[9] == line[9]):
        reh = reh + 4

    if (correct[10] == line[10]):
        reh = reh + 4


    if (correct[11] == line[11]):
        reh = reh + 5

    if (correct[12] == line[12]):
        reh = reh + 5



    if (correct[13] == line[13]):
        reh = reh + 5


        if(reh > h):
            h = reh
            wn = reh
            indexOfwn = names




    x= x + 1
    if len(line) > max_length:
        names = line
        max_length = len(line)



    if(id == line[0:5]):
            cont = True
            indexOfid = line[6:20]


x= x - 1

#2. Feladat
print("2.Feladat: A versenyen ", x, "versenyző indult ")



#3. Feladat
print("3.Feladat: ")

if(cont == True):
    print("A megadott azonosítójú versenyző válaszai: ")
    print(indexOfid)
else:
    print("Nincs ilyen azonosítójú versenyző")


#4. Feladat
print("4.Feladat: A jó megoldás ", "\n", correct )


if (cont == True):

    if (correct[0] == indexOfid[0]):
        print("+", end = " ")
    else:
        print(" ", end = " ")

    if (correct[1] == indexOfid[1]):
        print("+", end=" ")
    else:
        print(" ", end=" ")

    if (correct[2] == indexOfid[2]):
        print("+", end=" ")
    else:
        print(" ", end=" ")

    if (correct[3] == indexOfid[3]):
        print("+", end=" ")
    else:
        print(" ", end=" ")

    if (correct[4] == indexOfid[4]):
        print("+", end=" ")
    else:
        print(" ", end=" ")

    if (correct[5] == indexOfid[5]):
        print("+", end=" ")

    else:
        print(" ", end=" ")
    if (correct[6] == indexOfid[6]):
        print("+", end=" ")

    else:
        print(" ", end=" ")

    if (correct[7] == indexOfid[7]):
        print("+", end=" ")
    else:
        print(" ", end=" ")

    if (correct[8] == indexOfid[8]):
        print("+", end=" ")
    else:
        print(" ", end=" ")

    if (correct[9] == indexOfid[9]):
        print("+", end=" ")
    else:
        print(" ", end=" ")

    if (correct[10] == indexOfid[10]):
        print("+", end=" ")
    else:
        print(" ", end=" ")

    if (correct[11] == indexOfid[11]):
        print("+", end=" ")
    else:
        print(" ", end=" ")

    if (correct[12] == indexOfid[12]):
        print("+", end=" ")
    else:
        print(" ", end=" ")

    if (correct[13] == indexOfid[13]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
else:

    if (correct[0] == first[0]):
        print("+", end=" ")
    else:
        print(" ", end=" ")

    if (correct[1] == first[1]):
        print("+", end=" ")
    else:
        print(" ", end=" ")

    if (correct[2] == first[2]):
        print("+", end=" ")
    else:
        print(" ", end=" ")

    if (correct[3] == first[3]):
        print("+", end=" ")
    else:
        print(" ", end=" ")

    if (correct[4] == first[4]):
        print