import json
dic ={
    'Bleach':{
        "imagen" : "https://pics.filmaffinity.com/Bleach_Serie_de_TV-235942666-large.jpg",
        "ID" : "1",
        "nombre":"Bleach",
        "descripcion":"El mejor segador de almas sustituto"
    },
    'Naruto' :{
        "imagen":"https://www.formulatv.com/images/series/posters/100/135/dest_1.jpg",
        "ID":"2",
        "nombre":"Naruto",
        "descripcion":"Sere hokage de veras"
    },
    'Boku no hero':{
        "imagen":"https://www.crunchyroll.com/imgsrv/display/thumbnail/480x720/catalog/crunchyroll/7e023c55c6cb63b2ecbb31b6aae9bf12.jpe",
        "ID" : "3",
        "nombre":"Boku no hero",
        "descripcion":"Plus ultra"
    }

}

#js= {'nombre':'garay'}


def escribir_json(js):
 with open('AnimesEnplataforma.json','w') as r:
   json.dump(js, r, indent = 4)

def leer_json():
  with open('AnimesEnPlataforma.json','r') as r:
    leer = json.load(r)
    return leer

