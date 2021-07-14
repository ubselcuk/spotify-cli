import json

with open("/home/anxiety/Documents/spotify-cli/user.json", "r") as f:
    data = json.load(f)


def client_id(take):
    data['client_id'] = take
    with open("user.json", "w") as f:
        json.dump(data, f)

def client_secret(take):
    data['client_secret'] = take
    with open("user.json", "w") as f:
        json.dump(data, f)

def redirect_uri(take):
    data['redirect_uri'] = take
    with open("user.json", "w") as f:
        json.dump(data, f)

def username(take):
    data['username'] = take
    with open("user.json", "w") as f:
        json.dump(data, f)

def current_user():
    print(
        "\nclient id: " + data['client_id'] + 
        "\nclient secret: " + data['client_secret'] + 
        "\nredirect uri: " + data['redirect_uri'] + 
        "\nusername: " + data['username'] + "\n"
        )

def delete_user():
    data['client_id'] = ""
    data['client_secret'] = ""
    data['redirect_uri'] = ""
    data['username'] = ""
    with open("user.json", "w") as f:
        json.dump(data, f)