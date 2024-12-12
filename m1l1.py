meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "CREPPY": "algo aterrador o siniestro",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print("El significado de", word, "es:", meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
     print("Lo siento, no tengo el significado de", word,)
