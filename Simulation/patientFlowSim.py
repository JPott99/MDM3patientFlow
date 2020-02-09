import csv
import numpy as np
import importHospData as iH
import findHospInput as fHi
import findProbs as fP

# NOTE: readHospData MUST be run once prior to using the simulation.

def targetfromsource(source, data, uniform):
    #targetfromsource gives a random target given one person in a given source
    # based on the weightings calculated.
    [sources,targets,probs] = data
    patientSource = source
    patientTarget = source
    # Pick a random number upto 1.
    randomChance = np.random.randint(1,2e9)/2e9
    probability = 0
    for i in range(len(sources)):
        # Check that the current source index is the source required, which is
        # needed because there are multiple targets for each source.
        if sources[i] == patientSource:
            # probability, which starts at 0, has the weighting of the currently
            # checked source-target pair times a uniformly distributed random
            # number added to it.
            probability += float(probs[i]) * uniform
        if probability>=randomChance:
            # If the weightings of all of the transfers checked upto and
            # including the current one exceed the randomChance, then assign the
            # current target as the target.
            patientTarget = targets[i]
            patientProb = probs[i]
            break
    return(patientTarget)

def simulateHospital(wards,wardPatients,loops,data,wardTransfers,uniform,aeinput,currentLoop = 0):
    # Cycles through the simulation for as many loops required. Loops are
    # similar to weeks in the original data.
    while currentLoop < loops:
        wardPatientsCurrent = wardPatients[-1]
        wardPatients.append(assignment(wards, wardPatientsCurrent,currentLoop, uniform, data,aeinput))
        currentLoop+=1
    return(wardPatients, wardTransfers)

def simulateNewPatients(aeinput):
    # Uses findHospInput to find the number of patients entering the hospital.
    # We currently assume that all patients enter via the EmergencyDepts, as
    # it has the only significant input-output difference.
    dh_input = int(np.random.normal(aeinput[0][1],aeinput[0][2],1))
    pruh_input = int(np.random.normal(aeinput[1][1],aeinput[1][2],1))
    return(dh_input,pruh_input)


def assignment(wards, wardPatientsCurrent,currentLoop, uniform, data, aeinput):

    dh_input,pruh_input = simulateNewPatients(aeinput)
    wardPatientsCurrent[wards.index("PRUH.EmergencyDept.PRUH")] += pruh_input
    wardPatientsCurrent[wards.index("KCH.EmergencyDept.DH")] += dh_input

    # In order that each cycle can end, patients transfer from
    # wardPatientsCurrent to wardPatientsFuture.
    wardPatientsFuture = [0]*len(wards)
    for i in range(len(wards)):
        # As patients cannot transfer out of ExitHospital, it quickly becomes
        # very large and can take a long time to individually assign each
        # patient to stay where they are. As such, they are all transferred in
        # one block.
        if wards[i] != "ExitHospital.PRUH" and wards[i] != "ExitHospital.DH" and wards[i] != "ExitHospital.Orpington":
            counter = wardPatientsCurrent[i]
            # Other patients are assigned individually.
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
    return (wardPatientsFuture)

hospData = iH.importData()

# Get the weightings from findProbs, and put them in a useable format.
myData = fP.findMeanProbs(hospData)
myData = sorted(myData,key=lambda x: -float(x[2]))
myData = np.array(myData)
sources = myData[:,0]
targets = myData[:,1]
probs = myData[:,2]
data = [sources,targets,probs]

# Find the names of each ward.
wards = sorted(list(set(list(sources) + list(targets))))
###############################################################################
loops = 82 #The number of loops in the main simulation
###############################################################################
# As we don't know the number of patients in each ward, we use the simulation
# to initialise the hospital. We run it for 5 cycles as that is enough for it
# to stabilise. If current situation is known, that would be preferable.
###############################################################################
wardPatientsCurrent = [[0]*len(wards)]
wardTransfers = np.array([[0]*5]*len(sources))
mu = 1; sigma = 1/6 #mu and sigma were selected to roughly scale to the data.
uniform = np.random.normal(mu,sigma,5*len(wards))
# We calculate uniform in advance to improve performance.
aeinputs = fHi.getInputs(hospData)
wardPatients, wardTransfers = simulateHospital(wards,wardPatientsCurrent,5,data,wardTransfers,uniform,aeinputs)
###############################################################################
# Having initialised the hospital, we can now run the simulation.
wardTransfers = np.array([[0]*loops]*len(sources))
uniform = np.random.normal(mu,sigma,loops*len(wards))
wardPatients = [wardPatients[-1]]
wardPatients, wardTransfers = simulateHospital(wards,wardPatients,loops,data,wardTransfers,uniform,aeinputs)
transfers = []
for i in range(len(sources)):
    transfers.append([sources[i]]+[targets[i]]+list(wardTransfers[i]))
transfers = sorted(transfers,key = lambda x: x[0])
with open("data/simTransfers.csv",'w') as file:
    # This output is the simulation of the original data, in the transfers format.
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Source","Target"]+list(range(loops)))
    for i in range(len(transfers)):
        writer.writerow(transfers[i])
with open("data/simPatients.csv",'w') as file:
    # This output is a rough estimate of the number of patients in each ward
    # based on the transfers into it.
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Ward"]+list(range(loops+1)))
    for i in range(len(wards)):
        writer.writerow([wards[i]]+list(np.array(wardPatients)[:,i]))
