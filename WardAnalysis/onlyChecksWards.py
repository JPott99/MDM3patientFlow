import importHospData as iH
import csv
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
