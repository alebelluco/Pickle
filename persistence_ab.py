# Package per salvare e rileggere il file su github
from github import Github
import pickle

username = "alebelluco"
token  = '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'



def upload_file(df,repository_name, file_path ):#username, token, file_path):
    encoded_data = pickle.dumps(df)
    # GitHub authentication
    g = Github(username,token)
    # Get repository
    try:
        repo = g.get_user().get_repo(repository_name)
    except Exception as e:
        print("Error accessing repository:", e)
        exit()
    

    try:    
        file = repo.get_contents(file_path)
        repo.update_file(file_path, "Updated data", encoded_data, file.sha)
        print("File updated successfully.")
    except:
        repo.create_file(file_path, 'File created', encoded_data)

def retrieve_file(repository_name, file_path):#username,token, file_path):
    g = Github(username,token)

    # Get repository
    try:
        repo = g.get_user().get_repo(repository_name)
    except Exception as e:
        print("Error accessing repository:", e)
        exit()
    contents = repo.get_contents(file_path)
    content_string = contents.decoded_content
    loaded_data = pickle.loads(content_string)
    
    return loaded_data
