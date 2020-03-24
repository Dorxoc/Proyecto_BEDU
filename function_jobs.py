
'''funcion para obtener un salario promedio 
a partir del rango de salarios'''

def salary(cadena):
    salary_list = list(map(float, cadena.split('-')))
    salary_average = sum(salary_list)/2
    return salary_average

´