morse_symbols = {"a": ".-",
                 "b": "-...",
                 "c": "-.-.",
                 "d": "-..",
                 "e": ".",
                 "f": "..-.",
                 "g": "--.",
                 "h": "....",
                 "i": "..",
                 "j": ".---",
                 "k": "_._",
                 "l": ".-..",
                 "m": "--",
                 "n": "-.",
                 "o": "---",
                 "p": ".--.",
                 "q": "--.-",
                 "r": "--.-",
                 "s": "...",
                 "t": "-",
                 "u": "..-",
                 "v": "...-",
                 "w": ".--",
                 "x": "-..-",
                 "y": "-.--",
                 "z": "--..",
                 "å": ".--.-",
                 "ä": ".-.-",
                 "ö": "---.",
                 "1": ".----",
                 "2": "..---",
                 "3": "...--",
                 "4": "....-",
                 "5": "....",
                 "6": "-....",
                 "7": "--...",
                 "8": "---..",
                 "9": "----.",
                 "0": "-----",
                 "error": "........",
                 "&": ".-...",
                 "'": ".----.",
                 "@": ".--.-.",
                 ")": "-.--.-",
                 "(": "-.--.",
                 ":": "---...",
                 ",": "--..--",
                 "=": "-...-",
                 "!": "-.-.--",
                 ".": ".-.-.-",
                 "-": "-....-",
                 "*": "-..-",
                 "%": "----- -..-. -----",
                 "+": ".-.-.",
                 '"': ".-..-.",
                 "?": "..--..",
                 "/": "-..-.",
                 }

space_for_letters = " "
space_for_words = "/"
no_translation = "Error"


print("""Welcome to text to international morse code.\n
         ' ' space means space between symbols.
         / slash means space between words.
         "Error" means no symbol found at translation table. \n""")


def text_to_morse():
    morsed_string = ""
    text_to_be_morsed = input("Type the text to be morsed:").lower()
    print("Morse for chacter:")
    for char in text_to_be_morsed:

        if char == " ":
            print(space_for_words)
            morsed_string = morsed_string[:-1]
            morsed_string += space_for_words
        else:
            try:
                print(char, morse_symbols[char])
                morsed_string += morse_symbols[char]
                morsed_string += " "
            except KeyError:
                print(char, no_translation)
                morsed_string += no_translation
    print("The whole text morsed:")
    print(morsed_string)
    choice = input("Do you want to tranlate another text? (y/n): ").lower()
    if choice == "y":
        text_to_morse()
    else:
        print("Have a nice day! Bye, bye!")


text_to_morse()
