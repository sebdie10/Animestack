import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



Config = {
  'apiKey': "AIzaSyBvyb76yPUN3rthAUw7xUpH_4FEovHlGtA",
  'authDomain': "animelist-a2905.firebaseapp.com",
  'databaseURL': "https://animelist-a2905-default-rtdb.firebaseio.com",
  'projectId': "animelist-a2905",
  'storageBucket': "animelist-a2905.appspot.com",
  'messagingSenderId': "281061517652",
  'appId': "1:281061517652:web:04db515987456eef7a40c1",
  'measurementId': "G-HGTMJCDB03"
}


cred = credentials.Certificate('./animelist-a2905-b050a568db0d.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()


"""dato={
    'nombre':'diego',
    'apellido':'garay'
}


#doc_ref = db.collection(u'users').document(u'seba')
#doc_ref.set(dato)

users_ref = db.collection(u'users').document(u'seba')
docs = users_ref.get()

#for doc in docs:
#    print(f'{doc.id} => {doc.to_dict()}')
print(docs.to_dict())"""


def GuardarUsuarioNuevo(id, datos):
    doc_ref = db.collection(u'users').document(id)
    informacion={
        'AnimesVistos':{},
        'datos': datos
    }
    doc_ref.set(informacion)


def LeerAnimes(id):
    coleccion = db.collection(u'users').document(id)
    coleccion = coleccion.get()
    animeinfo = coleccion.to_dict()
    animeinfo = animeinfo['AnimesVistos']
    print(animeinfo)
    return animeinfo


dotos = {
  'seb':{
    'nombre':'bleach',
    'imagen':'https://pics.filmaffinity.com/Bleach_Serie_de_TV-235942666-large.jpg'
    }
    }



dotos2 = {
  'animes':{
    'nombre':'bleach',
    'imagen':'https://pics.filmaffinity.com/Bleach_Serie_de_TV-235942666-large.jpg'
    }
    }
