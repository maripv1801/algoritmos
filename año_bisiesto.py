# Asumimos que el año base es 1900, el cual no es bisiesto por ser divisible entre 100 y no entre 400
year_base = 1900

year = int(input("Ingrese un año entre 1900 y 2199: "))
bisiestos = 0

if year % 4 == 0:
        # Excepto si es divisible por 100 y no divisible por 400
    if year % 100 == 0 and year % 400 != 0:
        print("El año no es bisiesto")
    else:
        print("El año es bisiesto")
else:
    # No es bisiesto
    print("El año no es bisiesto")
    
# Cantidad de años divisibles entre 4
divisibles_entre_4 = (year // 4) - ((year_base) // 4)
# Cantidad de años divisibles entre 100
divisibles_entre_100 = (year // 100) - ((year_base) // 100)
# Cantidad de años divisibles entre 400
divisibles_entre_400 = (year // 400) - ((year_base) // 400)
    
# Cálculo de años bisiestos: Divisibles entre 4 - divisibles entre 100 + divisibles entre 400
bisiestos = divisibles_entre_4 - divisibles_entre_100 + divisibles_entre_400
print("Cantidad de años bisiestos entre", year_base, "y", year, ":", bisiestos)