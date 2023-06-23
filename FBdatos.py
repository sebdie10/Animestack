from firebase import  Firebase



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



def RegistrarUsuario(email, password, datos): #Esto anda no tocar mas
    fb = Firebase(Config)
    auth = fb.auth()
    auth.create_user_with_email_and_password(email, password)
    print(datos['username'])
    


    
def loginUsuario(email, password):
    fb = Firebase(Config)
    auth = fb.auth()
    user = auth.sign_in_with_email_and_password(email, password)
    dat = auth.get_account_info(user['idToken'])
    da = dat['users']
    di = da[0]
    token_id = di['localId']
    return token_id





