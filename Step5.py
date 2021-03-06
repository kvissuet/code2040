
import requests
import json
import dateutil.parser
import datetime

task = {"token": "932a1b1ccd567e2d94ee4b3f8a1a2a2b", "github": "https://github.com/kvissuet/code2040" }
resp = requests.post('http://challenge.code2040.org/api/dating', json=task)
x=json.loads(resp.text)
y=dateutil.parser.parse(x['datestamp'])
z=y +datetime.timedelta(0,x['interval'])
t=z.isoformat()
s=""
for x in range(19):
	s+=t[x]
s+="Z"
task = {"token": "932a1b1ccd567e2d94ee4b3f8a1a2a2b", "datestamp": s }
resp = requests.post('http://challenge.code2040.org/api/dating/validate', json=task)