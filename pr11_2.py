import pandas as pd
import matplotlib.pyplot as plt
import locale

locale.setlocale(locale.LC_TIME, 'Ukrainian_Ukraine.1251')

df = pd.read_csv('comptagevelo2013.csv')
print(df.head())
print(df.info())
print(df.describe())

df['Date'] = pd.to_datetime(df['Date'], format='mixed')
num_cols = df.select_dtypes(include='number').columns
df[num_cols] = df[num_cols].fillna(0)
df[num_cols] = df[num_cols].astype(int)
print("\nОновлений датафрейм --->\n")
print(df.info())
print(df.head())
total_all=df[num_cols].sum().sum()
print("\nЗагальна кількість велосипедистів за 2013 рік:", total_all)
total_per_track=df[num_cols].sum()
print("\nК-сть велосипедистів за рік по доріжках:")
print(total_per_track)
tracks=['Rachel / Papineau','Berri1','Maisonneuve_2']
print("\nНайпопуляніший місяць на обраних доріжках:")
for t in tracks:
    monthly = df.groupby(df['Date'].dt.month)[t].sum()
    monthly.index = monthly.index.map(lambda m: pd.to_datetime(str(m),format='%m').strftime('%B'))
    best = monthly.idxmax()
    print(t, ":", best, "->", monthly[best])
track_plot='Rachel / Papineau'
mp = df.groupby(df['Date'].dt.month)[track_plot].sum()
mp.index = mp.index.map(lambda x: pd.to_datetime(str(x),format='%m').strftime('%B'))
plt.figure(figsize=(10,5))
mp.plot(kind='bar', color='skyblue')
plt.title("Завантаженість велодоріжки "+track_plot+" по місяцях")
plt.xlabel("Місяць")
plt.ylabel("К-сть велосипедистів")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=.6)
plt.show()
