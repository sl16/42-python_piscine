import sys

def countChars(str: str):
	upper = 0
	lower = 0
	punct = 0
	spaces = 0
	digits = 0

	punct_list = "!”#$%&'()*+,-./:;<=>?@[\\]^_`{|}~\""

	for char in str:
		if char.isupper():
			upper += 1
		elif char.islower():
			lower += 1
		elif char.isdigit():
			digits += 1
		elif char.isspace():
			spaces += 1
		elif char in punct_list:
			punct += 1

	print(
		f"The text contains {len(str)} characters:\n"
		f"\t{upper} upper letters\n"
		f"\t{lower} lower letters\n"
		f"\t{punct} punctuation marks\n"
		f"\t{spaces} spaces\n"
		f"\t{digits} digits")

def main():
	"""
	Provides the sums of upper-case characters, lower-case
	characters, punctuation characters, digits and spaces provided in the argv.
	"""
	try:
		# If nothing is provided, the user is prompted to provide a string
		if len(sys.argv) == 1:
			try:
				text = input("What is the text to count?\n")
			except EOFError:
				text = ""
		else:
			# If more than one argument is provided, raise an AssertionError
			assert len(sys.argv) == 2, "Please provide only one argument."
			text = sys.argv[1]

		countChars(text)
		return (0)

	except AssertionError as e:
		print(e)
		return (1)

if __name__ == "__main__":
	main()