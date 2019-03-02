import requests

url = 'https://gateway-wdc.watsonplatform.net/natural-language-understanding/api/v1/analyze?version=2018-11-16'
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
api_key = ('apikey', '-x6m_vef22iFpYejuFHnolIJsDOB0eQUtTUqMRAdsJLY')
with open("data.json") as file:
    data = file.read()
r = requests.post(url, data=data, headers=headers, auth=api_key)
print(r.text)
