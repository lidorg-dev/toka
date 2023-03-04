from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse
import pandas as pd
import ast
import yaml
import time
from kubernetes import client, config, watch


app = Flask(__name__)
api = Api(app)

JOB_NAME = 'simple-job'
kubernetes_config_file_path = 'kube-config'

data = []i # Initialize empty list 


def create_job_object():
    # Configureate Pod template container
    container = client.V1Container(
        name='busybox',
        image='busybox',
        args=['sleep', '6'])
    # Create and configurate a spec section
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={'name': 'simple-job'}),
        spec=client.V1PodSpec(restart_policy='OnFailure', containers=[container]))
    # Create the specification of deployment
    spec = client.V1JobSpec(template=template)
    # Instantiate the job object
    job = client.V1Job(
        api_version='batch/v1',
        kind='Job',
        metadata=client.V1ObjectMeta(name=JOB_NAME),
        spec=spec)

    return job

def create_job(api_instance, job):
    api_response = api_instance.create_namespaced_job(
        body=job,
        namespace='default')
    print("Job created. status='%s'" % str(api_response.status))



def main():
    config.load_kube_config(kubernetes_config_file_path)
    batch_v1 = client.BatchV1Api()
    job = create_job_object()

    create_job(batch_v1, job)
    time.sleep(30)


@app.route('/connection', methods=['POST']) # '/connection' is our entry point for connection stuff
def con(): # methods go here

    data.append(request.get_json())  # add args to data
    main()
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

