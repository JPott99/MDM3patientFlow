import importHospData as iH
import numpy as np

def getInputs():
    myData,myDataHeaders,sourceTransfers,sourceTransfersHeaders,targetTransfers,targetTransfersHeaders,transfers,tranfersHeaders,transProb,transProbHeaders=iH.importData()
    sourceNum = np.array(sourceTransfers)[:,1:]
    sourceNums = []
    for i in range(len(sourceNum)):
        sourceNums.append(list(map(int,sourceNum[i])))
    targetNum = np.array(targetTransfers)[:,1:]
    targetNums = []
    for i in range(len(targetNum)):
        targetNums.append(list(map(int,targetNum[i])))


    output = []
    for i in range(len(sourceTransfers)):
        source = sourceTransfers[i][0]
        for j in range(len(targetTransfers)):
            target = targetTransfers[j][0]
            if source == target:
                input = np.array(sourceNums[i])-np.array(targetNums[j])
                mean_input = sum(input)/len(input)
                var_input = 0

                for i in input:
                    var_input += i**2
                var_input = np.sqrt(var_input/len(input) - mean_input**2)
                if mean_input > 100:
                    output.append([source,mean_input,var_input])
    return(output)
