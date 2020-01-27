import csv
import numpy as np

def targetfromsource(source, data):
    #targetfromsource gives a random target given one person in source
    [sources,targets,probs] = data
    patientSource = source
    patientTarget = source
    randomChance = np.random.randint(1,1e18)/1e18
    probability = 0
    for i in range(len(sources)):
        if sources[i] == patientSource:
            probability += float(probs[i])
        if probability>=randomChance:
            patientTarget = targets[i]
            patientProb = probs[i]
            break
    return(patientTarget)

def simulateHospital(wards,wardPatientsCurrent,loops,data,currentLoop=0):
    wardPatientsFuture = [0]*len(wards)
    for i in range(len(wards)):
        while wardPatientsCurrent[i]>0:
            target = targetfromsource(wards[i],data)
            wardPatientsFuture[wards.index(target)]+=1
            wardPatientsCurrent[i]-=1
    currentLoop+=1
    if currentLoop<loops:
        wardPatientsFuture=simulateHospital(wards,wardPatientsFuture, loops,data, currentLoop)
    return(wardPatientsFuture)

with open('modelProbabalities.csv','rt') as hospInput:
    csv_input = csv.reader(hospInput,delimiter=',')
    myDataHeaders = next(csv_input)
    myData = list(csv_input)

myData = sorted(myData,key=lambda x: -float(x[2]))
myData = np.array(myData)

sources = myData[:,0]
targets = myData[:,1]
probs = myData[:,2]
data = [sources,targets,probs]

wards = sorted(list(set(list(sources) + list(targets))))

wardPatientsCurrent = [1]*len(wards)

wardPatientsFuture = simulateHospital(wards,wardPatientsCurrent,11,data)
print(wardPatientsFuture)

for i in range(len(wards)):
    if wardPatientsFuture[i]!= 0:
        print(wards[i],wardPatientsFuture[i])
