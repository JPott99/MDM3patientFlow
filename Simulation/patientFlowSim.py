import csv
import numpy as np
import time
import importHospData as iH

start_time = time.time()

def targetfromsource(source, data, uniform):
    #targetfromsource gives a random target given one person in source
    [sources,targets,probs] = data
    patientSource = source
    patientTarget = source
    randomChance = np.random.randint(1,2e9)/2e9
    probability = 0
    for i in range(len(sources)):
        if sources[i] == patientSource:
            probability += float(probs[i]) * uniform
        if probability>=randomChance:
            patientTarget = targets[i]
            patientProb = probs[i]
            break
    return(patientTarget)

def simulateHospital(wards,wardPatients,loops,data,wardTransfers,uniform,currentLoop = 0):
    while currentLoop < loops:
        wardPatientsCurrent = wardPatients[-1]
        wardPatients.append(assignment(wards, wardPatientsCurrent,currentLoop, uniform, data))
        currentLoop+=1
    return(wardPatients, wardTransfers)

def assignment(wards, wardPatientsCurrency,currentLoop, uniform, data):
    dh_input,pruh_input = simulateNewPatients()
    wardPatientsFuture = [0]*len(wards)
    wardPatientsFuture[wards.index("PRUH.EmergencyDept.PRUH")] += pruh_input
    wardPatientsFuture[wards.index("KCH.EmergencyDept.DH")] += dh_input
    wardPatientsCurrent = wardPatientsCurrency
    for i in range(len(wards)):
        if wards[i] != "ExitHospital.PRUH" and wards[i] != "ExitHospital.DH" and wards[i] != "ExitHospital.Orpington":
            counter = wardPatientsCurrent[i]
            while counter>0:
                uniformNo = uniform[currentLoop*len(wards)+i]
                target = targetfromsource(wards[i],data, uniformNo)
                wardPatientsFuture[wards.index(target)]+=1
                counter-=1
                for j in range(len(sources)):
                    if sources[j] == wards[i] and targets[j] == target:
                        wardTransfers[j][currentLoop] += 1
                        break
        else:
            wardPatientsFuture[i]+=wardPatientsCurrent[i]
            wardPatientsCurrent[i] = 0
    return (wardPatientsFuture)

def simulateNewPatients():
    dh_input = int(np.random.normal(414,54,1))
    pruh_input = int(np.random.normal(431.71,31.79,1))
    return(dh_input,pruh_input)

with open('data/modelProbabalities.csv','rt') as hospInput:
    csv_input = csv.reader(hospInput,delimiter=',')
    myDataHeaders = next(csv_input)
    myData = list(csv_input)
iH.stripNewLine(myData)
myData = sorted(myData,key=lambda x: -float(x[2]))
myData = np.array(myData)

sources = myData[:,0]
targets = myData[:,1]
probs = myData[:,4]
data = [sources,targets,probs]

wards = sorted(list(set(list(sources) + list(targets))))
###############################################################################
loops = 82
###############################################################################
wardPatientsCurrent = [[0]*len(wards)]

wardTransfers = np.array([[0]*6]*len(sources))
print("--- Initialising ---")
mu = 1; sigma = 1/6
uniform = np.random.normal(mu,sigma,6*len(wards))

wardPatients, wardTransfers = simulateHospital(wards,wardPatientsCurrent,6,data,wardTransfers,uniform)
wardTransfers = np.array([[0]*loops]*len(sources))
print("--- %s seconds ---" % (time.time() - start_time))
print("--- Initialised ---")

print("--- Starting ---")
uniform = np.random.normal(mu,sigma,loops*len(wards))
wardPatients = [wardPatients[-1]]
wardPatients, wardTransfers = simulateHospital(wards,wardPatients,loops,data,wardTransfers,uniform)
transfers = []
for i in range(len(sources)):
    transfers.append([sources[i]]+[targets[i]]+list(wardTransfers[i]))
transfers = sorted(transfers,key = lambda x: x[0])
with open("data/simTransfers.csv",'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Source","Target"]+list(range(loops)))
    for i in range(len(transfers)):
        writer.writerow(transfers[i])
with open("data/simPatients.csv",'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Ward"]+list(range(loops+1)))
    for i in range(len(wards)):
        writer.writerow([wards[i]]+list(np.array(wardPatients)[:,i]))
print("--- %s seconds ---" % (time.time() - start_time))
print("--- Finished ---")
