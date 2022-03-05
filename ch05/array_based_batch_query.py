# Array-based Batch Queries using Python

import requests

queries = [
  {"query":"query {systemHealth}"},
  {"query":"query {systemHealth}"}
]

r = requests.post('http://localhost:5013/graphql', json=queries)

print(r.json())
