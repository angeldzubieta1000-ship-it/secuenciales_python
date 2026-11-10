## CDT

cantidadDinero = float(input("Ingrese la cantidad de dinero: "))
periodo = float(input("Ingrese el periodo en dias: "))
porcentajeInteres = float(input("Ingrese el porcentaje de interes: "))

porcentajeInteres = porcentajeInteres / 100

valorInteres = (cantidadDinero * porcentajeInteres * periodo) / 360
impuesto = (valorInteres * 0.07)
netopagar = cantidadDinero + valorInteres - impuesto

print ("Intereses ganados" ,valorInteres)
print ("Valor del impuesto" ,impuesto)
print ("Total a pagar" ,netopagar)
