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


#Пердуперждение
warn = Label(window, text="Пароль сразу копируется в буфер обмена")
warn.pack()


#Получаем входные данные 
user_input = Entry(window, width=10)
user_input.pack(pady = 10)
user_input.focus()


#Вводим пока пустую переменную для пароля
final = StringVar()
final.set('')
final_key = Entry(window, textvariable=final)
final_key.pack(pady = 10)


password_arr = []
symbols = []


#Логическая часть
def Clicked():
	final_key.delete(0, 'end')
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

		secure_random = random.SystemRandom()
		for i in range (length):
			password_arr.append(secure_random.choice(symbols))

		return(''.join(password_arr))


	#Присваиваем пустой переменной парольное значение	
	password = Random_Symbols()
	final.set(password)	
	window.clipboard_clear()
	window.clipboard_append(password)


#Пишем кнопулю, которая запускает весь цирк
button = Button(window, text="Генерировать", command = Clicked)
button.pack(pady = 10)


#Продолжаем цикл окна(чтобы его не украли)
window.mainloop()