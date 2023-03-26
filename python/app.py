from flask import Flask, request, jsonify
import mysql.connector as mysql
import functions_for_api as functions

# connecting to the mysql database
mydb = mysql.connect(
    host="localhost",
    port="3306",
    user="root",
    password="Kg39562K!jkm",
    database="mybusiness",
    auth_plugin="mysql_native_password"
)

# cursor for making the changes
mycursor = mydb.cursor()

app = Flask(__name__)

app.route('/')

# get one customer with matching id from the mybusiness.customer
@app.route('/customers/<customer_id>')
def get_specific_customer(customer_id):
    my_customer = functions.getSpecificCustomer(customer_id)
    return jsonify(my_customer), 200