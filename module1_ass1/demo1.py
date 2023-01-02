'''
The code deploys a flask app to display the folder and their respective files
Run the following lines to execute the code
1. conda env create -f blob_app_env.yml
2. conda activate azure_training
3. python demo1.py
'''
from azure.storage.blob import BlobServiceClient
from flask import Flask


def get_blob_from_container(container_name='demo1'):
    '''
    input: takes container name as input
    output: returns a list of blobs in the container
    '''
    connection_string = 'BlobEndpoint=https://assignment476.blob.core.windows.net/;QueueEndpoint=https://assignment476.queue.core.windows.net/;FileEndpoint=https://assignment476.file.core.windows.net/;TableEndpoint=https://assignment476.table.core.windows.net/;SharedAccessSignature=sv=2021-06-08&ss=b&srt=c&sp=rwdlaciytfx&se=2023-01-01T16:41:58Z&st=2022-12-21T08:41:58Z&spr=https&sig=UXnXurkcxkf0h0jZEHAiVMpY9haLTvIGWjYexELI2Bk%3D'
    container_name=container_name

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container= container_name)

    blob_list = container_client.list_blobs()
    folders = []
    for blob in blob_list:
        print("\t" + blob.name)
        folders.append(blob.name)
    return folders

#print(blob_service_client.list_containers()[0])
'''
download_file_path = os.path.join(local_path, str.replace(local_file_name ,'.txt', 'DOWNLOAD.txt'))
container_client = blob_service_client.get_container_client(container= container_name) 
print("\nDownloading blob to \n\t" + download_file_path)

with open(file=download_file_path, mode="wb") as download_file:
 download_file.write(container_client.download_blob(blob.name).readall())
'''


app = Flask(__name__)



@app.route("/", methods=['GET'])
def display_folders():
    #displays the dictionary containing folder name and their respective file
    folders = get_blob_from_container()
    folders_dict = {}
    for folder in folders:
        folder_name = folder.split('/')[0]
        files = folder.split('/')[1]
        folders_dict[folder_name] = files
    return(folders_dict)
        
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4400)