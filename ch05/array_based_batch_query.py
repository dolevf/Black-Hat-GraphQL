# Array-based Batch Queries using Python

import requests

data = [
  {"query":"query {systemHealth}"},
  {"query":"query {systemHealth}"}
]

r = requests.post('http://localhost:5013/graphql', json=data)

print(r.json())
