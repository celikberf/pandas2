import pandas as pd

data = pd.read_csv("pandas_string.csv")
data = pd.DataFrame(data)
data.rename(columns={"en_US Monday": "Name"}, inplace=True)
data.dropna(inplace = True) # NaN alanlarını sildik
# data["Name"] = data["Name"].str.upper() # en_US Monday  alanlarını komple büyük yazdı
# data["index"] = data["Name"].str.find('a')
# data = data.Name.str.contains('August')
data = data.Name.str.replace(' ', '-')




print(data)