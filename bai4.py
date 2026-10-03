tong_giay = int(input())
phut = (tong_giay % 3600) // 60
gio = tong_giay // 3600
giay = tong_giay % 60
print(gio, round(phut), giay, sep =":")
