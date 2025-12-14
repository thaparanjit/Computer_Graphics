x1=int(input("Enter x1:"))
y1=int(input("Enter y1:"))
x2=int(input("Enter x2:"))
y2=int(input("Enter y2:"))

def dda_line_draw(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    if dx>dy:
        step=dx
    else: 
        step=dy
    Xinc=dx/step
    Yinc=dy/step
    x=x1
    y=y1
    for i in range(step-1):
        x=x+Xinc
        y=y+Yinc
        print("(",x,y,")")
    

dda_line_draw(x1,y1,x2,y2)
