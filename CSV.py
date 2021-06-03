import csv 


with open('CSV/Empleados.csv', 'r') as Empleados_csv:
    nombre_empleado = csv.reader(Empleados_csv, delimiter=',')
    
    for row in nombre_empleado:
        if 'Diciembre' in row[2]:
            print(row[0])


            