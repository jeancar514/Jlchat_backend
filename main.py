from flask import Flask, request,jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import asyncio
from flask_cors import CORS, cross_origin

# Use a service account
cred = credentials.Certificate('jlchat-3aedd-firebase-adminsdk-d0ifu-f2840d5d46.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

CORS(app)

@cross_origin()
@app.route("/usuarios", methods=['GET','POST'])
def usuarios():
    usuario = request.json
    metodo = "adicionar"
    usuariodb = {}
    # Add a new doc in collection 'cities' with ID 'LA'
    
    def añadir_usuario(usuario):
        db.collection("usuarios").add(usuario)

    def obtener_usuario(usuario):
        usuario = db.collection("usuario").where("passwork", "==",usuario["passwork"]).get()
        return usuario

    if (metodo == "adicionar"):
        añadir_usuario(usuario)
    if (metodo == "obtener"):
        for doc in obtener_usuario(usuario):
            usuariodb = doc.to_dict()
            print(usuariodb)
    
    return "leo"
    
@cross_origin()
@app.route("/mensajes", methods=['GET','POST'])
def mensajes():
    mensaje = request.json
    metodo = "adicionar"
    mensajesdb = {}
    # Add a new doc in collection 'cities' with ID 'LA'
    
    def añadir_mensaje(mensaje):
        db.collection("mensajes").add(mensaje)

    def obtener_mensajes(mensaje):
        docs = db.collection("mensajes").where("id", "==",mensaje["id"]).get()
        return docs.to_dict()

    if (metodo == "adicionar"):
        añadir_mensaje(mensaje)
        for doc in obtener_mensajes(mensaje):
            mensajesdb = doc.to_dict()

    if (metodo == "obtener"):
        for doc in obtener_mensajes(mensaje):
            mensajesdb = doc.to_dict()
    
    return "leo"
    
@cross_origin()
@app.route("/publicaciones", methods=['GET','POST'])
def publicaciones():
    publicacion = request.json
    metodo = ""
    publicacionesdb = {}
    # Add a new doc in collection 'cities' with ID 'LA'
    
    def añadir_publicacion(publicacion):
        db.collection("publicaciones").add(publicacion)

    def obtener_publicaciones(userid):
        docs = db.collection("publicaciones").where("userid", "==",userid).get()
        return docs.to_dict()

    if (metodo == "añadir"):
        añadir_publicacion(publicacion)
        for doc in obtener_publicaciones(publicacion["userid"]):
            mensajesdb = doc.to_dict()

    if (metodo == "obtener"):
        for doc in obtener_mensajes(mensaje):
            mensajesdb = doc.to_dict()
    
    return "leo"

@cross_origin()
@app.route("/amigos", methods=['GET','POST'])
def amigos():
    amigo = request.json
    metodo = "adicionar"
    amigosdb = {}
    # Add a new doc in collection 'cities' with ID 'LA'
    
    def adicionar_amigo(amigo):
        db.collection("amigo").add(amigo)

    def obtener_publicaciones(userid):
        docs = db.collection("publicaciones").where("userid", "==",userid).get()
        return docs.to_dict()

    if (metodo == "adicionar"):
        adicionar_publicacion(publicacion)
        for doc in obtener_publicaciones(publicacion["userid"]):
            mensajesdb = doc.to_dict()

    if (metodo == "obtener"):
        for doc in obtener_mensajes(mensaje):
            mensajesdb = doc.to_dict()
    
    return "leo"
app.run(debug=True)