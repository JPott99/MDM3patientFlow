import csv

def importData():
    with open('data/hospitalData.csv','rt') as hospInput:
        csv_input = csv.reader(hospInput,delimiter=',')
        myDataHeaders = next(csv_input)
        myData = list(csv_input)
    with open('data/sourceTransfers.csv','rt') as hospInput:
        csv_input = csv.reader(hospInput,delimiter=',')
        sourceTransfersHeaders = next(csv_input)
        sourceTransfers = list(csv_input)
    with open('data/targetTransfers.csv','rt') as hospInput:
        csv_input = csv.reader(hospInput,delimiter=',')
        targetTransfersHeaders = next(csv_input)
        targetTransfers = list(csv_input)
    with open('data/transfers.csv','rt') as hospInput:
        csv_input = csv.reader(hospInput,delimiter=',')
        tranfersHeaders = next(csv_input)
        transfers = list(csv_input)
    with open('data/transferProbability.csv','rt') as hospInput:
        csv_input = csv.reader(hospInput,delimiter=',')
        transProbHeaders = next(csv_input)
        transProb = list(csv_input)
    return (myData,myDataHeaders,sourceTransfers,sourceTransfersHeaders,targetTransfers,targetTransfersHeaders,transfers,tranfersHeaders,transProb,transProbHeaders)
