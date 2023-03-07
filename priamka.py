from PIL import Image


pic = Image.new("RGB", (300,250), 'white')
pixels = pic.load()


A = input("zadaj 2 hodnoty")
B = input("zadaj 2 hodnoty")
A = A.split(",")
B = B.split(",")

Ax = int(A[0])
Ay = int(A[1])
Bx = int(B[0])
By = int(B[1])




# if int(Bx-Ax)>int(By-Ay):
#     k = (By-Ay)/(Bx-Ax)
#     q = (Ay-k)*Ax
#     for x in range(Ax,Bx):
#         y = int(k*x*q)
#         pixels[x,y]=(0,0,0)
# if int(Bx-Ax)<int(By-Ay):
#     k = (By-Ay)/(Bx-Ax)
#     q = (Ay-k)*Ax
#     for x in range(Ax,Bx):
#         y = int(k*x*q)
#         pixels[x,y]=(0,0,0)

# if Ax < Bx:
#
#     k = (By-Ay)/(Bx-Ax)
#     q = Ay-k*Ax
#     for x in range(Ax, Bx):
#         y = int(k*x*q)
#         pixels[x,y] = (0, 0, 0)
#
# elif Ax == Bx:
#     if Ay < By:
#         for y in range(Ay, By):
#             x = Ax
#             pixels[x,y] = (0, 0, 0)
#     elif Ay == By:
#         x = Ax
#         y = Ay
#         pixels[x,y] = (0, 0, 0)
#     else:
#         for y in range(By, Ay):
#             x = Ax
#             pixels[x,y] = (0, 0, 0)
#
# else:
#     k = (Ay-By)/(Ax-Bx)
#     q = By-k*Bx
#     for x in range(Bx, Ax):
#         y = int(k*x+q)
#         pixels[x,y] = (0, 0, 0)
if Ax < Bx:

    k = (By-Ay)/(Bx-Ax)
    q = Ay-k*Ax
    for x in range(Ax,Bx):
        y = int(k*x+q)
        pixels[x,y] = (0,0,0)

elif Ax == Bx:
    if Ay < By:
        for y in range(Ay,By):
            x = Ax
            pixels[x,y] = (0,0,0)
    elif Ay == By:
        x = Ax
        y = Ay
        pixels[x,y] = (0,0,0)
    else:
        for y in range(By,Ay):
            x = Ax
            pixels[x,y] = (0,0,0)

else:
    k = (Ay-Ay) / (Ax-Bx)
    q = By-k*Bx
    for x in range(Bx,Ax):
        y = int(k*x+q)
        pixels[x,y] = (0,0,0)


pic.show()
