import requests

TOKEN = "9944b09133c62bcf941av246dd0e4sdfdc6ee2b"  
response = requests.get("http://127.0.0.1:8000/api/", headers={    "Authorization": f"Token {TOKEN}"})
if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code)
    print(response.text)