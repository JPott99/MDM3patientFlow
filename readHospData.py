import csv

with open('pone0185912s003.csv', 'rt') as f_input:
    csv_input = csv.reader(f_input, delimiter=',')
    header = next(csv_input)
    data = list(csv_input)

maxWeek = 0
maxYear = 0
minWeek = 10000
minYear = 10000

myData = []
for i in range(len(data)):
    currentData = []
    currentData.append(data[i][0]) #Source
    # currentData.append(data[i][1]) #Site Source
    currentData.append(data[i][2]) #Target
    # currentData.append(data[i][3]) #Site Target
    currentData.append(int(data[i][4])) #Transfers
    currentYear = int(data[i][5]) #Year
    currentWeek = int(data[i][6]) #Week of Year
    if currentYear == 2014:
        currentWeek = currentWeek-48
    if currentYear == 2015:
        currentWeek = currentWeek+3
    if currentYear == 2016:
        currentWeek = currentWeek + 52 + 3
    currentData.append(currentWeek)
    myData.append(currentData)

#myData form is [Source, Target, Transfers, Week]

Sources = []
Targets = []
for i in range(len(myData)):
    currentSource = myData[i][0]
    currentTarget = myData[i][1]
    if currentSource not in Sources:
        Sources.append(currentSource)
    if currentTarget not in Targets:
        Targets.append(currentTarget)

weeklyTransfers = [0]*82
for i in range(len(myData)):
    j = myData[i][3]
    weeklyTransfers[j]+=myData[i][2]
print((weeklyTransfers))
