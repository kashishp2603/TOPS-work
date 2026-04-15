lst_city=["Ahmedabad","Surat","diu","baroda"]
for i in lst_city:
    if len(i)>5:
        print(f"{i.upper()}")
    else:
        print(f"{i.lower()}")