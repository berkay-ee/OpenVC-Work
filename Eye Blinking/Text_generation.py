MORSE_ALPHABET = {
    ".-"   : "A",
    "-..." : "B",
    "-.-." : "C",
    "-.."  : "D",
    "."    : "E",
    "..-." : "F",
    "--."  : "G",
    "...." : "H",
    ".."   : "I",
    ".---" : "J",
    "-.-"  : "K",
    ".-.." : "L",
    "--"   : "M",
    "-."   : "N",
    "---"  : "O",
    ".--." : "P",
    "--.-" : "Q",
    ".-."  : "R",
    "..."  : "S",
    "-"    : "T",
    "..-"  : "U",
    "...-" : "V",
    ".--"  : "W",
    "-..-" : "X",
    "-.--" : "Y",
    "--.." : "Z"
}

MORSE_NUMBERS = {
    "-----" : "0",
    ".----" : "1",
    "..---" : "2",
    "...--" : "3",
    "....-" : "4",
    "....." : "5",
    "-...." : "6",
    "--..." : "7",
    "---.." : "8",
    "----." : "9"
}

morse = ""


def alfabet_generation(time):
    global morse
    
    if time < 0.25:
        morse += "."
        print("dot")
    elif time < 0.4:
        morse += "-"
        print("dash")
    else:
        if morse == "":
            return
        else:
            print(MORSE_ALPHABET[morse])
            morse = " "
        
    
    
def enter_alfabet_mode():
    print("alfabet mode")
    
def enter_text_mode():
    print("TEXT MODE")
    