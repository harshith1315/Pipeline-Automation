from flask import Flask, request, render_template
import pandas as pd
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

app = Flask(__name__)


azure_storage_connection_string = "DefaultEndpointsProtocol=https;AccountName=harshithprojecttest1;AccountKey=0BEWqGDuix3lq1m+SgqbsrmvkVp2QMeowtvd+c5MqoF4nZaWAePWzBY+zrzAo34w63EdDEe2nNBr+AStHo8x9Q==;EndpointSuffix=core.windows.net"




def upload_to_blob(file_path, blob_name,container_name):

    blob_service_client = BlobServiceClient.from_connection_string(azure_storage_connection_string)
    

    container_client = blob_service_client.get_container_client(container_name)

    with open(file_path, "rb") as data:
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(data, overwrite=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch-data', methods=['POST'])
def fetch_data():
    uploaded_file = request.files['file']
    container_name = request.form['cname']
    print(container_name)
    if uploaded_file.filename != '':
        file_path = 'uploads/' + uploaded_file.filename
        uploaded_file.save(file_path)
        
        blob_name = uploaded_file.filename
        data=pd.read_csv(file_path)
        if data.isnull().sum()[0]==0:
            upload_to_blob(file_path, blob_name,container_name)
            return 'File uploaded to database!'
        else:
            return 'dataset contain null values'
    else:
        return 'No file selected'

if __name__ == '__main__':
    app.run()
