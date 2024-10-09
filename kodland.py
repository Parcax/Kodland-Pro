None

meme_dict = {
    "CRINGE" : "Algo Excepcionalmente raro o embarazoso",
    "LOL" : "Una respuesta común a algo gracioso",
    "ROFL" : "Una respuesta a una broma",
    "SHEESH" : "Ligera desaprobación",
    "CREEPY" : "Aterrador, Siniestro",
    "AGGRO" : "Ponerse agresivo/enojado",
}

word = input("Escribe una palabra que no entiendas (EN MAYUSCULAS!)")

for i in range(1):
    if word in meme_dict.keys():
        print(meme_dict[word])
    
    else:
        print("La palabra no se encuentra o esta mal escrita")
