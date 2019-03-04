import urllib
import json
    
    
def download_file():
    
    ##URL    
    
    my_url ="https://firebasestorage.googleapis.com/v0/b/halo2-1ce47.appspot.com/o/videos%2Fuser1?alt=media&token=07e0ebfe-52a9-4f2f-8889-f5b1a8134045"
    try:
        loader = urllib.request.urlretrieve(my_url, "newdata.mp4")
    except urllib.error.URLError as e:
        message = json.loads(e.read())
        print(message["error"]["message"])
    else:
        print(loader)
        
download_file()
