import importHospData as iH
import numpy as np
import csv

myData,myDataHeaders,sourceTransfers,sourceTransfersHeaders,targetTransfers,targetTransfersHeaders,transfers,tranfersHeadings,transProb,transProbHeaders = iH.importData()

def findMeanProbs(transProb):
    noProb = []
    modelProbLink = []
    modelProbZeros = []
    for i in range(len(transProb)):
        noProb.append(np.array(list(map(float,transProb[i][2:]))))
        modelProbLink.append(transProb[i][:2])
        modelProbZeros.append(0)
        for j in noProb[i]:
            if j == 0:
                modelProbZeros[i]+=1
    modelProb = []
    for i in range(len(noProb)):
        avgDiv = 82
        modelProb.append(sum(noProb[i])/(avgDiv))

    modelProb = np.array(modelProb)

    return(modelProb,modelProbZeros,modelProbLink)

def findTotalFlowDifference(sourceTransfers,targetTransfers):
    sourceTransference = []
    for i in range(len(sourceTransfers)):
        sourceTransference.append(np.array(list(map(float,sourceTransfers[i][1:]))))

    sourceTransferenceSum = np.array(sourceTransference)
    for i in range(len(sourceTransfers)):
        sourceTransferenceSum[i] = sum(sourceTransference[i])

    targetTransference = []
    for i in range(len(targetTransfers)):
        targetTransference.append(np.array(list(map(float,targetTransfers[i][1:]))))
    targetTransferenceSum = np.array(targetTransference)
    for i in range(len(targetTransfers)):
        targetTransferenceSum[i] = sum(targetTransference[i])

    differences = []
    differenceList = []
    for i in range(len(sourceTransfers)):
        difference = -sourceTransferenceSum[i][0]
        for j in range(len(targetTransfers)):
            if sourceTransfers[i][0] == targetTransfers[j][0]:
                difference+=targetTransferenceSum[j][0]
                differenceList.append(list(np.array(targetTransference[j])-np.array(sourceTransference[i])))
        if difference!=-sourceTransference[i][0]:
            differences.append([sourceTransfers[i][0],difference])
    return(differences, differenceList)

differences, differenceList = findTotalFlowDifference(sourceTransfers,targetTransfers)
with open("data/flowDifferences.csv",'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Location","Difference","Difference List"])
    for i in range(len(differences)):
        writer.writerow(differences[i]+differenceList[i])

modelProb,modelProbZeros,modelProbLink = findMeanProbs(transProb)

with open("data/modelProbabalities.csv",'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Source","Target","Probability","Number of Zero", "Total Prob"])
    for i in range(len(modelProb)):
        writer.writerow(modelProbLink[i]+[modelProb[i],modelProbZeros[i],modelProb[i]/((1-modelProbZeros[i]/82))])
