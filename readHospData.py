import csv
import numpy as np

if __name__ == "__main__":
    with open('pone0185912s003.csv', 'rt') as f_input:
        csv_input = csv.reader(f_input, delimiter=',')
        header = next(csv_input)
        data = list(csv_input)

    maxWeek = 0
    maxYear = 0
    minWeek = 10000
    minYear = 10000

    myData = []
    for i in range(len(data)):
        currentData = []
        currentData.append(data[i][0]+"."+data[i][1]) #Source
        # currentData.append(data[i][1]) #Site Source
        currentData.append(data[i][2]+"."+data[i][3]) #Target
        # currentData.append(data[i][3]) #Site Target
        currentData.append(int(data[i][4])) #Transfers
        currentYear = int(data[i][5]) #Year
        currentWeek = int(data[i][6]) #Week of Year
        if currentYear == 2014:
            currentWeek = currentWeek-48
        if currentYear == 2015:
            currentWeek = currentWeek+3
        if currentYear == 2016:
            currentWeek = currentWeek + 52 + 3
        currentData.append(currentWeek)
        myData.append(currentData)

    #myData form is [Source, Target, Transfers, Week]
with open("hospitalData.csv",'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Source","Target","Transfers","Week"])
    writer.writerows(myData)
Sources = []
Targets = []
for i in range(len(myData)):
    currentSource = myData[i][0]
    currentTarget = myData[i][1]
    if currentSource not in Sources:
        Sources.append(currentSource)
    if currentTarget not in Targets:
        Targets.append(currentTarget)

weeklyTransfers = [0]*82
for i in range(len(myData)):
    j = myData[i][3]
    weeklyTransfers[j]+=myData[i][2]

transferList = []
transferListLen = 0
transferListNo = []
for i in range(len(myData)):
    source = myData[i][0]
    target = myData[i][1]
    pairing = [source,target]
    week = myData[i][3]
    transferNo = myData[i][2]
    if pairing not in transferList:
        transferList.append(pairing)
        transferListLen += 1
        transferListNo.append([0]*82)
        transferListNo[transferListLen-1][week]+=transferNo
    else:
        transferListNo[transferList.index(pairing)][week]+=transferNo
with open("transfers.csv",'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Source","Target"]+list(range(82)))
    for i in range(len(transferList)):
        writer.writerow(transferList[i]+list(transferListNo[i]))

transferListNoNp = np.array(transferListNo)
sourceTransfers = np.array([np.array([0]*82)]*len(Sources))
for i in range(len(transferList)):
    source = transferList[i][0]
    j = Sources.index(source)
    sourceTransfers[j] += transferListNoNp[i]
with open("sourceTransfers.csv",'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Source"]+list(range(82)))
    for i in range(len(Sources)):
        writer.writerow([Sources[i]]+list(sourceTransfers[i]))

targetTransfers = np.array([np.array([0]*82)]*len(Targets))
for i in range(len(transferList)):
    target = transferList[i][1]
    j = Targets.index(target)
    targetTransfers[j] += transferListNoNp[i]
with open("targetTransfers.csv",'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Target"]+list(range(82)))
    for i in range(len(Targets)):
        writer.writerow([Targets[i]]+list(targetTransfers[i]))

probabilityMatrix = transferListNo
for i in range(len(transferList)):
    source = transferList[i][0]
    j = Sources.index(source)
    for k in range(82):
        if sourceTransfers[j][k]!=0:
            probabilityMatrix[i][k] = transferListNo[i][k]/sourceTransfers[j][k]

with open("transferProbability.csv",'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Source","Target"]+list(range(82)))
    for i in range(len(transferList)):
        writer.writerow(transferList[i]+list(probabilityMatrix[i]))
