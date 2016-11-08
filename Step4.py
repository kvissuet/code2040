
import requests
import json
task = {"token": "932a1b1ccd567e2d94ee4b3f8a1a2a2b", "github": "https://github.com/kvissuet/code2040" }
resp = requests.post('http://challenge.code2040.org/api/prefix', json=task)
x=json.loads(resp.text)
p=x['prefix']
list1=[]
for a in x['array']:
	if a[0] != p[0] or a[1]!=p[1] or a[2]!=p[2]:
		list1.append(a)




task={"token": "932a1b1ccd567e2d94ee4b3f8a1a2a2b", "array": list1}
requests.post('http://challenge.code2040.org/api/prefix/validate', json=task)


