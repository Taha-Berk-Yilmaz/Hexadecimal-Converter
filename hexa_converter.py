#Created by Taha Berk Yilmaz.
#Date 11.07.2024
from tabulate import tabulate

try:
	headers = ['Operations', 'Definition']
	operation_list = [['Operations', 'Definition'], ['1', 'Hexadecimal to Number'], ['2', 'Number to Hexadecimal'], ['3', 'String to Hexadecimal'], ['4', 'Hexadecimal to String'], ['99', 'Exit']]
	table = operation_list
	print("Hello! This program is a converter between Hexadecimal, numbers and strings.")
	print(tabulate(table))
	
	while True:
		operation = input('Please enter the number of the operation you want: ')

		if operation == '1':
			hexa_str = input("Plese enter yout Hexadecimal code: ")
			num = int(hexa_str, 16)
			print(str(num)[0::])
		elif operation == '2':
			num = int(input("Please enter your number here:"))
			hexa_str = hex(num)
			print(str(hexa_str)[2::])
		elif operation == "3":
			string = bytes(input("Please enter your string here:").encode('utf-8'))
			print(str(string.hex())[2::])
		elif operation == "4":
			hexa = input("Please enter your Hexadecimal code here:")
			string = bytes.fromhex(hexa).decode('utf-8')
			print(string)
		elif operation == "99":
			print("\nExitted the program.")
			break
		else:
			print("\nYou entered an invalid operation. Please try again.\nIf you want exit please enter 99.")

except KeyboardInterrupt:
	print("\nExitted the program.")


#hexadecimal ==> 0 1 2 3 4 5 6 7 8 9 A B C D E F | A4B2C ==> A*16**4 + 4*16**3 + B*16**2 + 2*16**1 + C*16**0 ==> 674.604
#decimal ==> 0 1 2 3 4 5 6 7 8 9 | 4123 ==> 4*10**3 + 1*10**2 + 2*10**1 + 3*10**0 ==> 4123 || binary ==> 0 1 | 100110 ==> 32 + 4 + 2 ==> 38
