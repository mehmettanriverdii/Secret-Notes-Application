characters = "qwertyuıopğüasdfghjklşizxcvbnmöç0123456789><#£$½{[]}-|@€₺"
def encode(value:str)->str:
    new_text = ""
    for i in value:
        for j in range(len(characters)):
            if(i == characters[j]):
                new_text = new_text + (characters[(j + 3) % len(characters)])
    return new_text
def decode(value:str)->str:
    new_text = ""
    for i in value:
        for j in range(len(characters)):
            if (i == characters[j]):
                new_text = new_text + (characters[(j - 3) % len(characters)])
    return new_text
