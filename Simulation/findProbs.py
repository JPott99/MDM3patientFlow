import importHospData as iH
import numpy as np
import csv

def findMeanProbs(data):
    # Takes the transferProbability found in readHospData and assigns a single
    # value weight to each transder.
    myData,myDataHeaders,sourceTransfers,sourceTransfersHeaders,targetTransfers,targetTransfersHeaders,transfers,tranfersHeadings,transProb,transProbHeaders = data
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
        avgDiv = 82 #The number of data points in the data (weeks)
        modelProb.append(sum(noProb[i])/(avgDiv))

    modelProb = np.array(modelProb)
    output = []
    for i in range(len(modelProb)):
        # outputs a list showing the transfer and probability weighting,
        # calulated by taking the mean of the rates per source-target pair
        # and calculating P(transfer|not zero), where not zero is the rate of
        # weeks where a transfer occurs.
        output.append(modelProbLink[i]+[modelProb[i]/((1-modelProbZeros[i]/82))])
    return([x for x in output if x != [0.0]])

if __name__=="__main__":
    output = findMeanProbs(iH.importData())

    with open("data/modelProbabalities.csv",'w') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(["Source","Target","Total Prob"])
        writer.writerows(output)
