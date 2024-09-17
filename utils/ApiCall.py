import requests

# C'est une mauvaise pratique de mettre des urls en dur dans le code
# Il est préférable de les mettre dans un fichier de configuration ou d'environnement
BASE_URL = "http://localhost:3000"
RETRY = 3

def bet(amount, retry=0):
    if amount > 50:
        print("ERROR: Amount must be less than 50")
        return None
    headers = {"Cookie": f"clientID={cookie_value}"}
    response = requests.post(f"{BASE_URL}/deal", data={"bet": amount}, headers=headers)
    if response.status_code == 200:
        return response.json()
    elif retry >= RETRY:
        return bet(amount, retry + 1)
    else:
        return None


def load(retry=0):
    response = requests.get(f"{BASE_URL}/load")
    if response.status_code == 200:
        global cookie_value
        global cookie
        cookie_value = response.cookies.get("clientID")
        return response.content
    elif retry >= RETRY:
        return load(retry + 1)
    else:
        return None


def hit(retry=0):
    headers = {"Cookie": f"clientID={cookie_value}"}
    response = requests.post(f"{BASE_URL}/hit", headers=headers)
    if response.status_code == 200:
        return response.json()
    elif retry >= RETRY:
        return hit(retry + 1)
    else:
        return None


def hold(retry=0):
    headers = {"Cookie": f"clientID={cookie_value}"}
    response = requests.post(f"{BASE_URL}/hold", headers=headers)
    if response.status_code == 200:
        return response.json()
    elif retry >= RETRY:
        return hold(retry + 1)
    else:
        return None
