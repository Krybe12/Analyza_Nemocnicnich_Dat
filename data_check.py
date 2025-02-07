import numpy as np
import pandas as pd

data = pd.read_excel("data.xlsx", sheet_name=None)
pacienti = data["data_pacienti"]
lecba = data["data_lecba"]
neutropenie = data["data_neutropenie"]

pacienti = pacienti.drop('id', axis=1)
#otestování nulových řádků
print(pacienti.isnull().sum())
print(lecba.isnull().sum())
print(neutropenie.isnull().sum())

#otestování duplicitních řádků
print(pacienti[pacienti.duplicated() == True])
print(lecba.duplicated().sum())
print(neutropenie.duplicated().sum())


#test validity dat
print(pacienti[["rok_narozeni", "datum_diagnozy", "datum_umrti"]].describe())

#počet každého pohlaví
print(pacienti.groupby("pohlavi").count())