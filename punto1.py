#Un turista realiza un viaje de un punto A a un punto B, dentro del rango del punto A al punto B debe realizar varias escalas , las cuales dependen de el realizar; diseñe un algoritmo que permita ingresar las cantidad de escalas dentro de las cuales el tusirta debe ingresar la distancia a recorrer y ir sumando cada una y al fin decor cuantas distancias y etapa realizo.
total = 0
etapasInt = int(input('Ingrese número de etapas -> '))
for i in range(etapasInt):
    distanciaInt = int(input('Ingrese distancia a recorrer -> '))
    total += distanciaInt
print('La distancia recorrida a sido' , total)


