import importHospData as iH
import numpy as np
import csv

myData,myDataHeaders,sourceTransfers,sourceTransfersHeaders,targetTransfers,targetTransfersHeaders,transfers,tranfersHeadings,transProb,transProbHeaders = iH.importData()

def findMeanProbs(transProb):
    noProb = []
    modelProbLink = []

    for i in range(len(transProb)):
        noProb.append(np.array(list(map(float,transProb[i][2:]))))
        modelProbLink.append(transProb[i][:2])

    avgDiv = len(noProb[0])
    modelProb = []
    for i in range(len(noProb)):
        modelProb.append(sum(noProb[i])/avgDiv)

    modelProb = np.array(modelProb)

    return(modelProb, modelProbLink)

modelProb,modelProbLink = findMeanProbs(transProb)
with open("modelProbabalities.csv",'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Source","Target","Probability"])
    for i in range(len(modelProb)):
        writer.writerow(modelProbLink[i]+[modelProb[i]])
