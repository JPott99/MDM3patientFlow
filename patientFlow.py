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
        avgDiv = len(noProb[i])-modelProbZeros[i]
        modelProb.append(sum(noProb[i])/(avgDiv*2))

    modelProb = np.array(modelProb)

    return(modelProb,modelProbZeros,modelProbLink)

def findTotalFlowDifference(sourceTransfers,targetTransfers):
    sourceTransference = []
    for i in range(len(sourceTransfers)):
        sourceTransference.append(np.array(list(map(float,sourceTransfers[i][1:]))))

    sourceTransference = np.array(sourceTransference)
    for i in range(len(sourceTransfers)):
        sourceTransference[i] = sum(sourceTransference[i])

    targetTransference = []
    for i in range(len(targetTransfers)):
        targetTransference.append(np.array(list(map(float,targetTransfers[i][1:]))))
    targetTransference = np.array(targetTransference)
    for i in range(len(targetTransfers)):
        targetTransference[i] = sum(targetTransference[i])

    differences = []
    for i in range(len(sourceTransfers)):
        difference = -sourceTransference[i][0]
        for j in range(len(targetTransfers)):
            if sourceTransfers[i][0] == targetTransfers[j][0]:
                difference+=targetTransference[j][0]
        if difference!=-sourceTransference[i][0]:
            differences.append([sourceTransfers[i][0],difference])
    return(differences)

differences = findTotalFlowDifference(sourceTransfers,targetTransfers)
with open("flowDifferences.csv",'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Location","Difference"])
    writer.writerows(differences)

modelProb,modelProbZeros,modelProbLink = findMeanProbs(transProb)

with open("modelProbabalities.csv",'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Source","Target","Probability","Rate of Zero", "Total Prob"])
    for i in range(len(modelProb)):
        writer.writerow(modelProbLink[i]+[modelProb[i],modelProbZeros[i]/82,modelProb[i]*(1-modelProbZeros[i]/82)])
