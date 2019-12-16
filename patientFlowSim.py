import csv
import numpy as np

with open('modelProbabalities.csv','rt') as hospInput:
    csv_input = csv.reader(hospInput,delimiter=',')
    myDataHeaders = next(csv_input)
    myData = list(csv_input)

myData = sorted(myData,key=lambda x: -float(x[2]))
myData = np.array(myData)

sources = myData[:,0]
targets = myData[:,1]
probs = myData[:,2]
patientTarget = sources[np.random.randint(len(sources))]
print("The Patient Starts in", patientTarget)
week = 0
while patientTarget != "ExitHospital":
    patientSource = patientTarget
    randomChance = np.random.randint(1,1e18)/1e18
    probability = 0
    for i in range(len(sources)):
        if sources[i] == patientSource:
            probability += float(probs[i])
        if probability>=randomChance:
            patientTarget = targets[i]
            patientProb = probs[i]
            break
    if patientTarget != patientSource:
        print("In week",week,"the patient went from",patientSource, "to", patientTarget)
    else:
        print("In week",week,"the patient stayed in", patientTarget)
    week+=1
