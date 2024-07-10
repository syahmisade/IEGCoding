'''
Pandas:
- a library
- install jupyter notebook (download it)
- install pandas
'''
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
data = randn(5,4)
print(data)

clms = ["W","X","Y","Z"]
print(clms)

index = ["A","B","C","D","E"]
print(index)

df = pd.DataFrame(data, columns=clms, index=index)
print(df)

