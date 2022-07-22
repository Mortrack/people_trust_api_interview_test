"""
This program contains a simple REST API implementation, with Flask, to receive
numeric data through a POST request on a specific end point to then store it in
a txt file. In addition, if a GET request is made for another specific end
point, it will then sum all the numeric values contained in that txt file to
then return the result in JSON format.

AUTOR: César Miranda Meza
DATE OF CREATION: July 22, 2022.
LAST UPDATE: N/A.
"""

from flask import Flask, request
from flask_restful import Resource, Api
from pathlib import Path
import os

app = Flask(__name__)
api = Api(app)

file_name = 'data.txt'

class EndPointOne(Resource):
    def post(self):
        """Retrieves a numeric data through a POST request.

        Args:
            number: Contained in the POST request body to store a numberic value.

        Returns:
            An empty string and the corresponding Status Code.

        Raises:
            IndexError: If the \'number\' index of the POST request does not exist.
            TypeError: If no numeric value is received through the POST request.
        """
        # We retrieve the POST request received on this end point and then
        # validate having received the right type of value in the right index.
        data = request.get_json()
        try:
            if not data['number'].isnumeric():
                raise TypeError("Only numeric values are allowed for the \'number\' index of the POST request.")
        except:
            raise IndexError("It is expected to send data through the \'number\' index of the POST request")
        
        # We create a file named as 'data.txt'.
        if not os.path.exists(file_name):
            Path(file_name).touch()
        
        # We read the content of the file 'data.txt'.
        with open(file_name, 'r') as f:
            current_data = f.read()
        
        # We rewrite the file with its previous content and add the new number
        # that was received through the POST request.
        with open(file_name, 'w') as f:
            for line in current_data.split():
                f.write(line + '\n')
            f.write(data['number'])
            
        return '', 201
    
class EndPointTwo(Resource):
    def get(self, get_data):
        """Calculates the sum of all the numeric values stored in 'data.txt' by
        making a GET request with whatever value.

        Returns:
            A JSON with the index 'result', containing the sum of all the
            numeric values stored in each line of the 'data.txt' file.

        Raises:
            TypeError: If a non numeric value is identified inside the
            'data.txt' file.
        """
        sum = 0
        with open(file_name, 'r') as f:
            data = f.readlines()
            for line in data:
                try:
                    sum += float(line)
                except:
                    raise TypeError("Only numeric values are allowed in the " + file_name + " file.")
        return {'result': sum}
    
api.add_resource(EndPointOne, '/end_point_one')
api.add_resource(EndPointTwo, '/end_point_two/<get_data>')

if __name__ == '__main__':
    app.run(debug=True)