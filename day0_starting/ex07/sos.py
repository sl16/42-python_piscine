import sys

def translate(string: str):
	morse_dict = {	'A':'.-',
					'B':'-...',
					'C':'-.-.',
					'D':'-..',
					'E':'.',
					'F':'..-.',
					'G':'--.',
					'H':'....',
					'I':'..',
					'J':'.---',
					'K':'-.-',
					'L':'.-..',
					'M':'--',
					'N':'-.',
					'O':'---',
					'P':'.--.',
					'Q':'--.-',
					'R':'.-.',
					'S':'...',
					'T':'-',
					'U':'..-',
					'V':'...-',
					'W':'.--',
					'X':'-..-',
					'Y':'-.--',
					'Z':'--..',
					'1':'.----',
					'2':'..---',
					'3':'...--',
					'4':'....-',
					'5':'.....',
					'6':'-....',
					'7':'--...',
					'8':'---..',
					'9':'----.',
					'0':'-----',
					' ':'/'}
	
	encrypted_string = ""

	for c in string:
		encrypted_string += morse_dict.get(c.upper()) + " "

	return encrypted_string

def main():
	"""
	Accepts a string and prints it in Morse code.
	
	Supports only space and alphanumeric characters.
	"""
	try:
		# Check if the correct number of arguments is provided
		assert (len(sys.argv) == 2), ("Provide 1 argument (string to convert)")

		# Check if the string only contains alphanum chars and spaces
		assert (all(c.isalnum() or c.isspace() for c in sys.argv[1])), (
		"The string must only include alphanumeric characterss and spaces")

		print(translate(sys.argv[1]))
		
	except AssertionError as e:
		print(f"AssertionError: {e}")
	except ValueError as e:
		print(f"ValueError: {e}")


if __name__ == "__main__":
	main()