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

'''
crear wordcloud
parametros: columna a crear wordcloud, titulo de la imagen, numero de palabras en la imagen
'''
def create_WC(data, title, words=25, _filter=True):
    
    if _filter:
            text_filter=data.apply(fj.text)
    else:
        text_filter = data

    
    StopWords = set(stopwords.words('english'))

    text_nlp = ' '.join(text_filter)
    wordcloud = WordCloud(background_color='white',
        stopwords=StopWords,
        max_words=words,
        max_font_size=200, 
        scale=3,
        random_state=3).generate(str(text_nlp))
    wordcloud.recolor(random_state=1)
    plt.figure(figsize=(20, 15))
    plt.title(title, fontsize=25,color='black')
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
        