import math
import turtle


def square():
    a = float(input("Longueur/Largeur/Hauteur de ton Carré/Cube en centimètre : "))

    square_perimeter = a + a + a + a
    square_air = a * a
    cube_volume = a * a * a

    print("")
    print("Le périmètre de ton carré est de", round(square_perimeter, 2), "centimètres.")
    print("L'aire de ton carré est de", round(square_air, 2), "centimètres carré.")
    print("Le volume de ton cube est de", round(cube_volume, 2), "centimètres cube.")

    turtle.setup(1920, 1080)
    turtle.title("Traçage en cours...")
    turtle.up()
    turtle.goto(-600, -100)
    turtle.down()
    turtle.speed(11)
    turtle.color("blue")
    turtle.begin_fill()
    turtle.pensize(4)
    turtle.pencolor("black")

    turtle.forward(a * 37.7953)
    turtle.left(90)
    turtle.forward(a * 37.7953)
    turtle.left(90)
    turtle.forward(a * 37.7953)
    turtle.left(90)
    turtle.forward(a * 37.7953)

    turtle.end_fill()
    turtle.hideturtle()
    turtle.up()

    turtle.goto(-200, -100)
    turtle.showturtle()
    turtle.down()
    turtle.speed(0)
    turtle.color("red")
    turtle.begin_fill()
    turtle.pensize(4)
    turtle.pencolor("black")

    turtle.left(90)
    turtle.forward(a * 37.7953)
    turtle.left(90)
    turtle.forward(a * 37.7953)
    turtle.left(90)
    turtle.forward(a * 37.7953)
    turtle.left(90)
    turtle.forward(a * 37.7953)

    turtle.end_fill()
    turtle.hideturtle()
    turtle.up()

    turtle.goto(200, -100)
    turtle.showturtle()
    turtle.down()
    turtle.speed(0)
    turtle.color("green")
    turtle.begin_fill()
    turtle.pensize(4)
    turtle.pencolor("black")

    turtle.left(90)
    turtle.forward(a * 37.7953)
    turtle.left(45)
    turtle.forward((a * 37.7953) / 2)
    turtle.left(135)
    turtle.forward(a * 37.7953)
    turtle.left(45)
    turtle.forward((a * 37.7953) / 2)
    turtle.left(135)
    turtle.forward(a * 37.7953)

    turtle.left(90)
    turtle.forward(a * 37.7953)
    turtle.left(90)
    turtle.forward(a * 37.7953)
    turtle.left(90)
    turtle.forward(a * 37.7953)
    turtle.left(90)
    turtle.forward(a * 37.7953)

    turtle.left(45)
    turtle.forward((a * 37.7953) / 2)
    turtle.left(45)
    turtle.forward(a * 37.7953)
    turtle.left(135)
    turtle.forward((a * 37.7953) / 2)
    turtle.right(180)
    turtle.forward((a * 37.7953) / 2)
    turtle.left(135)
    turtle.forward(a * 37.7953)
    turtle.left(90)
    turtle.forward(a * 37.7953)
    turtle.right(180)
    turtle.forward(a * 37.7953)
    turtle.left(135)
    turtle.forward((a * 37.7953) / 2)

    turtle.end_fill()

    turtle.hideturtle()
    turtle.done()


