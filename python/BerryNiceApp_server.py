from flask import Flask, jsonify, request
import mysql.connector as mysql
import functions_for_api_server as functions
from flask_cors import CORS

from logging import FileHandler,WARNING

# connecting to the mysql database
mydb = mysql.connect(
    host="154.49.137.221",
    user="Nikita",
    password="CheeseTax",
    database="berry_nice",
    auth_plugin="mysql_native_password"
)

app = Flask(__name__, template_folder= 'template')

file_Handler = FileHandler('errorlog.txt')
file_Handler.setLevel(WARNING)

app.route('/')
CORS(app)

# get all customers from the mybusiness.customer
@app.route('/berry_data')
def get_data():
    data = functions.getalldata()
    return jsonify(data)

@app.route('/map_data')
def get_map_data():
    data = functions.getmapdata()
    return jsonify(data)

@app.route('/berry_data_post', methods=['POST'])
def berry_post():
    print("posting")
    data = request.json
    my_post = functions.posting_berry_data(data)

    return jsonify(my_post)


if __name__ == '__main__':
    app.run()