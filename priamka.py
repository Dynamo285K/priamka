from PIL import Image
pic = Image.new("RGB", (250,250), 'white')
pixels = pic.load()


A = input("zadaj 2 hodnoty")
B = input("zadaj 2 hodnoty")
A = A.split(",")
B = B.split(",")

Ax = int(A[0])
Ay = int(A[1])
Bx = int(B[0])
By = int(B[1])


if int(Bx-Ax)>int(By-Ay):
    k = (By-Ay)/(Bx-Ax)
    q = (Ay-k)*Ax
    for x in range(Ax,Bx):
        y = int(k*x*q)
        pixels[x,y]=(0,0,0)


pic.show()
