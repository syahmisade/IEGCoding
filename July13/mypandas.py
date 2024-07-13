import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector as mysql
from sqlalchemy import create_engine


population = pd.read_csv("population.csv")
population.drop([0,1],axis=0,inplace=True)
population.reset_index(inplace=True)
population.drop("index",axis=1,inplace=True)
population.drop("idxs",axis=1,inplace=True)
population = population[["state","pop_5","pop_12","pop_18","pop_60","pop"]]
population.columns = ["state","children","teenager","adults","senior","total"]
print(population)
population.to_excel("population.xlsx")

# connection = mysql.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="peneraju"
#     )

# population.to_sql(connection,"population") # type: ignore

engine = create_engine("mysql+mysqlconnector://root@localhost/peneraju")
population.to_sql("population",con=engine,if_exists="append")