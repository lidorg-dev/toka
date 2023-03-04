from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

data = []i # Initialize empty list 

@app.route('/connection', methods=['POST']) # '/connection' is our entry point for connection stuff

def con(): # methods go here

    data.append(request.get_json())  # add args to data
    return {'data': data} , 200 # return the data 



if __name__ == '__main__':
    app.run(host="0.0.0.0")  # run our Flask app

# tried to do something complex with classe and it didn't work so leave the code here

#class Connection(Resource):
    # methods go here
#    def post(self):
#        parser = reqparse.RequestParser()  # initialize

#        parser.add_argument('ip', required=True)  # add args
#        ip = args['ip']
#        print(ip)
#        parser.add_argument('port', required=True)
#        parser.add_argument('username', required=True)
#        parser.add_argument('password', required=True)
#
#        args = parser.parse_args()  # parse arguments to dictionary
        # create new dataframe containing new values
#        new_data = pd.DataFrame({
#            'IP': args['ip'],
#            'PORT': args['port'],
#            'USERNAME': args['username'],
#            'PASSWORD': args['password']
#        })
#        return {'data': new_data.to_dict()}, 200  # return data with 200 OK

#api.add_resource(Connection, '/connection') # '/connection' is our entry point for connection stuff

