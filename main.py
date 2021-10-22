import json

def save_creds(creds):
    json.dump(creds, open("password.json", "w"))

def get_creds(filename):
    return json.load(open(filename, "r"))

username = "ericschles"
password = "1234"

creds = {
    "username": username,
    "password": password
}
save_creds(creds)
creds == get_creds("password.json")
