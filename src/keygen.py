import string 
import random 


length = int(input())
password = []
symbols = []


#Получаем массив с символами
for symbol in string.printable:
    symbols.append(symbol)
    
del symbols[95:100]


#Выбираем случайные символы из массива 
def Random_Symbols():

	for i in range (length+1):
		secure_random = random.SystemRandom()
		password.append(secure_random.choice(symbols))

	return(''.join(password))



password = Random_Symbols()
print(password)	
