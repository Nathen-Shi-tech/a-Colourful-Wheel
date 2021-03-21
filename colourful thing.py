import turtle,random
turtle.mode("logo")
turtle.shape("turtle")

turtle.colormode(255)




turtle.speed(5)


for j in range(12):
    r=(random.randint(0,255))
    g=(random.randint(0,255))
    b=(random.randint(0,255))
    for i in range(2):
        turtle.pencolor(r,g,b)
        turtle.forward(100)
        turtle.dot(50)
          
    turtle.left(180)
    turtle.forward(200)
    turtle.left(180)
    turtle.right(30)







