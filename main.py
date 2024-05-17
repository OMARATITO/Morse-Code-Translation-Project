morse_en = {"a": "*-", "b": "-***", "c": "-*-*", "d": "-**", "e": "*", "f": "**-*", "g": "--*", "h": "****", "i": "**",
            "j": "*---", "k": "-*-", "l": "*-**", "m": "--", "n": "-*", "o": "---", "p": "*--*", "q": "--*-",
            "r": "*-*", "s": "***", "t": "-", "u": "**-", "v": "***-", "w": "*--", "x": "-**-", "y": "-*--",
            "z": "--**"}

morse_ar = {"ا": "*-", "ب": "-***", "ت": "-", "ث": "-*-*", "ج": "*---", "ح": "****", "خ": "---", "د": "-**",
            "ذ": "--**", "ر": "*-*", "ز": "---*", "س": "***", "ش": "----", "ص": "-**-", "ض": "***-", "ط": "**-",
            "ظ": "-*--", "ع": "*-*-", "غ": "--*", "ف": "**-*", "ق": "--*-", "ك": "-*-", "ل": "*-**", "م": "--",
            "ن": "-*", "ه": "**-**", "و": "*--", "ي": "**", "ء": "*", "ئ": "*", "ؤ": "*", "ة": "**-**", "ى": "**",
            "إ": "*-", "أ": "*-"}

symbols = {"0": "-----", "1": "*----", "2": "**---", "3": "***--", "4": "****-", "5": "*****", "6": "-****",
            "7": "--***", "8": "---**", "9": "----*", " ": " ", ".": "*-*-*-", ",": "--**--", "،": "--**--",
            ";": "--**--", "؛": "--**--", ":": "---***", "?": "**--**", "!": "-*-*--", "-": "-****-", "/": "-**-*",
            "(": "-*--*-", ")": "-*--*-", '"': "*-**-*", "'": "*----*", "`": "*----*", "+": "*-*-*", "=": "-***-",
            "_": "**--*-", "$": "***-**-", "@": "*--*-*", "&": "*-***"}

print("===============\nMorse Code Translation\n===============")

def morse(text, dict):
    message = ""
    for letter in text:
        if letter == " ":
            message += "| "
        elif letter in symbols:
            message += symbols[letter] + " "
        else:
            message += dict[letter] + " "
    return message



def translate(message):
    chars = ""
    for letter in message:
        if letter in morse_en:
            chars += "e"
        elif letter in morse_ar:
            chars += "a"
        elif letter in symbols:
            pass
        else:
            chars += "f"


    if "f" in chars:
        print("your message includes unsupported letters")
    elif "e" in chars and "a" in chars:
        print("your message has mixed languages")
    elif "e" in chars:
        print(morse(message, morse_en))
    elif "a" in chars:
        print(morse(message, morse_ar))
    else:
        print(morse(message, symbols))


while True:
    text = input("please enter your message: ").lower()
    if text == "exit":
        print("FINNISH")
        break
    else:
        translate(text)
# this is my Morse Code Translation Project
