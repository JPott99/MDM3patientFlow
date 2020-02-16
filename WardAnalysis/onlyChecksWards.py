import importHospData as iH
import csv
from matplotlib import pyplot as plt
import numpy as np
from operator import add

def makeListofStringsInt(inputtedMatrix):
    newMatrix = inputtedMatrix
    for i in range(len(inputtedMatrix)):
        newMatrix[i] = list(map(int,inputtedMatrix[i][2:]))
    return(newMatrix)

myData,myDataHeaders,sourceTransfers,sourceTransfersHeaders,targetTransfers,targetTransfersHeaders,transfers,tranfersHeadings,transProb,transProbHeaders = iH.importData()

wardData = []
medData = []
medS = []
medT = []
medB = []
surData = []
surS = []
surT = []
surB = []

for i in transfers:
    if "Ward" in i[0] or "Ward" in i[1]:
        nums = ('0','1','2','3','4','5','6','7','8','9')
        if any(s in i[0] for s in nums) or any(s in i[1] for s in nums):
            wardData.append(i)
            if "MedicalWard" in i[0] or "MedicalWard" in i[1]:
                medData.append(i)
                if "MedicalWard" in i[0] and "MedicalWard" not in i[1]:
                    medS.append(i)
                elif "MedicalWard" in i[1] and "MedicalWard" not in i[0]:
                    medT.append(i)
                else:
                    medB.append(i)
            elif "SurgicalWard" in i[0] or "SurgicalWard" in i[1]:
                surData.append(i)
                if "SurgicalWard" in i[0] or "SurgicalWard" in i[1]:
                    surData.append(i)
                    if "SurgicalWard" in i[0] and "SurgicalWard" not in i[1]:
                        surS.append(i)
                    elif "SurgicalWard" in i[1] and "SurgicalWard" not in i[0]:
                        surT.append(i)
                    else:
                        surB.append(i)

medS = sorted(medS,key=lambda x: x[1])
surS = sorted(surS,key=lambda x: x[1])

medwardS =np.array([[0]*82]*9)
for i in medwardS:
    i = np.array(i)
for i in range(len(medS)):
    if "1" in medS[i][0]:
        medwardS[0]+=np.array(list(map(int,medS[i][2:])))
    elif "2" in medS[i][0]:
        medwardS[1]+=np.array(list(map(int,medS[i][2:])))
    elif "3" in medS[i][0]:
        medwardS[2]+=np.array(list(map(int,medS[i][2:])))
    elif "4" in medS[i][0]:
        medwardS[3]+=np.array(list(map(int,medS[i][2:])))
    elif "5" in medS[i][0]:
        medwardS[4]+=np.array(list(map(int,medS[i][2:])))
    elif "6" in medS[i][0]:
        medwardS[5]+=np.array(list(map(int,medS[i][2:])))
    elif "7" in medS[i][0]:
        medwardS[6]+=np.array(list(map(int,medS[i][2:])))
    elif "8" in medS[i][0]:
        medwardS[7]+=np.array(list(map(int,medS[i][2:])))
    elif "9" in medS[i][0]:
        medwardS[8]+=np.array(list(map(int,medS[i][2:])))
medwardT =np.array([[0]*82]*9)
for i in medwardT:
    i = np.array(i)
for i in range(len(medT)):
    if "1" in medT[i][1]:
        medwardT[0]+=np.array(list(map(int,medT[i][2:])))
    elif "2" in medT[i][1]:
        medwardT[1]+=np.array(list(map(int,medT[i][2:])))
    elif "3" in medT[i][1]:
        medwardT[2]+=np.array(list(map(int,medT[i][2:])))
    elif "4" in medT[i][1]:
        medwardT[3]+=np.array(list(map(int,medT[i][2:])))
    elif "5" in medT[i][1]:
        medwardT[4]+=np.array(list(map(int,medT[i][2:])))
    elif "6" in medT[i][1]:
        medwardT[5]+=np.array(list(map(int,medT[i][2:])))
    elif "7" in medT[i][1]:
        medwardT[6]+=np.array(list(map(int,medT[i][2:])))
    elif "8" in medT[i][1]:
        medwardT[7]+=np.array(list(map(int,medT[i][2:])))
    elif "9" in medT[i][1]:
        medwardT[8]+=np.array(list(map(int,medT[i][2:])))

