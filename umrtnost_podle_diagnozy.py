import pandas as pd
import matplotlib.pyplot as plt

#načtení dat
data = pd.read_excel("data.xlsx", sheet_name=None)
pacienti = data["data_pacienti"]

#přidání sloupce úmrtí true/false
pacienti["umrti"] = ~pacienti["datum_umrti"].isna()

#skupinový počet pacientů a počet zemřelých podle diagnózy
umrtnost_podle_diagnozy = (
  pacienti.groupby("diagnoza", as_index=False)
  .agg(celkem_pacientu=("id", "count"), zemreli=("umrti", "sum"))
)

#výpočet úmrtnosti v procentech
umrtnost_podle_diagnozy["umrtnost (%)"] = (
  umrtnost_podle_diagnozy["zemreli"] / umrtnost_podle_diagnozy["celkem_pacientu"] * 100
)

#graf úmrtnosti podle diagnózy
plt.figure(figsize=(10, 6))
plt.bar(umrtnost_podle_diagnozy["diagnoza"], umrtnost_podle_diagnozy["umrtnost (%)"], color="skyblue")
plt.xticks(rotation=50)
plt.title("Úmrtnost podle diagnózy")
plt.xlabel("Diagnóza")
plt.ylabel("Úmrtnost (%)")
plt.tight_layout()
plt.show()