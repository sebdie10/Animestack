'''importar librerias Flask'''
import flask
from flask import request, redirect, session

'''Base de datos'''
from FBdatos import  RegistrarUsuario, loginUsuario
from BaseAnimes import dic
from BaseDeDatosFB import leerdatos, agregarAnimeUsuario, ordenarDiccionario

'''Parseo de Diccionarios'''
import ast





'''instancia de flask'''
app = flask.Flask(__name__)
app.secret_key = 'cortina'




'''paginas de referencias'''
@app.errorhandler(404) #PAgina no encontrada
def paginaNoEncontrada(e):
    return flask.render_template('404page.html')

@app.route('/') # PAgina de inicio
def inicio():
    if 'token_id' in session:
        return redirect('/list')
    else:
        return redirect('/login')





'''---Rutas funcionales e interactivas---'''



'''Rutas de credenciales'''
@app.route('/login') #Ruta Login para ingresar con credenciales
def login():
    if 'token_id' in session:
        return redirect('/list')
    #variable para determinar si las credenciales son incorrectas
    Email = request.args.get('email')
    contraseña = request.args.get('contraseña') 
    if Email != None and contraseña !=None:   
        print(Email)
        print(contraseña)
        try:
            token_id = loginUsuario(Email, contraseña)
            session['token_id'] = token_id
            #AnimesVistos.append(leerdatos(token_id))
            return redirect('/list')
        except:
            Incorrecta = True #variable para determinar si las credenciales son incorrectas
            return flask.render_template('logi.html', Incorrecta = Incorrecta)
    
    else:
        return flask.render_template('logi.html')
    

@app.route('/logout')
def cerrarSesion():
    print(session['token_id'])
    session.clear()
    return redirect ('/list')



@app.route('/register', methods=['GET', 'POST']) #esto anda no tocar mas
def registro():
    Email = request.args.get('email')
    contraseña = request.args.get('contraseña')
    nombre = request.args.get('nombre')
    apellido = request.args.get('apellido')
    username = request.args.get('username')

    if Email != None and contraseña !=None:
        print(Email)
        print(contraseña)
        
        datos = {
            'Email': Email,
            'nombre' : nombre,
            'apellido': apellido,
            'username': username

        }
        RegistrarUsuario(Email, contraseña, datos)

    return flask.render_template('registro.html')


'''---Fin rutas de credenciales---'''







@app.route('/list')
def list():
    if not 'token_id' in session:
        token = 0
    else:
        token = session['token_id']
    return flask.render_template("listAnime.html", dicis = dic, token_id=token)


@app.route('/plantilla')
def plantilla():
    return flask.render_template("plantilla.html", token_id=session['token_id'])


@app.route('/ba',methods=['GET','POST']) #informacion de anime en un 25% armado
def info():
    anime = request.args.get('anime')
    if 'token_id' in session:
        animesVistosporUsuario = leerdatos(session['token_id'])
        token_id = session['token_id']
        if anime in animesVistosporUsuario:
            AnimeEnLista = False
        else:
            AnimeEnLista = True
    else:
        token_id = 0
        AnimeEnLista = True
    
    biblioteca= dic
    return flask.render_template("Animeinfo.html",token_id = token_id, anime= biblioteca[anime], AnimeEnLista = AnimeEnLista)



@app.route('/agregar',methods=['GET','POST']) #funcion agregar ya quedo lista
def agregarAnime():
    anime = request.args.get('anime')
    anime = ast.literal_eval(anime)
    
    url = anime['nombre']
    diccionarioLista = []
    diccionarioLista.append(leerdatos(session['token_id']))
    
    if not diccionarioLista[0]:
        diccionarioLista.pop()
    diccionarioLista.append(anime)

    ordenarDiccionario(diccionarioLista, session['token_id'])
    

    return redirect('/ba?anime='+url)




@app.route('/profile') #Perfil aun sin maquetar ya se muestran los animes vistos
def perfil():
    if 'token_id' in session:
      AnimesVistosUsuario = leerdatos(session['token_id'])
      token_id = session['token_id']
    else:
        token_id = 0
        AnimesVistosUsuario = {}
    return flask.render_template('perfil.html',token_id = token_id, animes = AnimesVistosUsuario)






if __name__ == '__main__':
    app.run(host='0.0.0.0' ,debug = True)