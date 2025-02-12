import pandas as pd
import numpy as np

personeller = {
    'Çalışan' : ['Berfin Çelik','Güler Çelik','Barış Çelik','Gamze Sırakaya','Nimet Yıldız','Ali Çelik','Zeynep Çelik'],
    'Departman' : ['Yazılım','Fabrikacı','Garson','Yazılım','Fabrikacı','Garson','Fabrikacı'],
    'Yaş': [26,52,45,26,47,46,37],
    'Semt' : ['Şehitlik','Şehitlik','Cumhuriyet','Kurtuluş','Kurtuluş','Şentepe','Cumhuriyet'],
    'Maaş': [35000,23000,25000,95000,22000,26000,28000]
}

df = pd.DataFrame(personeller)
result = df
result = df["Maaş"].sum() #komple maaş toplamı

result = df.groupby("Departman") #<pandas.core.groupby.generic.DataFrameGroupBy object at 0x10714e120>
result = df.groupby("Departman").groups #{'Fabrikacı': [1, 4, 6], 'Garson': [2, 5], 'Yazılım': [0, 3]}
result = df.groupby(["Departman","Semt"]).groups

# for name, group in df.groupby("Semt"):
#     print(name)
#     print(group)


# for name, group in df.groupby("Departman"):
#     print(name)
#     print(group)

result = df.groupby("Semt").get_group("Şehitlik")
result = df.groupby("Departman").get_group("Fabrikacı")
result = df.groupby("Departman").sum()
result = df.groupby("Departman").min()
result = df.groupby("Departman")["Maaş"].mean()
result = df.groupby("Semt")["Yaş"].mean()
result = df.groupby("Semt")["Çalışan"].count()
result = df.groupby("Departman")["Yaş"].max()
result = df.groupby("Departman")["Maaş"].min()
result = df.groupby("Departman")["Maaş"].max()["Fabrikacı"]
result = df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min]).loc["Fabrikacı"] #Ortalama


print(result)
