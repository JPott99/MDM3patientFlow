from matplotlib import pyplot as plt
import numpy as np

data = [419, 435, 456, 697, 582, 396, 400, 411, 417, 360, 377, 415, 427, 443, 408, 404, 383, 401,
 401, 400, 405, 425, 459, 427, 410, 435, 470, 433, 448, 472, 439, 474, 396, 400, 411, 385,
 424, 408, 435, 401, 418, 438, 391, 385, 401, 397, 415, 430, 399, 395, 387, 398, 385, 431,
 378, 415, 442, 433, 446, 383, 461, 409, 434, 377, 393, 420, 393, 417, 411, 361, 416, 390,
 406, 377, 441, 398, 407, 418, 382, 384, 336, 193]

data = sorted(data)
minData = min(data)
maxData = max(data)

mean_data = sum(data)/len(data)
var_data = 0

for i in data:
    var_data += i**2
var_data = np.sqrt(var_data/len(data) - mean_data**2)

bins = np.linspace(minData,maxData,10)
# print(data)

midbins = [0]
for i in range(len(bins)-1):
    midbins.append((bins[i]+bins[i+1])/2)
midbins.append(np.inf)
bin0 = []
bin1 = []
bin2 = []
bin3 = []
bin4 = []
bin5 = []
bin6 = []
bin7 = []
bin8 = []
bin9 = []
for i in data:
    for j in range(len(midbins)-1):
        if i >= midbins[j] and i<= midbins[j+1]:
            if j == 0:
                bin0.append(i)
            if j == 1:
                bin1.append(i)
            if j == 2:
                bin2.append(i)
            if j == 3:
                bin3.append(i)
            if j == 4:
                bin4.append(i)
            if j == 5:
                bin5.append(i)
            if j == 6:
                bin6.append(i)
            if j == 7:
                bin7.append(i)
            if j == 8:
                bin8.append(i)
            if j == 9:
                bin9.append(i)
binData = [bin0,bin1,bin2,bin3,bin4,bin5,bin6,bin7,bin8,bin9]

binSizes = []

for i in binData:
    binSizes.append(len(i))

binSizes = binSizes/np.linalg.norm(np.array(binSizes).reshape(1,-1))
print(mean_data,var_data)
plt.plot(range(len(binSizes)),binSizes)
plt.show()
