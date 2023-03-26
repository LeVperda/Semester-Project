from flask import Flask, jsonify
import mysql.connector as mysql
import functions_for_api as functions

# connecting to the mysql database
mydb = mysql.connect(
    host="localhost",
    port="3306",
    user="root",
    password="Kg39562K!jkm",
    database="berry_nice",
    auth_plugin="mysql_native_password"
)

app = Flask(__name__)

app.route('/')

# get all customers from the mybusiness.customer
@app.route('/berry_data')
def get_data():
    data = functions.getalldata()
    return jsonify(data)