plt.plot(medwardS.transpose())
plt.grid()
plt.legend(["1","2","3","4","5","6","7","8","9"],loc="upper left", bbox_to_anchor=(1,1))
plt.title("Medical Wards as the Transfer Source")
plt.savefig("data/MedicalS.png")
plt.clf()
plt.figure(figsize=(10,5))
p9 = plt.bar(range(82),medwardS[8],bottom=medwardS[7])

p8 = plt.bar(range(82),medwardS[7],bottom=medwardS[6])

p7 = plt.bar(range(82),medwardS[6],bottom=medwardS[5])

p6 = plt.bar(range(82),medwardS[5],bottom=medwardS[4])

p5 = plt.bar(range(82),medwardS[4],bottom=medwardS[3])

p4 = plt.bar(range(82),medwardS[3],bottom=medwardS[2])

p3 = plt.bar(range(82),medwardS[2],bottom=medwardS[1])

p2 = plt.bar(range(82),medwardS[1],bottom=medwardS[0])

p1 = plt.bar(range(82),medwardS[0])

plt.title("Medical Wards as the Transfer Source")

plt.legend(["9","8","7","6","5","4","3","2","1"],loc="upper left", bbox_to_anchor=(1,1))

plt.savefig("data/MedicalSBar.png")
plt.clf()
plt.plot(medwardT.transpose())
plt.grid()
plt.legend(["1","2","3","4","5","6","7","8","9"],loc="upper left", bbox_to_anchor=(1,1))
plt.title("Medical Wards as the Transfer Target")
plt.savefig("data/MedicalT.png")
plt.clf()
plt.figure(figsize=(10,5))
p9 = plt.bar(range(82),medwardT[8],bottom=medwardT[7])

p8 = plt.bar(range(82),medwardT[7],bottom=medwardT[6])

p7 = plt.bar(range(82),medwardT[6],bottom=medwardT[5])

p6 = plt.bar(range(82),medwardT[5],bottom=medwardT[4])

p5 = plt.bar(range(82),medwardT[4],bottom=medwardT[3])

p4 = plt.bar(range(82),medwardT[3],bottom=medwardT[2])

p3 = plt.bar(range(82),medwardT[2],bottom=medwardT[1])

p2 = plt.bar(range(82),medwardT[1],bottom=medwardT[0])

p1 = plt.bar(range(82),medwardT[0])


plt.title("Medical Wards as the Transfer Target")
plt.legend(["9","8","7","6","5","4","3","2","1"],loc="upper left", bbox_to_anchor=(1,1))
plt.savefig("data/MedicalTBar.png")

surwardS =np.array([[0]*82]*9)
for i in surwardS:
    i = np.array(i)
for i in range(len(surS)):
    if "1" in surS[i][0]:
        surwardS[0]+=np.array(list(map(int,surS[i][2:])))
    elif "2" in surS[i][0]:
        surwardS[1]+=np.array(list(map(int,surS[i][2:])))
    elif "3" in surS[i][0]:
        surwardS[2]+=np.array(list(map(int,surS[i][2:])))
    elif "4" in surS[i][0]:
        surwardS[3]+=np.array(list(map(int,surS[i][2:])))
    elif "5" in surS[i][0]:
        surwardS[4]+=np.array(list(map(int,surS[i][2:])))
    elif "6" in surS[i][0]:
        surwardS[5]+=np.array(list(map(int,surS[i][2:])))
    elif "7" in surS[i][0]:
        surwardS[6]+=np.array(list(map(int,surS[i][2:])))
surwardT =np.array([[0]*82]*9)
for i in surwardT:
    i = np.array(i)
