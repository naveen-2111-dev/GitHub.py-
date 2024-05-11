import requests

def Apicall(mode = "", username = "", reponame = "", Payload = ""):
    Base_url = "https://api.github.com"
    URI = DataCondition(Base_url,mode,Payload,username,reponame)
    try:
        response = requests.get(URI).json()
        if response:
            return response
    except Exception as err:
        print(f"error {err}")

def DataCondition(base,mode,payload,username,reponame):
    if mode:
        base += f"/{mode}"

    if username:
        base += f"/{username}"

    if reponame:
        base += f"/{reponame}"  

    if payload:
        base += f"/{payload}"

    return base
