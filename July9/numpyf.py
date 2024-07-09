'''
As a data science:
- Data Collection
- Data Preparation
- Exploratory Data Analysis (EDA)
    - Statistic
        - Discriptive
            - Statistics
            - Mathematics
        - Inferential
        - Mean/Median
        - Mod/STD
        - Quartile/Variance
        - Normal Distribution
            - Positive/Negetive Skew
            - Unimodel/Bimodel/Multimodel
            - Standard deviations
            - Boxplot
            - iqr formula to find outliers
            
'''
q0 = [10,20,30,40,50] # a quantity
nq = [5,15,25,35,45] # new quantity
tq = zip(q0,nq) # total quantity
ltq = [x+y for x,y in tq]

# print(tq)
# print(list(tq))
# print(ltq)
import time
import numpy as np

size = 10000000
la = range(0,size)
lb = range(0,size)
npa = np.arange(0,size)
npb = np.arange(0,size)

st = time.time()
tqab = [x+y for x,y in zip(la,lb)]
print(time.time() - st)
# print(tqab)   

st = time.time()
d = npa + npb
print(time.time() - st)

print([tqab[0:10]])
print([d[0:10]])