import numpy as np
import importHospData as iH

def getInputs(data):
    # Calculates the mean and variance of the difference of the transfers into
    # and out of each ward.
    myData,myDataHeaders,sourceTransfers,sourceTransfersHeaders,targetTransfers,targetTransfersHeaders,transfers,tranfersHeaders,transProb,transProbHeaders=data
    sourceTransfers = [x for x in sourceTransfers if x!=[]]
    sourceNum = np.array(sourceTransfers)[:,1:]
    sourceNums = []
    for i in range(len(sourceNum)):
        sourceNums.append(list(map(int,sourceNum[i])))
    targetTransfers = [x for x in targetTransfers if x!=[]]
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
                # Currently only outputs for the two EmergencyDept wards, as
                # they are the only significant positive difference. 
                if mean_input > 100:
                    output.append([source,mean_input,var_input])
    return(output)

if __name__=="__main__":
    output = getInputs(iH.importData())
    print(output)
