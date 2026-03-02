#membuat tuple
import sys
logsApps=("User1 Login", "User2 Login")
print(logsApps)
print("Memiliki ukuran Tuple", sys.getsizeof(logsApps))

#buktikan bahwa tuple bersifat imutable
#menambahkan elemen kedalam tuple
#logsApps.append("User3 Login")
#logsApps[0]="User4 Login"
#logsApps.remove("User2 Login")

#pembuktian bahwa tuple bisa diakses dengan index
print(logsApps[0])#akses index ke-0
print(logsApps[-1])#akses index ke-1

#slice dan copy
print(logsApps[0:1])
backup_logsApps: = logsApps[:]
print(backup_logsApps)




