import requests

def client():
    #credentials = {"username":"admin","password":"1234"}
    #response = requests.post("http://127.0.0.1:8000/api/dj-rest-auth/login/", data=credentials)
    token = "Token a5186a6ec2d3e6219f079d8539c896c98bd40a2c"
    headers = {"Authorization":token}
    response = requests.get("http://127.0.0.1:8000/api/profiles/",headers=headers)
    print("Status Code:", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__=="__main__":
    client()