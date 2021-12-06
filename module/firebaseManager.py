import ufirebase as firebase
from config import firebase_url, path_version

firebase.setURL(firebase_url)

def getData(location):
    path = path_version + location
    firebase.get(path, "value")
    
    return firebase.value

def storeData(location, data):
    path = path_version + location
    firebase.addto(path, data)
    
    return "Sucessfull store data to {0} with value {1}".format(path, data)
    
def putData(location, data):
    path = path_version + location
    firebase.put(path, data)
    
    return "Sucessfull update data to {0} with value {1}".format(path, data)
    
def deleteData(location):
    path = path_version + location
    firebase.delete(path)
