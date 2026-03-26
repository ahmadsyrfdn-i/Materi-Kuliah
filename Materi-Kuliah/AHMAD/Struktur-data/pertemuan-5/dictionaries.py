#membuat struktur data dictionary
userLogin = {"name": "Ahmad", "age":19, "role":"pangeran"}
print(type(userLogin))

# Mengakses Data
print(f"Nama Akun : {userLogin['name']}")
print(f"Umur Akun : {userLogin['age']} Tahun")
print(f"Role Akun : {userLogin['role']}")

#akses data seluruh
print(userLogin.items())
print(userLogin.keys())
print(userLogin.values())

# Menambah Data kedalam dictionary big-O O(1)
userLogin["email"] = "ahmad123@gmail.com"
print(userLogin)

# Menghapus Data dari dictionary big-O O(1)
userLogin.pop("age")
print(userLogin)

#mengubah data dalam dictionary big-O O(1)
userLogin["role"] = "raja"
print(userLogin)

#nested dictionary
dbUser = {"user1": {"name": "Ahmad", "age": 19, "role": "pangeran"},
          "user2": {"name": "Syarif", "age": 25, "role": "raja"},
          "user3": {"name": "udin", "age": 21, "role": "tuan"}}

print(dbUser)

#akses value base key
print(dbUser["user1"])

#melakukan pencarian data dalam dictionary
finword = input("Masukkan nama user yang ingin dicari: ")
if finword in dbUser:
    print("Data ditemukan")
    print(dbUser[finword])
else:
    print("Data tidak ditemukan")