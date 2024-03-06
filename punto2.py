#Un agricultor realiza la siembra de 3 cultivos: papa, yuca y zanahoria; el cultivo de papa requiere una cantidad X de riego a la semana, la yuca y la zanahoria tambien. consultar en internet dicho procedimiento y establecer esta caracteristica en un programa 
total = 0
cultivoStr = input('1. Papa \n2. Yuca\n3. Zanahoria \n- >')

if cultivoStr == '1':
    for i in range(3):
        litros_papa = int(input('¿Cantidad de litros? -> '))
        total+= litros_papa
    print('La cantidad de litros aplicados a la semana son: ', total)
if cultivoStr =='2':
    for i in range(1):
        litros_yuca = int(input('¿Cantidad de litros? -> '))
        total+= litros_yuca
    print('La cantidad de litros aplicados a la semana son: ', total)
if cultivoStr == '3':
    for i in range(4):
        litros_zanahoria = int(input('¿Cantidad de litros? -> '))
        total+= litros_zanahoria
    print('La cantidad de litros aplicados a la semana son: ', total)