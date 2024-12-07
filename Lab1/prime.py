

def prime_number(limit):
	try:
		# Ensure that the limit is positive number
		if not isinstance(limit, int):
			raise TypeError("limit must be an integer.")
		if limit <= 0:
			raise ValueError("limit must be greater than 0.")		
		result=[]
		n=1
		p=6
		while n < limit:
			val1 = p * n - 1
			if(val1 < limit):
				result.append(val1)
			val2 = p * n + 1
			if(val2 < limit):
				result.append(val2)
			n += 1
		return result 
	except TypeError as te:
		print(f"Type Error: {te}")
	except ValueError as ve:
		print(f"Value Error: {ve}")
	except Exception as e:
		print(f"An unexpected error occured: {e}")

#number = prime_number(20)
#if number:
#	print(number)
