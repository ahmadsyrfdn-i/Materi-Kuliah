#pertemuan 2 materi list

import sys
colors: list[str] = ["red"]
print(colors)
print(sys.getsizeof(colors))

#menambahkan elemen kedalam list
colors.append("Blue")
print(colors)
print(sys.getsizeof(colors))

colors.insert(0, "White")
print(colors)
print(sys.getsizeof(colors))

colors.append("Green")
print(colors)
print(sys.getsizeof(colors))

colors.append("Yellow")
print(colors)
print(sys.getsizeof(colors))

colors.append("Purple")
print(colors)
print(sys.getsizeof(colors))

colors.append("Pink")
print(colors)
print(sys.getsizeof(colors))

colors.append("Black")
print(colors)
print(sys.getsizeof(colors))

colors.append("Brown")
print(colors)
print(sys.getsizeof(colors))

#menghapus elemen dari list
colors.pop()
print(colors)
print(sys.getsizeof(colors))

colors.remove("red")
print(colors)
print(sys.getsizeof(colors))

colors.reverse
print(colors)
print(sys.getsizeof(colors))

numbers: list[int] = [3.60, 3.80, 3.60, 3.80, 3.60, 3.80, 3.60, 3.80]
print(sum(numbers)/len(numbers))
print(len(numbers))
print(sys.getsizeof(numbers))
print(numbers)

backup_numbers: list[float] = numbers.copy()
print(backup_numbers)
print(sys.getsizeof(backup_numbers))