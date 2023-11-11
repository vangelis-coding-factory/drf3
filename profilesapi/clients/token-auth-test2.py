import requests

def client():
    data = {
        "username":"test1",
        "email":"test1@example.com",
        "password1":"changeme123",
        "password2":"changeme123"
    }

    response = requests.post("http://127.0.0.1:8000/api/dj-rest-auth/registration/", data=data)
    print("Status Code:", response.status_code)
    

if __name__=="__main__":
    client()