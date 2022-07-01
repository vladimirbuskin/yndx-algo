from matplotlib import pyplot as plt
from math import trunc as tr

def salary_to_bucket(value):
    alpha = 2 / (1 + pow(5, 0.5))
    m = 971
    bucket = tr((value * alpha - tr(value * alpha)) * m)
    return bucket

myhist = [0] * 1000000
n_bins = 100
for i in range(1000000):
    myhist[i] = salary_to_bucket(71*i)

fig, ax = plt.subplots(figsize =(10, 7))
ax.hist(myhist, bins = n_bins)
 
plt.show()