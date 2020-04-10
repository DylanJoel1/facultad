def esPrimo(num): #funcion para calcular si un numero es primo
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True  
        
print('ingrese la palabra: ')
lista=[]
palabra = input().lower()

letras_sin_repetir = set(palabra)
for i in letras_sin_repetir:
	lista.append((i,palabra.count(i))) #me guardo en la lista la letra junto a la cantidad de veces que se repite.
for letra in lista:
	if (esPrimo(letra[1])): #si es primo devuelve true, caso contrario false.
		print('la letra: '+'"'+ letra[0]+'"' +' aparece: ' + str(letra[1]) + ' veces. Por lo tanto aparece un numero primo de veces.')
	else:
		print('la letra: '+'"'+ letra[0]+'"' + 'aparece: ' + str(letra[1]) + ' veces. Por lo tanto no aparece un numero primo de veces.')

	
	
