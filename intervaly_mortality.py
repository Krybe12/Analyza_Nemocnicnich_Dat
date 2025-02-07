import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("data.xlsx", sheet_name=None)
pacienti = data["data_pacienti"]
lecba = data["data_lecba"]
neutropenie = data["data_neutropenie"]



posledni_lecba = (
  lecba.groupby("id")["datum_aplikace"]
  .max()
  .reset_index()
  .rename(columns={"datum_aplikace": "posledni_lecba"})
)

pacienti = pd.merge(pacienti, posledni_lecba, on="id")

pacienti["rozdil_dny"] = (
  pd.to_datetime(pacienti["datum_umrti"]) - pd.to_datetime(pacienti["posledni_lecba"])
).dt.days

#intervaly
intervaly = [(0, 30), (30, 60), (60, 90), (90, 120), (120, 150), (150, 180)]

#výpočet mortality pro každý interval
mortalita = []
for start, end in intervaly:
  pocet = pacienti[
    (pacienti["rozdil_dny"] <= end) & (pacienti["rozdil_dny"] > start)
  ].shape[0]
  mortalita.append(pocet)

#graf
interval_popis = [f"{start}-{end}" for start, end in intervaly]
plt.bar(interval_popis, mortalita, color="skyblue")
plt.title("30denní intervaly mortality od poslední léčby")
plt.xlabel("Intervaly (dny od poslední léčby)")
plt.ylabel("Počet úmrtí")
plt.show()

