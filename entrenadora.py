y=input("Que edad tienes? ")

if int(y)<10:
    if y=="chico":
        print("No tienes edad",
              "para ser entrenador")
    else:
        print("No tienes edad",
              "para ser entrenadora")
    quit()