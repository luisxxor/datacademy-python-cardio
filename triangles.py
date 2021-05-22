
# Obtener parametros
base = float(input("Inserte la base: "))
altura = float(input("Ingresa la altura: "))

# Calcular y rendondear area
area = round( base*altura/2 , 2)

print(f"El area del triangulo es: {area}")

# Pedir los otros 2 lados para categorizar el triangulo dependiendo del largo de sus lados
lado_a = float(input("Inserte uno de los lados: "))
lado_b = float(input("Inserte otro de los lados: "))

# Si todos sus lados son iguales es equilatero
if lado_a == lado_b and lado_b == base:
    print("Es un triangulo equilatero")

# si no, debe ser escaleno o isosceles, como para ser escaleno debe cumplir una sola condicion
# pues es mas facil preguntar si es escaleno
elif lado_a != lado_b and lado_b != base and base != lado_a:
    print("Es un triangulo escaleno")

# Y si no es equilatero ni escaleno, entonces es isosceles
else:
    print("Es un triangulo isosceles")
