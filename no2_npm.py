a=int(input('Masukkan suku pertama :'))
b=int(input('Masukkan pembeda sukunya :'))
c=int(input('Masukkan berapa banyak sukunya :'))
x=0
z=[]
while x<c:
    z.append(a)
    print(a)
    x=x+1
    a=a+b
w=0
y=0
while y<c:
	w+=z[y]
	y=y+1
print('jumlah aritmatika',w)
