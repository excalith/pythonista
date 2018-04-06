def main():

	morse = {
		'A': '.-',
		'B': '-...',
		'C': '-.-.',
		'Ç': '-.-.',
		'D': '-..',
		'E': '.',
		'F': '..-.',
		'G': '--.',
		'Ğ': '--.',
		'H': '....',
		'I': '..',
		'İ': '..',
		'J': '.---',
		'K': '-.-',
		'L': '.-..',
		'M': '--',
		'N': '-.',
		'O': '---',
		'Ö': '---',
		'P': '.--.',
		'Q': '--.-',
		'R': '.-.',
		'S': '...',
		'Ş': '...',
		'T': '-',
		'U': '..-',
		'Ü': '..-',
		'V': '...-',
		'W': '.--',
		'X': '-..-',
		'Y': '-.--',
		'Z': '--..',
		'0': '-----',
		'1': '.----',
		'2': '..---',
		'3': '...--',
		'4': '....-',
		'5': '.....',
		'6': '-....',
		'7': '--...',
		'8': '---..',
		'9': '----.',
		".": ".-.-.-",
		",": "--..--",
		":": "---...",
		"!": "-.-.--",
		"?": "..--..",
		"'": ".----.",
		"-": "-....-",
		"/": "-..-.",
		"@": ".--.-.",
		"=": "-...-"
	}

	msg = input("Message: ")
	print()
	for char in msg:
		if char.upper() in morse:		
			print(char.upper() + ": " + morse[char.upper()])
		elif char == " ":
			print()
		else:
			print(char.upper() + ": ?")
	
	print()
	main()


if __name__ == "__main__":
	main()
