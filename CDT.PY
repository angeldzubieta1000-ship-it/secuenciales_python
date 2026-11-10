cantidadDinero = float(input("Ingrese la cantidad de dinero: "))
periodo = float(input("Ingrese el periodo en dias: "))
porcentajeInteres = float(input("Ingrese el porcentaje de interes: "))


valorInteres=(cantidadDinero*porcentajeInteres*periodo)/360
impuesto=valorInteres*0.07
totalApagar=(cantidadDinero+valorInteres) - impuesto

print ("Intereses ganados" ,valorInteres)
print ("Total a pagar" ,totalApagar)