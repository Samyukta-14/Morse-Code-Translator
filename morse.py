# Morse Code Translator

# Dictionary
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

def wtom(message):
    word = ''
    for i in message:
        if i != ' ':
            word += morse_dict[i.upper()] + ' '
        else:
            word += ' '
    return word

def mtow(message):
    message += ' '
    morse = ''
    code = ''
    x = 0
    for i in message:
        if (i != ' '):
            code += i
            x = 0
        else:
            x += 1
            if x == 2 :
                morse += ' '
            else:
                morse += list(morse_dict.keys())[list(morse_dict.values()).index(code)]
                code = ''
    return morse

def main():
    print("Hi, I am Encrypto here to help you out with your secret messages :)")
    print(" ")
    while True:
        print("To generate an encrypted message type 1.")
        print(" ")
        print("To decrypt a received morse code type 2.")
        print(" ")
        print("How would you like me to help you? ")
        choice=input()
        print("Great!!")
        message = input("You can now enter your message here: ")
        if choice == '1':
            result = wtom(message)
        elif choice == '2':
            result = mtow(message)
        else:
            result = "Invalid choice"
            continue
        print("Your message:",result)
        print("Do you want further assistance? (Yes/No)")
        loop=input().lower()
        if loop =='no':
            print("Okay, feel free to reach out to me anytime you need help with your secret messages. Goodbye!")
            break

if __name__ == '__main__':
    main()