def rectangle():
    b = float(input("Longueur de ton Rectangle/Parallelepipède en centimètre : "))
    c = float(input("Largeur de ton Rectangle/Parallelepipède en centimètre : "))
    d = float(input("Hauteur de ton Rectangle/Parallelepipède en centimètre : "))

    rectangle_perimeter = b + b + c + c
    rectangle_air = b * c
    rectangle_volume = b * c * d

    print("")
    print("Le périmètre de ton carré est de", round(rectangle_perimeter, 2), "centimètres.")
    print("L'aire de ton carré est de", round(rectangle_air, 2), "centimètres carré.")
    print("Le volume de ton cube est de", round(rectangle_volume, 2), "centimètres cube.")

    turtle.setup(1920, 1080)
    turtle.title("Traçage en cours...")
    turtle.up()
    turtle.goto(-900, -100)
    turtle.down()
    turtle.speed(11)
    turtle.color("blue")
    turtle.begin_fill()
    turtle.pensize(4)
    turtle.pencolor("black")
    turtle.showturtle()

    """début périmètres"""

    turtle.forward(c * 37.7953)
    turtle.left(90)
    turtle.forward(d * 37.7953)
    turtle.left(90)
    turtle.forward(c * 37.7953)
    turtle.left(90)
    turtle.forward(d * 37.7953)
    turtle.left(90)

    turtle.end_fill()
    turtle.hideturtle()
    turtle.up()

    """fin périmètre"""

    """début aire"""

    turtle.goto(-300, -100)
    turtle.color("red")
    turtle.pencolor("black")
    turtle.showturtle()
    turtle.begin_fill()
    turtle.down()

    turtle.forward(c * 37.7953)
    turtle.left(90)
    turtle.forward(d * 37.7953)
    turtle.left(90)
    turtle.forward(c * 37.7953)
    turtle.left(90)
    turtle.forward(d * 37.7953)
    turtle.left(90)

    turtle.end_fill()
    turtle.hideturtle()
    turtle.up()

    """fin aire"""

    """début volume"""

    turtle.goto(300, -100)
    turtle.color("green")
    turtle.pencolor("black")
    turtle.showturtle()
    turtle.begin_fill()
    turtle.down()

    turtle.forward(c * 37.7953)
    turtle.left(45)
    turtle.forward((b * 37.7953) / 2)
    turtle.left(45)
    turtle.forward(d * 37.7953)
    turtle.left(90)
    turtle.forward(c * 37.7953)
    turtle.left(45)
    turtle.forward((b * 37.7953) / 2)
    turtle.left(45)
    turtle.forward(d * 37.7953)
    turtle.left(90)
    turtle.forward(c * 37.7953)
    turtle.left(90)
    turtle.forward(d * 37.7953)
    turtle.left(90)
    turtle.forward(c * 37.7953)
    turtle.left(180)
    turtle.forward(c * 37.7953)
    turtle.left(45)
    turtle.forward((b * 37.7953) / 2)
    turtle.right(135)
    turtle.end_fill()
    turtle.forward(d * 37.7953)
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(c * 37.7953)
    turtle.end_fill()
    turtle.right(90)
    turtle.begin_fill()
    turtle.forward(d * 37.7953)
    turtle.end_fill()
    turtle.left(180)
    turtle.forward(d * 37.7953)
    turtle.begin_fill()
    turtle.right(45)
    turtle.end_fill()
    turtle.forward((b * 37.7953) / 2)

    turtle.hideturtle()
    turtle.up()
    turtle.done()




def disc():
    e = float(input("Le rayon de ton Disque/Cylindre en centimètres : "))
    f = float(input("La hauteur de ton cylindre : "))

    disc_diameter = e + e
    disc_perimeter = 2 * math.pi * e
    disc_air = math.pi * e * e
    cylinder_volume = disc_air * f

    print("")
    print("Le diamètre de ton disque est de", round(disc_diameter, 2), "centimètres.")
    print("Le périmètre de ton disque est de", round(disc_perimeter, 2), "centimètres.")
    print("L'aire de ton disque est de", round(disc_air, 2), "centimètres carré.")
    print("Le volume de ton cylindre est de ", round(cylinder_volume), "centimètres cube.")


def sphere():
    g = float(input("Le rayon de ta sphère en centimètres : "))

    sphere_air = 4 * math.pi * g * g
    sphere_volume = 4 / 3 * math.pi * g * g * g

    print("")
    print("L'aire de ta sphère est de", round(sphere_air, 2), "centimètres.")
    print("Le volume de ta sphère est de", round(sphere_volume, 2), "centimètres.")


print("Vous pouvez calculer le carré, le rectangle, le disque/cylindre, la sphère,")
print("")
calcul = str(input("Que voulez-vous calculer ? "))

if calcul == "carré":
    square()
elif calcul == "rectangle":
    rectangle()
elif calcul == "disque":
    disc()
elif calcul == "sphère":
    sphere()
else:
    print("Rien n'a été choisi")
