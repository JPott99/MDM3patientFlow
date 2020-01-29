import csv
import numpy as np
import time

start_time = time.time()

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

def simulateHospital(wards,wardPatientsCurrent,loops,data,wardTransfers,currentLoop = 0):
    # while currentLoop < loops:
    dh_input,pruh_input = simulateNewPatients()
    wardPatientsFuture = [0]*len(wards)
    wardPatientsFuture[wards.index("PRUH.EmergencyDept.PRUH")] += pruh_input
    wardPatientsFuture[wards.index("KCH.EmergencyDept.DH")] += dh_input
    for i in range(len(wards)):
        if wards[i] != "ExitHospital.PRUH" and wards[i] != "ExitHospital.DH" and wards[i] != "ExitHospital.Orpington":
            while wardPatientsCurrent[i]>0:
                target = targetfromsource(wards[i],data)
                wardPatientsFuture[wards.index(target)]+=1
                wardPatientsCurrent[i]-=1
                for j in range(len(sources)):
                    if sources[j] == wards[i] and targets[j] == target:
                        wardTransfers[j][currentLoop] += 1
                        break
        else:
            wardPatientsFuture[i]+=wardPatientsCurrent[i]
            wardPatientsCurrent[i] = 0
    currentLoop+=1
    if currentLoop<loops:
        wardPatientsFuture, wardTransfers = simulateHospital(wards,wardPatientsFuture,loops,data,wardTransfers,currentLoop)
    return(wardPatientsFuture, wardTransfers)

def simulateNewPatients():
    dh_input = int(np.random.normal(414,54,1))
    pruh_input = int(np.random.normal(431.71,31.79,1))
    return(dh_input,pruh_input)

with open('modelProbabalities.csv','rt') as hospInput:
    csv_input = csv.reader(hospInput,delimiter=',')
    myDataHeaders = next(csv_input)
    myData = list(csv_input)

myData = sorted(myData,key=lambda x: -float(x[2]))
myData = np.array(myData)

sources = myData[:,0]
targets = myData[:,1]
probs = myData[:,4]
data = [sources,targets,probs]

wards = sorted(list(set(list(sources) + list(targets))))

loops = 82

wardPatientsCurrent = [0]*len(wards)

wardTransfers = np.array([[0]*6]*len(sources))
print("--- Initialising ---")
wardPatientsCurrent, wardTransfers = simulateHospital(wards,wardPatientsCurrent,6,data,wardTransfers)
wardTransfers = np.array([[0]*loops]*len(sources))
print("--- %s seconds ---" % (time.time() - start_time))
print("--- Initialised ---")

print("--- Starting ---")
wardPatientsFuture, wardTransfers = simulateHospital(wards,wardPatientsCurrent,loops,data,wardTransfers)
#
# for i in range(len(wards)):
#     if wardPatientsFuture[i]!= 0:
#         print(wards[i],wardPatientsFuture[i])

with open("simTransfers.csv",'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Source","Target"]+list(range(loops)))
    for i in range(len(sources)):
        writer.writerow([sources[i]]+[targets[i]]+list(wardTransfers[i]))
print("--- Finished ---")
print("--- %s seconds ---" % (time.time() - start_time))
