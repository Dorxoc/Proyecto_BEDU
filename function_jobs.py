'''
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(jobs['country'].value_counts().sort_values('index'))
'''




'''funcion para obtener un salario promedio 
a partir del rango de salarios'''

def salary(value):
    splitted = value.split('-')
    if len(splitted) == 2:
        try:
            avg = sum(map(float, splitted))/2
            return avg
        except ValueError:
            return 0.0
    else:
        try:
            return float(value)
        except ValueError:
            return 0.0
        
'''
localizacion
index 0 arroja el pais
index 1 arroja el estado 
index 2 arroja ciudad
'''
        
            
def country(string): 
    list_string = string.split(', ') 
    if len(list_string) == 3 and list_string[0]!='': 
        return list_string[0] 
    else: 
        return 'unknown' 

    
    
    
    
def state(string): 
    list_string = string.split(', ') 
    if len(list_string) == 3 and list_string[1]!='': 
        return list_string[1].upper() 
    else: 
        return 'unknown' 
    
    
    
def city(string): 
    list_string = string.split(', ') 
    if len(list_string) == 3 and list_string[2]!='': 
        return list_string[2].lower() 
    else: 
        return 'unknown' 

    
    
''' 
lo que tenga que ver con vocational lo pasa a professional
''' 

def education(x):
    if x == 'Vocational' or x == 'Vocational - Degree' or x == 'Vocational - HS Diploma' :
        return 'Professional'
    else:
        return x
    

'''
conteo de palabras en un string
'''
def count_(string):
    if type(string) == str:
        
        for i in '(,_.)/:;-1234567890':
    
            string = string.replace(i, '')
     
        list_string = string.split(' ')
        return len(list_string)
    else:
        return str(string)

    
'''
quita todo tipo de signo posible al string
'''
def text(string):
    if type(string) == str:
        
        for i in '(,_.)/:;-1234567890':
    
            string = string.replace(i, '')
        return string
    else:
        str(string)
        