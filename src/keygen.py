import string 
import random 
from tkinter import *


#Параметры окна
window = Tk()
window.title("Keygen")
window.geometry('400x200')


#Заголовок
key_length = Label(window, text="Введите длину пароля")
key_length.pack()


#Получаем входные данные 
user_input = Entry(window, width=10)
user_input.pack()
user_input.focus()


#Вводим пока пустую переменную для пароля
final = StringVar()
final.set('')
final_key = Entry(window, textvariable=final)
final_key.pack()


password_arr = []
symbols = []


#Логическая часть
def Clicked():


	#Переводим входные данные в нужный формат
	length = int(user_input.get())	


	#Получаем массив с символами
	for symbol in string.printable:
		symbols.append(symbol)


	#Убираем лишние
	del symbols[95:100]
	del symbols[86]



	#Выбираем случайные символы из массива 
	def Random_Symbols():

		for i in range (length):
			secure_random = random.SystemRandom()
			password_arr.append(secure_random.choice(symbols))

		return(''.join(password_arr))


	#Присваиваем пустой переменной парольное значение	
	password = Random_Symbols()
	final_key.delete(0, 'end')
	final.set(password)	


#Пишем кнопулю, которая запускает весь цирк
button = Button(window, text="Генерировать", command = Clicked)
button.pack()

#Продолжаем цикл окна(чтобы его не украли)
window.mainloop()