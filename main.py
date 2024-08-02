meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL" : "una respuesta a una broma",
            "SHEESH":"ligera desaprobacion",
            "CREEPY":"aterrador,siniestro",
            "AGGRO":"ponerse agresivo/enojado"
            }
for i in range(5):
  
  word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print("Significa:"+meme_dict[word])
else:
    print("No se ha encontrado esa palabra,prueba con otra")
