import importHospData as iH
import numpy as np
import csv

def findMeanProbs(data):
    # Takes the transferProbability found in readHospData and assigns a single
    # value weight to each transfer.
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

def findSeasonalProbs(data):
    myData,myDataHeaders,sourceTransfers,sourceTransfersHeaders,targetTransfers,targetTransfersHeaders,transfers,tranfersHeadings,transProb,transProbHeaders = data
    noProb = []
    modelProbLink = []
    modelProbZeros = []
    modelProbSeasonSizes = []
    modelProbSeason =[]
    for i in range(len(transProb)):
        noProb.append(np.array(list(map(float,transProb[i][2:]))))
        modelProbLink.append(transProb[i][:2])
        modelProbZeros.append([0,0,0,0])
        modelProbSeasonSizes.append([0,0,0,0])
        modelProbSeason.append([0,0,0,0])
        for j in range(len(noProb[i])):
            if j<2 or (j>=42 and j<55):
                # Autumn
                modelProbSeasonSizes[i][0]+=1
                if noProb[i][j] == 0:
                    modelProbZeros[i][0]+=1
                else:
                    modelProbSeason[i][0]+=noProb[i][j]
            elif (j>=2 and j<15) or (j>=55 and j < 68):
                # Winter
                modelProbSeasonSizes[i][1]+=1
                if noProb[i][j] == 0:
                    modelProbZeros[i][1]+=1
                else:
                    modelProbSeason[i][1]+=noProb[i][j]
            elif (j>=15 and j<28) or (j>=68 and j < 81):
                # Spring
                modelProbSeasonSizes[i][2]+=1
                if noProb[i][j] == 0:
                    modelProbZeros[i][2]+=1
                else:
                    modelProbSeason[i][2]+=noProb[i][j]
            elif (j>=28 and j<41) or (j>=81):
                # Summer
                modelProbSeasonSizes[i][3]+=1
                if noProb[i][j] == 0:
                    modelProbZeros[i][3]+=1
                else:
                    modelProbSeason[i][3]+=noProb[i][j]
    modelProb =[]
    for i in range(len(modelProbSeason)):
        modelProb.append([0,0,0,0])
        for j in range(len(modelProb[i])):
            modelProb[i][j] = modelProbSeason[i][j]/modelProbSeasonSizes[i][j]
            if (modelProbZeros[i][j]!=modelProbSeasonSizes[i][j]):
                modelProb[i][j] = modelProb[i][j]/(1-modelProbZeros[i][j]/modelProbSeasonSizes[i][j])
    output = []
    for i in range(len(modelProb)):
        output.append(modelProbLink[i]+modelProb[i])
    return([x for x in output if x != [0.0]])

if __name__=="__main__":
    output = findSeasonalProbs(iH.importData())

    with open("data/modelProbabalities.csv",'w') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(["Source","Target","Total Prob"])
        writer.writerows(output)
