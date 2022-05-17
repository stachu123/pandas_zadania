import pandas as pd

# df = pd.read_excel("imiona2.xlsx")
# print(df.head(10))
#
# wieksza_od_1000 = df.loc[df.Liczba > 1000]
# print(wieksza_od_1000)
#
# moje_imie = df.loc[df.Imie == "STANISŁAW"]
# print(moje_imie)
#
# print(df.Liczba.sum())
# print(df.groupby(["Imie"]).agg({"Liczba":["sum"]}))
# print(df.loc[df.Rok>=2000].loc[df.Rok<=2005].agg({'Liczba':['sum']}))
# print(df.groupby(["Plec"]).agg({'Liczba':['sum']}))
#
# print(df["Imie"].max(axis=0))
# print(df.groupby(["Rok", "Plec"]).agg('min'))

# grupaplec = df.groupby('Plec')
# for n in grupaplec.groups.keys():
#     for m in grupaplec.get_group(n).groupby('Rok').groups.keys():
#         print(grupaplec.get_group(n).groupby('Rok').get_group(m).sort_values(by='Liczba').iloc[-1]['Imie'])

# print(df.groupby(["Rok"]).agg({'Liczba':['max']}))
#
# plecrok = df.groupby(['Plec','Rok'])
#
# for m in plecrok.groups.keys():
#     print(plecrok.get_group(m).sort_values(by='Liczba').iloc[-1])

df = pd.read_csv("zamowienia.csv", sep=";")

print(df.head())
print(df["Sprzedawca"].unique())
print(df["Utarg"].nlargest(5))
# print(df.loc[df["Utarg"].idmax()])
print(df.groupby("Sprzedawca").agg({"idZamowienia" : "count"}))
print(df.groupby("Kraj").agg({"idZamowienia" : "count"}))
mask2005 = (df['Data zamowienia'] >= "2005-01-01") & (df['Data zamowienia'] <= "2005-12-31")
mask2004 = (df['Data zamowienia'] >= "2004-01-01") & (df['Data zamowienia'] <= "2004-12-31")
df1 = df[mask2005]
df2 = df[mask2004]
print(df1.head)
print(df1.groupby("Kraj").agg({"Sprzedawca": "count"}))
print(df2.groupby("Kraj").agg({"Utarg": "mean"}))
df1.to_csv(r'dane2005', index=False)
df1.to_csv(r'dane2004', index=False)






