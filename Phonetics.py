import sys

def main():
	phonetics = {
    'a': 'alpha', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliet',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray',
    'y': 'yankee', 'z': 'zulu',
	}

	msg = input("Message: ")
	print()
	for char in msg:
		if char.lower() in phonetics:		
			print(char.lower() + ": " + phonetics[char.lower()])
		elif char == " ":
			print()
		else:
			print(char.lower() + ": ?")
	
	print()
	main()


if __name__ == "__main__":
	main()
