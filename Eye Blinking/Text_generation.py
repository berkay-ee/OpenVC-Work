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


TEXT = {
    "."     : "yes",
    "-"     : "no",
    ".."    : "lunch",
    "--"    : "water",
    ".-"    : "toilet",
    "..."   : "coffe"
}


morse = ""
text  = ""


def alfabet_generation(time):
    global morse
    
    if time < 0.25:
        morse += "."
        print("dot")
    elif time < 0.4:
        morse += "-"
        print("dash")
    else:
        if morse in MORSE_ALPHABET:
            print(MORSE_ALPHABET[morse])
            morse = ""
        else:
            morse = ""
        
    
    
def enter_alfabet_mode():
    print("alfabet mode")
    
def enter_text_mode(time):
    global text
    
    if time < 0.25:
        text += "."
        print("dot")
    elif time < 0.4:
        text += "-"
        print("dash")
    else:
        if text in TEXT:
            print(TEXT[text])
            text = ""
        else:
            text = ""
    
    