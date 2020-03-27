
'''funcion para obtener un salario promedio 
a partir del rango de salarios'''

def salary(value):
    splitted = value.split('-')
    if len(splitted) == 2:
        try:
            avg = sum(list(map(float, splitted)))/2
            return avg
        except ValueError:
            return False
    else:
        try:
            return float(value)
        except ValueError:
            return False
        return float(value)
    