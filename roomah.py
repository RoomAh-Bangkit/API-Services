from flask import Flask, jsonify, redirect, url_for, request, session, flash
from flask_mysqldb import MySQL, MySQLdb
import bcrypt
import werkzeug

app = Flask(__name__)
mysql = MySQL(app)
app.secret_key = "RoomahFlask"

app.config["MYSQL_HOST"] = '10.74.65.3'
app.config['MYSQL_UNIX_SOCKET'] = "/cloudsql/roomah-351214:us-east1:roomah-project"
app.config["MYSQL_USER"] = 'user'
app.config["MYSQL_PASSWORD"] = 'roomah'
app.config["MYSQL_DB"] = 'roomah'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

def db_write(query, params):
            cursor = mysql.connection.cursor()
            try:
                cursor.execute(query, params)
                mysql.connection.commit()
                cursor.close()

                return True

            except pymysql._exceptions.IntegrityError:
                cursor.close()
                return False

@app.route('/register', methods=['POST', 'GET'])
def register():
        name = request.form['Name']
        email = request.form['Email']
        password = request.form['Password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())

        if db_write(
        """INSERT INTO user (Name,Email,Password) VALUES (%s,%s,%s)""" ,(name, email, hash_password)
        ):
            return jsonify({"error": False, "message": "User Created"})
        else:
            return jsonify({"error": True, "message": "User Not Created"})

            
if __name__ == '__main__':
    app.run(debug=True)