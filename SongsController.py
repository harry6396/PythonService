import flask
from flask import Flask
import json
import mysql.connector
import os

app = Flask(__name__)

# to get the user details for the login


@app.route("/")
def hello1():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="harry",
        database="SongsCollection"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM SongDetails WHERE RANK <= 50 ORDER BY RANK")

    myresult = mycursor.fetchall()
    iCounter=0
    data={}

    for doc in myresult:
        data[iCounter] = doc
        iCounter = iCounter + 1

    return flask.jsonify(json.dumps({'status':data}))


@app.route("/<string:searchKeyWord>")
def hello(searchKeyWord):
    mydb = mysql.connector.connect(
        host="sql12.freemysqlhosting.net",
        user="sql12280554",
        passwd="qCu4mBHg3I",
        database="sql12280554"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM SongDetails WHERE RANK <= 50 AND (ARTISTS LIKE '%"+searchKeyWord+"%' OR NAME LIKE '%"+searchKeyWord+"%') ORDER BY RANK")

    myresult = mycursor.fetchall()
    iCounter=0
    data={}

    for doc in myresult:
        data[iCounter] = doc
        iCounter = iCounter + 1

    return flask.jsonify(json.dumps({'status':data}))

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)



