a=int(input('Masukkan suku pertama :'))
b=int(input('Masukkan pembeda sukunya :'))
c=int(input('Masukkan berapa banyak sukunya :'))
x=0
z=0
while x<c:
    print(a,end=' ')
    z+=a
    x=x+1
    a=a*b
print('Jumlah :',z)
 
