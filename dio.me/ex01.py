# Faça um algoritimo que calcule a quantidade combustivel gasto em uma viajem, sabendo que o carro faz 12km com um litro. 
# Além disso, forneça ao usuário o tempo da viajem.

def inputs():
    try: 
        print("Informe a distancia da viajem: ")
        distance = float(input().replace(',', '.'))
        
        print("Informe a velocidade (KM/hr): ")
        speed = float(input().replace(',', '.'))

        return [distance, speed]
    except ValueError:
        print("Digite apenas números!")
        inputs()


infos = inputs()

distance = infos[0]
speed = infos[1]

# Litros gastos
liters = round((distance / 12), 2)
print("Litros gastos: " + str(liters) + "L")

# Tempo
time = round((distance / speed), 2)
print("Tempo da viajem: " + str(time) + " hrs")
