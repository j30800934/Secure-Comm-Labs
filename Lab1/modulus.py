
def modulus_of(a,b):
	try:
		if not isinstance(a, int) | isinstance(b,int):
			raise TypeError("The two numbers must be positive integers")
		if (a <= 0 | b <= 0 ):
			raise valueError("The two numbers must be greater than 0")

		result = a % b

		return result
	
	except TypeError as te:
		print(f"The numbers must be integers. {te}")
	except ValueError as ve:
		print(f"The numbers must not be less than 0 {ve}")
	except Exception  as  e:
		print(f"An unexpected  error occured  {e}")

number = modulus_of(53431, 553)

if number:
	print(number)