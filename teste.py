
#aula dicionario

carros = {"Jeep Renegade":['R$90000,00','2019'],
          "Jeep Compass":['R$150000,00','2020'],
          "Troller":['R$200000,00','2023']}
print(carros)
print(carros["Jeep Renegade"])

carros["Jeep Compass"] = 'R$180000,00'

print(carros)

#carros["Jeep Renegade"][1] = "2016"
print(carros)

del carros["Troller"]
print(carros)

carros["Audi"] = ['R$250.000,00',"2023"]
print(carros)

print(carros.keys())
print(carros.values())

#carros["Jeep Compass"][1] = "2019"
print(carros)
