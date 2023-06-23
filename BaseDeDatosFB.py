import firebase_admin
from firebase_admin import firestore, credentials
#import ast

cred = credentials.Certificate("cred.json")
firebase_admin.initialize_app(cred)


db = firestore.client()




def agregarUsuarioABase(token_id):
    doc_ref = db.collection(u'ListaAnimesUsuarios').document(token_id)
    doc_ref.set({'nombre': 'animes'})

def leerdatos(token_id):
    animesVistos = {}
    users_ref = db.collection(u'ListaAnimesUsuarios')
    docs = users_ref.stream()
    for doc in docs:
        if doc.id == token_id:
            animesVistos = doc.to_dict()        
    return animesVistos

    

def agregarAnimeUsuario(token_id, anime):
    doc_ref = db.collection(u'ListaAnimesUsuarios').document(token_id)
    doc_ref.set(anime)
    print("\n Se sobre-escribio la base de datos \n")



def ordenarDiccionario(listaDeDicionarios, token_id):
    dicglobal = {}
    n = len(listaDeDicionarios)
    if n == 1:
        dicglobal[listaDeDicionarios[0]['nombre']] = listaDeDicionarios[0]
        agregarAnimeUsuario(token_id, dicglobal)
    else:
        dicglobal = listaDeDicionarios[0]
        dicglobal[listaDeDicionarios[1]['nombre']] = listaDeDicionarios[1]
        agregarAnimeUsuario(token_id, dicglobal)

#agregarAnimeUsuario('AM9HpP5ks3OM23yQErhTPuZkrto2', dic )