import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#načtení dat
data = pd.read_excel("data.xlsx", sheet_name=None)
pacienti = data["data_pacienti"]
lecba = data["data_lecba"]
neutropenie = data["data_neutropenie"]

#získání data poslední léčby pro každého pacienta
posledni_lecba = (
    lecba.groupby("id")["datum_aplikace"]
    .max()
    .reset_index()
    .rename(columns={"datum_aplikace": "posledni_lecba"})
)

#spojení tabulek pacienti a poslední léčby
pacienti_lecba = pd.merge(pacienti, posledni_lecba, on="id", how="left")

#spojení pacientů s daty o neutropenii
pacienti_neutropenie = pd.merge(pacienti_lecba, neutropenie, on="id", how="left")

#přidání příznaku neutropenie (True/False)
pacienti_neutropenie["neutropenie"] = ~pacienti_neutropenie["datum_neutropenie"].isna()

#výpočet výskytu neutropenie podle pohlaví
neutropenie_pohlavi = (
    pacienti_neutropenie.groupby("pohlavi")["neutropenie"].mean() * 100
)

#graf
labels = ["Muži", "Ženy"]
values = [neutropenie_pohlavi.get(1, 0), neutropenie_pohlavi.get(2, 0)]  #1 = Muž, 2 = Žena

plt.bar(labels, values, color=["blue", "pink"])
plt.title("Procentuální výskyt febrilní neutropenie podle pohlaví")
plt.xlabel("Pohlaví")
plt.ylabel("Výskyt (%)")
plt.ylim(0, 16)
plt.show()