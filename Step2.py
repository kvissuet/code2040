import requests

task = {"token": "932a1b1ccd567e2d94ee4b3f8a1a2a2b", "github": "https://github.com/kvissuet/code2040" }
resp = requests.post('http://challenge.code2040.org/api/reverse', json=task)

task={"token": "932a1b1ccd567e2d94ee4b3f8a1a2a2b", "string": resp.text[::-1]}
requests.post('http://challenge.code2040.org/api/reverse/validate', json=task)

