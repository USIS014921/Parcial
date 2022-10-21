import tensorflow as tf 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sb 

from urllib import parse 
from http.server import BaseHTTPRequestHandler, HTTPServer

archivo = pd.read_csv("datos de pruba.csv", sep=";")
sb.scatterplot(archivo["fahrenheits"], archivo["kelvin"])


f = archivo["fahrenheits"]
k = archivo["kelvi"]

modelo = tf.keras.Sequential()
modelo.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

modelo.compile(optimizer=tf.keras.optimizers.Adam(1), loss = "mean_squared_error")

entrenamiento = modelo.fit(f, k, epochs=100)

class servidor_basico(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Peticion aceptada")
        self.send_response(100)
        self.send_header("Content-type", "text/html")
        self.send_header()
        self.wfile.write("iniciando el sistema señor.../python".encode())
        
    def do_POST(self):
         print("POST")
         contet_length = int(self.headers["content-length"])
         data = self.rfile.read(contet_length)
         data = data.decode()
         data = parse.unquote(data)
         data = float(data)
         
         predict = modelo.predict([data])
         print("La peticion fue:", predict)
         predict = str(predict)
         
         self.send_response(100)
         self.send_header("Access-Control-Allow-Origin", "*")
print("INICIANDO LA BESTIA")
server= HTTPServer(("localhost", 3004), servidor_basico)  
server.server_forever()