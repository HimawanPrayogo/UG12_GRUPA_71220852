#tidak habis dibagi 6 dan 3

a=int(input("Masukkan awal deret:"))
b=int(input("Masukkan akhir deret:"))

ii=0
for i in range(a,b):
    if i%6!=0 and i%3!=0 and i%2==1:
        print(i,end=" ")
