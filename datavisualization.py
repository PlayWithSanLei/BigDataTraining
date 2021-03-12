dat=dat[(dat['label']==1)].index.tolist()
rat=data1.loc[dat,:]
print(rat)
print(a,b)
print(dat)
print(rat["industryphy"])
print(Counter(rat["industryphy"]))
print(Counter(data1["industryphy"]))
print(rat.columns)
print(rat.loc[:,['ID','opfrom_TONOW','regcap']])
rst=rat.loc[:,['ID','opfrom_TONOW','regcap']]
rst.to_csv(r"C:\Users\aini\Documents\Tencent Files\1029241313\FileRecv\result.csv")
