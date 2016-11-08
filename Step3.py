import requests
import json
task = {"token": "932a1b1ccd567e2d94ee4b3f8a1a2a2b", "github": "https://github.com/kvissuet/code2040" }
resp = requests.post('http://challenge.code2040.org/api/haystack', json=task)
x=json.loads(resp.text)



task={"token": "932a1b1ccd567e2d94ee4b3f8a1a2a2b", "needle": str(x['haystack'].index(x['needle']))}
requests.post('http://challenge.code2040.org/api/haystack/validate', json=task)

