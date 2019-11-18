daftar_nilai = []
while True :
    nama = input("input nama : ")
    NIM = input("input NIM : ")
    tugas = int(input("input Tugas : "))
    UTS = int(input("input UTS : "))
    UAS =int(input("input UAS : "))
    akhir = (tugas * 30/100)+(UTS * 35/100)+(UAS * 35/100)
    daftar_nilai.append([nama, int(NIM), int(tugas), int(UTS), int(UAS), int(akhir)])
    if (input("input data lagi (y/t)?") == 't'):
        break
print("==============================================================")
print("| no |      Nama     |    NIM    | Tugas | UTS | UAS | Akhir |")
print("==============================================================")
i=0
for item in daftar_nilai:
    i+=1
    print("| {no:2d} |  {nama:12s} | {NIM:9d} | {tugas:5d} | {UTS:3d} | {UAS:3d} | {akhir:5.2f} |".format(nama=item[0], NIM=item[1], tugas=item[2], UTS=item[3], UAS=item[4], akhir=item[5], no=i))