for i in range(len(surT)):
    if "1" in surT[i][1]:
        surwardT[0]+=np.array(list(map(int,surT[i][2:])))
    elif "2" in surT[i][1]:
        surwardT[1]+=np.array(list(map(int,surT[i][2:])))
    elif "3" in surT[i][1]:
        surwardT[2]+=np.array(list(map(int,surT[i][2:])))
    elif "4" in surT[i][1]:
        surwardT[3]+=np.array(list(map(int,surT[i][2:])))
    elif "5" in surT[i][1]:
        surwardT[4]+=np.array(list(map(int,surT[i][2:])))
    elif "6" in surT[i][1]:
        surwardT[5]+=np.array(list(map(int,surT[i][2:])))
    elif "7" in surT[i][1]:
        surwardT[6]+=np.array(list(map(int,surT[i][2:])))
plt.clf()
plt.plot(surwardS.transpose())
plt.grid()
plt.legend(["1","2","3","4","5","6","7"],loc="upper left", bbox_to_anchor=(1,1))
plt.title("Surgical Wards as the Transfer Source")
plt.savefig("data/SurgicalS.png")
plt.clf()
plt.plot(surwardT.transpose())
plt.grid()
plt.legend(["1","2","3","4","5","6","7"],loc="upper left", bbox_to_anchor=(1,1))
plt.title("Surgical Wards as the Transfer Target")
plt.savefig("data/SurgicalT.png")
plt.clf()
plt.figure(figsize=(10,5))

p7 = plt.bar(range(82),surwardS[6],bottom=surwardS[5])

p6 = plt.bar(range(82),surwardS[5],bottom=surwardS[4])

p5 = plt.bar(range(82),surwardS[4],bottom=surwardS[3])

p4 = plt.bar(range(82),surwardS[3],bottom=surwardS[2])

p3 = plt.bar(range(82),surwardS[2],bottom=surwardS[1])

p2 = plt.bar(range(82),surwardS[1],bottom=surwardS[0])

p1 = plt.bar(range(82),surwardS[0])

plt.title("Surgical Wards as the Transfer Source")

plt.legend(["7","6","5","4","3","2","1"],loc="upper left", bbox_to_anchor=(1,1))

plt.savefig("data/SurgicalSBar.png")
plt.clf()
plt.figure(figsize=(10,5))

p7 = plt.bar(range(82),surwardT[6],bottom=surwardT[5])

p6 = plt.bar(range(82),surwardT[5],bottom=surwardT[4])

p5 = plt.bar(range(82),surwardT[4],bottom=surwardT[3])

p4 = plt.bar(range(82),surwardT[3],bottom=surwardT[2])

p3 = plt.bar(range(82),surwardT[2],bottom=surwardT[1])

p2 = plt.bar(range(82),surwardT[1],bottom=surwardT[0])

p1 = plt.bar(range(82),surwardT[0])


plt.title("Surgical Wards as the Transfer Target")
plt.legend(["7","6","5","4","3","2","1"],loc="upper left", bbox_to_anchor=(1,1))
plt.savefig("data/SurgicalTBar.png")
with open("data/onlywards.csv",'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Source", "Target"]+list(range(82)))
    for i in range(len(wardData)):
        writer.writerow(wardData[i])
with open("data/onlymeds.csv",'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Source", "Target"]+list(range(82)))
    for i in range(len(medData)):
        writer.writerow(medData[i])
with open("data/onlymedssource.csv",'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Source", "Target"]+list(range(82)))
    for i in range(len(medS)):
        writer.writerow(medS[i])
with open("data/onlymedstarget.csv",'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Source", "Target"]+list(range(82)))
    for i in range(len(medT)):
        writer.writerow(medT[i])
with open("data/onlymedsboth.csv",'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Source", "Target"]+list(range(82)))
    for i in range(len(medB)):
        writer.writerow(medB[i])
with open("data/onlysurs.csv",'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Source", "Target"]+list(range(82)))
    for i in range(len(surData)):
        writer.writerow(surData[i])
with open("data/onlysurssource.csv",'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Source", "Target"]+list(range(82)))
    for i in range(len(surS)):
        writer.writerow(surS[i])
with open("data/onlysurstarget.csv",'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Source", "Target"]+list(range(82)))
    for i in range(len(surT)):
        writer.writerow(surT[i])
with open("data/onlysursboth.csv",'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Source", "Target"]+list(range(82)))
    for i in range(len(surB)):
        writer.writerow(surB[i])
