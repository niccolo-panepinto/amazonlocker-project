from flask import Flask, render_template
from sensore import dato


#accedere a server flask mettendo http://127.0.0.1:5000/

app = Flask(__name__, template_folder= 'templates', static_folder='staticfiles')


#Pagine Main 
@app.route("/")
def main():

    print(dato.messaggio)

    return render_template('templates.html')


@app.route("/pacco")
def pacco():

    while True:
        ArrivatoPacco = dato.messaggio #Variabile dinamica per server html


        if ArrivatoPacco == 1:
            ArrivatoPacco = "Il pacco è presente nel locker!"
        if ArrivatoPacco == 0:   
            ArrivatoPacco = "Il pacco non è ancora presente nel locker."

        return render_template('il_tuo_pacco.html',ArrivatoPacco=ArrivatoPacco)
    



@app.route("/calcolatore")
def calcolatore():
    
    return render_template('calcolatore.html')


## verifica se è il programma principale
## e manda in esecuzione il web server su http://localhost:5000
# in questo caso in debug, ovvero si riavvia ad ogni cambiamento dei file
if __name__ == "__main__":
    app.run(debug=True, port=5000)





