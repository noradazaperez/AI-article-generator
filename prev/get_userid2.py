import requests
from requests.structures import CaseInsensitiveDict

url = "https://api.medium.com/v1/me"

headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer 289f6e4c3379ea917cb9b78faf012103efcbe05f12473673ef57ba8592013b135"

print(headers)
resp = requests.get(url, headers=headers)


#medium_id = '1ca65a90cc517c63f6bd26b9c6eb9ed1e7a3d487296132292c4ee43d028c8b93c'

print(resp.status_code)
print(resp.content)