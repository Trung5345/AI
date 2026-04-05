 
# ================= BÀI 1 =================
print("=== BÀI 1 ===")
a = 10
b = 5
print("Input: a =", a, ", b =", b)

print("Tong la", a + b)
print("Hieu la", a - b)
print("Tich la", a * b)
print("Thuong la", a / b)

print("\n--------------------------------------\n")

# ================= BÀI 2 =================
print("=== BÀI 2 ===")
string = "HelloWorld"
print("Input:", string)
print("Output:", string[2:5])

print("\n--------------------------------------\n")

# ================= BÀI 3 =================
print("=== BÀI 3 ===")
string = "Hello"
print("Input:", string)

print("Uppercase:", string.upper())
print("LowCase:", string.lower())
print("Replace:", string.replace("H", "J"))

print("\n--------------------------------------\n")

# ================= BÀI 4 =================
print("=== BÀI 4 ===")
a = 10
b = 5
print("Input: a =", a, ", b =", b)

print("Output:", "Hello World" if a > b else "b<a")

print("\n--------------------------------------\n")

# ================= BÀI 5 =================
print("=== BÀI 5 ===")
a = 5
b = 5
print("Input: a =", a, ", b =", b)

print("Output:", "Yes" if a == b else "No")

print("\n--------------------------------------\n")

# ================= BÀI 6 =================
print("=== BÀI 6 ===")
a = 7
b = 5
print("Input: a =", a, ", b =", b)

if a == b:
    print("Output: 1")
elif a > b:
    print("Output: 2")
else:
    print("Output: 3")

print("\n--------------------------------------\n")

# ================= BÀI 7 =================
print("=== BÀI 7 ===")
a, b, d = 5, 5, 5
print("Input:", a, b, d)

print("Output:", "Hello World" if a == b and b == d else "No")

print("\n--------------------------------------\n")

# ================= BÀI 8 =================
print("=== BÀI 8 ===")
a, b, d = 5, 3, 5
print("Input:", a, b, d)

print("Output:", "Hello World" if a == b or b == d else "No")

print("\n--------------------------------------\n")

# ================= BÀI 11 =================
print("=== BÀI 11 ===")
a = [1, 2, 3, 4, 5, 6]
print("Input mảng a:", a)

b = [x for x in a if x % 2 == 0]
print("Output mảng b (số chẵn):", b)

print("\n--------------------------------------\n")

# ================= BÀI 12 =================
print("=== BÀI 12 ===")
print("Input: từ 0 → 999")

sum_val = sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)
print("Output:", sum_val)

print("\n--------------------------------------\n")

# ================= BÀI 13 =================
print("=== BÀI 13 ===")
a = [1, 2, 3]
b = [4, 5, 6]
print("Input a:", a)
print("Input b:", b)

def tron_mang(a, b):
    result = []
    n = min(len(a), len(b))
    for i in range(n):
        result.append(a[i] + b[i])
    if len(a) > n:
        result.extend(a[n:])
    else:
        result.extend(b[n:])
    return result

print("Output:", tron_mang(a, b))

print("\n--------------------------------------\n")

# ================= BÀI 14 =================
print("=== BÀI 14 ===")
import random

def tao_mang(m, n):
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(m)]

a = tao_mang(3, 3)
print("Input: m = 3, n = 3")
print("Output:")
for row in a:
    print(row)

print("\n--------------------------------------\n")

# ================= BÀI 15 =================
print("=== BÀI 15 ===")
from datetime import datetime

class SinhVien:
    def __init__(self, ma_sv, ten, nam_sinh, diem_tb):
        self.ma_sv = ma_sv
        self.ten = ten
        self.nam_sinh = nam_sinh
        self.diem_tb = diem_tb

ds = [
    SinhVien("01DH0001", "Phan Lan", 2003, 6.5),
    SinhVien("02DH0002", "Nguyen Van A", 2005, 4.0),
    SinhVien("03CD0003", "Phan B", 2002, 7.0)
]

print("Input danh sách SV:")
for sv in ds:
    print(sv.ma_sv, sv.ten, sv.nam_sinh, sv.diem_tb)

def dem_len_lop(ds):
    return sum(1 for sv in ds if sv.diem_tb >= 5)

def dem_he_dh(ds):
    return sum(1 for sv in ds if sv.ma_sv[2:4] == "DH")

def dem_ten_lan(ds):
    return sum(1 for sv in ds if sv.ten.split()[-1] == "Lan")

def dem_ho_phan(ds):
    return sum(1 for sv in ds if sv.ten.split()[0] == "Phan")

def xuat_20_tuoi(ds):
    nam_hien_tai = datetime.now().year
    print("\nSinh viên đủ 20 tuổi:")
    for sv in ds:
        if nam_hien_tai - sv.nam_sinh >= 20:
            print(sv.ma_sv, sv.ten)

print("\n===== OUTPUT =====")
print("Số SV lên lớp:", dem_len_lop(ds))
print("Số SV hệ DH:", dem_he_dh(ds))
print("Số SV tên Lan:", dem_ten_lan(ds))
print("Số SV họ Phan:", dem_ho_phan(ds))

xuat_20_tuoi(ds)