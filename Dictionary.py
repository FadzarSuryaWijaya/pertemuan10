# Membuat dictionary
a = {
    "n1": 100, "n2" : 20, "n3" : 7
}

print()

# Akses Dictionary
print("=================Akses Dictionary=================")
print(a['n2'])
print(a.keys())
print(a.values())
print(a.items())
print("="*50)

print()

# Mengubah element
a["n2"] = 10

# Menambah element Dictionary
a['n4'] = 50

# Sesudah di tambahkan
print("===========Mengubah & Menambah Element============") 
print(a['n2'])
print(a.keys())
print(a.values())
print(a.items(),"\n")
print("="*50)
print()

# Loop Dictionary 
print("=================Loop Dictionary==================")
for item in a.items():
    print(item)
    print(item[0])
print("="*50)
print()