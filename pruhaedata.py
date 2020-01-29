from matplotlib import pyplot as plt
import numpy as np

data = [395, 394, 392, 672, 616, 402, 409, 421, 395, 433, 367, 440, 393, 419, 395, 407, 402, 402,
 383, 420, 405, 392, 387, 428, 402, 401, 456, 451, 469, 510, 466, 438, 448, 475, 487, 462,
 470, 481, 481, 460, 450, 453, 431, 444, 441, 434, 456, 471, 471, 439, 454, 478, 415, 453,
 417, 451, 446, 454, 430, 482, 473, 463, 428, 366, 376, 400, 417, 457, 406, 435, 437, 414,
 447, 418, 384, 406, 423, 427, 441, 477, 402, 185]

data = sorted(data)[1:-2]
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
